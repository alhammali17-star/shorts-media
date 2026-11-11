#!/usr/bin/env python3
"""Render a "شغّل مخك" riddle Short (1080x1920, 30fps, 18s, silent) from a JSON riddle.

Usage: python3 render.py riddle.json out.mp4 [--frames t1,t2,...]  (--frames writes PNG stills instead)
riddle.json: {"hook1","hook2","question":[lines],"answer","explanation":[lines]}
"""
import json, subprocess, sys, pathlib, shutil
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
FPS, DUR = 30, 18.0
# per-template length and soundtrack (v2 = owner-approved 13 s fast-hook layout, 2026-11-08)
V2 = {"template_v2.html": (13.0, "track_v2.wav"),
      # v3 = v2 timeline with a short loop-friendly ending; the same track, cut at 11.5 s by -shortest
      "template_v3.html": (11.5, "track_v2.wav")}


def chrome():
    for c in ("google-chrome", "chromium", "chromium-browser"):
        p = shutil.which(c)
        if p:
            return p
    return None


def main():
    global DUR
    data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    dur, track = V2.get(data.get("template", "template.html"), (18.0, "track.wav"))
    DUR = dur
    data.setdefault("hook1", "لغز صعب…")
    data.setdefault("hook2", "ركّز معايا!")
    out = pathlib.Path(sys.argv[2])
    stills = None
    if "--frames" in sys.argv:
        stills = [float(x) for x in sys.argv[sys.argv.index("--frames") + 1].split(",")]
    with sync_playwright() as p:
        kw = {"args": ["--force-color-profile=srgb", "--disable-gpu"]}
        exe = chrome()
        if exe:
            kw["executable_path"] = exe
        b = p.chromium.launch(**kw)
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto((HERE / data.get("template", "template.html")).as_uri())
        pg.evaluate("document.fonts.ready")
        pg.evaluate("d => setData(d)", data)
        pg.wait_for_timeout(300)
        if stills:
            out.mkdir(parents=True, exist_ok=True)
            for t in stills:
                pg.evaluate(f"renderAt({t})")
                pg.screenshot(path=str(out / f"s{t}.png"))
            b.close()
            return
        ff = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg",
             "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
             "-movflags", "+faststart", str(out)],
            stdin=subprocess.PIPE)
        n = int(FPS * DUR)
        for i in range(n):
            pg.evaluate(f"renderAt({i / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        ff.stdin.close()
        ff.wait()
        b.close()
    if ff.returncode != 0:
        sys.exit("ffmpeg failed")
    add_audio(out, track)


def add_audio(out, name="track.wav"):
    """Mux the channel soundtrack (assets/track.wav, made by make_audio.py) into the video."""
    track = HERE / "assets" / name
    if not track.exists():
        subprocess.run([sys.executable, str(HERE / "make_audio.py")] + (["v2"] if name != "track.wav" else []), check=True)
    tmp = out.with_suffix(".tmp.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(out), "-i", str(track), "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(tmp)], check=True)
    tmp.replace(out)


if __name__ == "__main__":
    main()

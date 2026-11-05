#!/usr/bin/env python3
"""Render a Byte Hook Short (1080x1920, 30fps, English, with music) from a JSON script.

Usage: python3 bytehook/render.py script.json out.mp4 [--frames t1,t2,...]
script.json keys: tag, hook (HTML ok, <em> = red), sub, points_title, points [{t,d}],
fix_label, fix (HTML ok), fix_sub, question (comment prompt), optional step (s per point).
"""
import json, subprocess, sys, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
FPS = 30


def main():
    data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = pathlib.Path(sys.argv[2])
    stills = None
    if "--frames" in sys.argv:
        stills = [float(x) for x in sys.argv[sys.argv.index("--frames") + 1].split(",")]
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--force-color-profile=srgb", "--disable-gpu"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto((HERE / "template.html").as_uri())
        pg.evaluate("document.fonts.ready")
        pg.evaluate("d => setData(d)", data)
        pg.wait_for_timeout(300)
        dur = pg.evaluate("window.DUR")
        if stills:
            out.mkdir(parents=True, exist_ok=True)
            for t in stills:
                pg.evaluate(f"renderAt({t})")
                pg.screenshot(path=str(out / f"s{t}.png"))
            b.close()
            print(f"dur={dur}")
            return
        ff = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg",
             "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
             "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
        for i in range(int(FPS * dur)):
            pg.evaluate(f"renderAt({i / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        ff.stdin.close(); ff.wait(); b.close()
    if ff.returncode != 0:
        sys.exit("ffmpeg failed")
    track = HERE / "track.wav"
    if not track.exists():
        subprocess.run([sys.executable, str(HERE / "make_audio.py")], check=True)
    tmp = out.with_suffix(".tmp.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(out), "-i", str(track), "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(tmp)], check=True)
    tmp.replace(out)
    print(f"ok {out} dur={dur}")


if __name__ == "__main__":
    main()

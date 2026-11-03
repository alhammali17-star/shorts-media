#!/usr/bin/env python3
"""Render a "شغّل مخك" riddle Short (1080x1920, 30fps, 18s, silent) from a JSON riddle.

Usage: python3 render.py riddle.json out.mp4 [--frames t1,t2,...]  (--frames writes PNG stills instead)
riddle.json: {"hook1","hook2","question":[lines],"answer","explanation":[lines]}
"""
import json, subprocess, sys, pathlib, shutil
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
FPS, DUR = 30, 18.0


def chrome():
    for c in ("google-chrome", "chromium", "chromium-browser"):
        p = shutil.which(c)
        if p:
            return p
    return None


def main():
    data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
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
        pg.goto((HERE / "template.html").as_uri())
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


if __name__ == "__main__":
    main()

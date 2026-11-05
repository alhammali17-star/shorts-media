#!/usr/bin/env python3
"""Original royalty-free Byte Hook soundtrack: dark synth pulse + beat, 40 s (videos cut it with -shortest).
Output: bytehook/track.wav"""
import numpy as np, wave, pathlib

SR, DUR = 44100, 40.0
t = np.arange(int(SR * DUR)) / SR
out = np.zeros_like(t)

def add(sig, start):
    i = int(start * SR); j = min(len(out), i + len(sig))
    if i < len(out): out[i:j] += sig[: j - i]

bpm = 118; beat = 60 / bpm; step = beat / 4
bass = [55, 55, 65.41, 49]  # A1 A1 C2 G1 per bar
n = 0
while n * step < DUR:
    s = n * step; bar = int(s // (beat * 4)) % 4
    tt = np.arange(int(step * 0.9 * SR)) / SR
    f = bass[bar] * (2 if n % 8 in (3, 6) else 1)
    saw = 2 * ((f * tt) % 1) - 1
    add(saw * np.exp(-tt * 9) * 0.10, s)
    if n % 4 == 0:
        kt = np.arange(int(0.2 * SR)) / SR
        add(np.sin(2 * np.pi * (110 * np.exp(-kt * 20)) * kt) * np.exp(-kt * 12) * 0.45, s)
    if n % 8 == 4:
        sn = np.random.default_rng(n).normal(0, 1, int(0.12 * SR)) * np.exp(-np.arange(int(0.12 * SR)) / SR * 30)
        add(sn * 0.10, s)
    if n % 2 == 1:
        h = np.random.default_rng(n).normal(0, 1, int(0.03 * SR)) * np.exp(-np.arange(int(0.03 * SR)) / SR * 120)
        add(h * 0.035, s)
    n += 1
# arp lead (A minor pentatonic), quiet
arp = [440, 523.25, 659.25, 783.99, 659.25, 523.25]
for k in range(int(DUR / (beat / 2))):
    tt = np.arange(int(beat / 2 * 0.8 * SR)) / SR
    add(np.sin(2 * np.pi * arp[k % len(arp)] * tt) * np.exp(-tt * 6) * 0.045, k * beat / 2)
out[: int(0.2 * SR)] *= np.linspace(0, 1, int(0.2 * SR))
out = np.tanh(out * 1.5)
out = out / np.max(np.abs(out)) * 0.6
p = pathlib.Path(__file__).resolve().parent / "track.wav"
with wave.open(str(p), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out * 32767).astype("<i2").tobytes())
print(p)

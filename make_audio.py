#!/usr/bin/env python3
"""Synthesize the channel's 18 s soundtrack (original, royalty-free): soft pad + light beat,
clock ticks during the 5-second countdown, a chime at the answer. Output: assets/track.wav.
The video timeline is fixed, so one track fits every Short."""
import numpy as np, wave, pathlib

SR, DUR = 44100, 18.0
t = np.arange(int(SR * DUR)) / SR
out = np.zeros_like(t)

def env(x, a, d):  # attack/decay envelope over a note of length len(x)
    n = len(x); e = np.ones(n)
    na, nd = int(a * SR), int(d * SR)
    if na: e[:na] = np.linspace(0, 1, na)
    if nd: e[-nd:] *= np.linspace(1, 0, nd)
    return x * e

def add(sig, start):
    i = int(start * SR); j = min(len(out), i + len(sig))
    out[i:j] += sig[: j - i]

def tone(freq, length, kind="sine"):
    tt = np.arange(int(length * SR)) / SR
    if kind == "sine":
        return np.sin(2 * np.pi * freq * tt)
    return (np.sin(2 * np.pi * freq * tt) + 0.35 * np.sin(4 * np.pi * freq * tt) + 0.15 * np.sin(6 * np.pi * freq * tt))

# chord pad: Am - F - C - G, 2 s each, soft
chords = [[220, 261.63, 329.63], [174.61, 220, 261.63], [196, 261.63, 329.63], [196, 246.94, 293.66]]
for k in range(9):
    for f in chords[k % 4]:
        add(env(tone(f, 2.2, "rich"), 0.25, 0.6) * 0.05, k * 2.0)

# beat: kick on every beat (100 bpm), hat on offbeats; quieter during the countdown
bpm = 100; beat = 60 / bpm
n = 0
while n * beat < DUR - 0.3:
    s = n * beat
    vol = 0.35 if 6.0 <= s < 11.0 else 1.0
    tt = np.arange(int(0.18 * SR)) / SR
    kick = np.sin(2 * np.pi * (120 * np.exp(-tt * 18)) * tt) * np.exp(-tt * 14)
    add(kick * 0.32 * vol, s)
    hat = np.random.default_rng(n).normal(0, 1, int(0.04 * SR)) * np.exp(-np.arange(int(0.04 * SR)) / SR * 90)
    add(hat * 0.03 * vol, s + beat / 2)
    n += 1

# countdown ticks at 6,7,8,9,10 s (clock tick, higher on the last)
for i, s in enumerate([6, 7, 8, 9, 10]):
    f = 1500 if i < 4 else 2000
    add(env(tone(f, 0.06), 0.002, 0.05) * 0.22, s)

# answer chime at 11.1 s
for f, d in [(880, 0), (1318.5, 0.08), (1760, 0.16)]:
    add(env(tone(f, 0.9), 0.005, 0.85) * 0.12, 11.1 + d)

# CTA swoosh at 15 s
sw = np.random.default_rng(7).normal(0, 1, int(0.5 * SR))
sw *= np.hanning(len(sw)) * 0.05
add(sw, 15.0)

# master: fade in/out, normalize to -3 dBFS
out[: int(0.3 * SR)] *= np.linspace(0, 1, int(0.3 * SR))
out[-int(1.2 * SR):] *= np.linspace(1, 0, int(1.2 * SR))
out = out / np.max(np.abs(out)) * 0.7
p = pathlib.Path(__file__).resolve().parent / "assets" / "track.wav"
p.parent.mkdir(exist_ok=True)
with wave.open(str(p), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out * 32767).astype("<i2").tobytes())
print(p)

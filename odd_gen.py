#!/usr/bin/env python3
"""Make one "لقى المختلف" (odd-one-out) puzzle JSON. Deterministic per seed (e.g. a date).
Usage: python3 odd_gen.py <seed> <out.json>"""
import json, random, sys
PAIRS = [("ح","خ"),("ب","ت"),("ع","غ"),("ص","ض"),("ر","ز"),("د","ذ"),("س","ش"),("ط","ظ"),("ف","ق"),
         ("٦","٧"),("٨","٩"),("6","9"),("O","Q"),("E","F"),("M","N"),("69","96"),("18","81"),("وو","ؤو")]
seed = sys.argv[1]; rnd = random.Random(seed)
base, odd = rnd.choice(PAIRS)
if rnd.random() < 0.5: base, odd = odd, base
rows, cols = (6, 6) if len(base) == 1 else (6, 5)
r, c = rnd.randrange(rows), rnd.randrange(cols)
d = {"kind": "odd", "hook1": "لقى المختلف…", "hook2": rnd.choice(["عندك 5 ثواني بس!", "عيونك قوية؟", "أغلب الناس ما يلقوهاش!"]),
     "grid": {"rows": rows, "cols": cols, "base": base, "odd": odd, "r": r, "c": c},
     "pill": "دوّر… عندك 5 ثواني", "apill": "الجواب", "answer": "هني!",
     "explanation": [f"السطر {r+1}، الخانة {c+1} من اليسار"],
     "cta": ["كم ثانية خذيت؟", "اكتبها في التعليقات", "اشترك لتحدي جديد كل يوم"]}
json.dump(d, open(sys.argv[2], "w"), ensure_ascii=False)
print(base, odd, r, c)

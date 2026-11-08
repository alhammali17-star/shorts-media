# Daily run — قناة "شغّل مخك" (YouTube @shaghelmokhak1)

The channel is "شغّل مخك" — anything that works the viewer's brain, not riddles only. Publish TWO Shorts per day (owner, 2026-11-08), automatically, and keep the office page (OFFICE.md) live while doing it. Read OFFICE.md, LEARNINGS.md and SCHEDULE.md first, and each employee's `staff/<id>` doc (its `skills` and `thinking`) before it works.

## Slots (times and formats live in SCHEDULE.md — only the Sunday meeting or the owner changes them)
**Template v2 (owner-approved 2026-11-08) is the default for every kind:** add `"template":"template_v2.html"` and a `"hook"` to each JSON. v2 is 13 s, shows the hook banner AND the puzzle on frame 0 (no empty intro), countdown 1.5–6.5 s, answer 6.6 s, CTA 10.3 s; render.py picks the 13 s soundtrack (`assets/track_v2.wav`) by itself. `hook` = one trap/curiosity line, ≤ 24 characters, no emoji, different from the last 5 hooks (e.g. "90% يغلطوا في اللغز هذا"، "سؤال سهل… لكن فيه فخ!"، "عيونك قوية؟ لقى المختلف"، "حيلة تحفظ بيها أي رقم"). v2 has its own CTA per kind, so `pill`/`cta`/`hook1`/`hook2` are not needed. The old template.html / template_quiz.html stay untouched as a fallback.
Formats (`kind` / bank):
- `riddle` — template.html, bank `bank.json`.
- `tip` — نصيحة لمخك, template.html with `kind:"tip"`, bank `tips.json`. JSON = the tips.json entry + `kind:"tip"`, `hook1:"نصيحة لمخك 🧠"`, `hook2` (short, e.g. "تخدم من أول يوم"), `pill:"جرّب الطريقة هذي"`, `cta:["احفظ الفيديو","وجرّبها الليلة","اشترك لنصيحة جديدة كل يوم"]`.
- `quiz` — multiple choice, `template_quiz.html`, bank `bank_quiz.json` (fields: template, tag, hook1, hook2, question[], options[3], correct 0-2, explanation[]).
- `odd` — لقى المختلف, generated: `python3 odd_gen.py <YYYY-MM-DD> riddles/<YYYY-MM-DD>_odd.json` (never needs a bank).
Never edit template.html or template_quiz.html; a new format gets its own template file only after the Sunday meeting approves it.

## Before making anything
Call Metricool `getScheduledPosts` (blogId 7526793, today, Africa/Tripoli). A slot that already has a post is filled — make videos only for the empty slots (e.g. on 2026-11-05 the 13:00 riddle «الساعة» is already scheduled).

## Team, in order (each one: status working → do the work → done/error, per OFFICE.md)
1. **رحاب — trend researcher** (free sources only: WebSearch for current Arabic brain/quiz/tips Shorts trends, hooks, formats). Write 3 short findings in her `task`/`thinking`. No vidIQ credits.
2. **طارق — trend filter**: keep only what fits the channel (family-safe, Libyan dialect, our templates, not a repeat). Output: the hook style for today.
3. **نوري — writer**: take the first unused entry from each bank today's slots need. When a bank runs low (riddles < 10, tips < 5, quiz < 5 unused), write 10 new entries in the same shape (riddles: question 2–3 short lines, answer ending "!", explanation 2 lines; tips: question 2 lines + 3 steps ≤ ~28 chars + `source`; quiz: certain, checkable facts), checked at the idea level against used.json and all banks, and append them.
4. **هدى — checker**: riddles: answer correct and unambiguous, not in `used.json` (`already_on_channel` + `published`; banned: plane riddles, family-relation riddles). Quiz and tips: only certain facts / well-established advice with a real source — verify anything new with one WebSearch; no medical, diet, medicine or money advice. All: Libyan wording (never "بلاصة", "فتّيت"), short lines. On failure send it back to نوري.
5. **خالد — editor**: render each JSON: `python3 render.py riddles/<file>.json videos/<YYYY-MM-DD>_<id>.mp4` (setup if missing: `pip install --break-system-packages playwright`; uses system google-chrome; render.py picks the template from the JSON and adds the channel soundtrack). Extract frames at t=0, 3, 7.5, 11.5 (v2; 4, 8, 13, 16 for old templates) and look at them — frame 0 must already show the hook and the puzzle: nothing clipped or overlapping, Arabic shaped, audio stream present.
6. **أسماء — publisher**:
   - Titles ≤ 70 chars, one emoji, not one of the last 5 titles. Riddle/quiz: trap-style hooks that worked (LEARNINGS.md). Odd: e.g. "لقى الحرف المختلف في 5 ثواني 👀". Tip: e.g. "حيلة صغيرة تخلي مخك يحفظ أي حاجة 🧠".
   - Description by kind — riddle: `جاوب في التعليقات قبل ما يطلع الحل 👇\n#shorts #لغز #شغل_مخك #تحدي`; quiz: `اختار أ ولا ب ولا ج… واكتب الحرف في التعليقات قبل ما يطلع الحل 👇\n#shorts #شغل_مخك #سؤال #معلومات #تحدي`; odd: `كم ثانية خذيت؟ 👇\n#shorts #تحدي #اختبار_نظر #شغل_مخك`; tip: `احفظ الفيديو وجرّبها 👇\n#shorts #نصائح #تطوير_الذات #شغل_مخك`.
   - Commit + push the mp4s and updated banks/used.json to `main` (pull --rebase first); confirm each `https://raw.githubusercontent.com/alhammali17-star/shorts-media/main/videos/<file>.mp4` returns 200.
   - Before scheduling, `getScheduledPosts` for today: never create a second post in a slot that already has one.
   - Metricool `createScheduledPost` per video: blogId `7526793`, providers youtube, youtubeData {title, type:"short", privacy:"public", madeForKids:false, category: tip "EDUCATION", others "ENTERTAINMENT"}, text = description, media = [raw URL], autoPublish true, at that slot's time today (Africa/Tripoli). A slot already past → skip it today, never stack posts.
   - Append to `used.json.published`: {date, slot, kind, id, title, file, plannerUrl}; commit + push.
7. End: one batch to the office (statuses, XP, history, log lines) and one short Libyan-Arabic message to the owner: what goes out at which time. If anything failed, say exactly which step and why; never post a broken or repeated video.

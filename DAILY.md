# Daily run — قناة "شغّل مخك" (YouTube @shaghelmokhak1)

Goal: publish THREE new Shorts per day at 13:00, 16:00 and 19:00 Africa/Tripoli (Metricool best-time data for YouTube, checked 2026-11-04: weekday peak 16:00 ≈12k, 13:00 ≈9.5k, 19:00 ≈7.2k, 23:00 only ≈2.8k — so 23:00 is dropped). The channel is "شغّل مخك", not only riddles: 13:00 and 19:00 = riddle (template.html), 16:00 = a different brain format (see below), automatically, in the exact channel template, and keep the office page (OFFICE.md) live while doing it. Read OFFICE.md and LEARNINGS.md first, and each employee's `staff/<id>` doc (its `skills` and `thinking`) before it works.

## 16:00 format — "تطوير" (not only riddles)
- Default: multiple-choice quiz (template_quiz.html, bank `bank_quiz.json`, fields: template, tag, hook1, hook2, question[], options[3], correct (0-2), explanation[]). Take the first unused id; facts must be certain and checkable (هدى verifies with WebSearch if unsure). When fewer than 5 unused remain, نوري writes 10 more.
- Every Sunday the CEO compares 16:00 views with the riddle slots; if the quiz loses 2 weeks running, try another brain format (true/false fact, math trick, memory tip) in a new template file — never edit template.html.
- Re-check `getBestTimeToPostByNetwork` (youtube, next 7 days) every Sunday; if the top hours move, change the three slots here and log why.

## Team, in order (each one: status working → do the work → done/error, per OFFICE.md)
1. **رحاب — trend researcher** (free sources only: WebSearch for current Arabic riddle/quiz Shorts trends, title hooks, formats). Write 3 short findings in her `task`/`thinking`. No vidIQ credits.
2. **طارق — trend filter**: keep only what fits the channel (family-safe riddle, Libyan dialect, our fixed template, not a repeat). Output: one angle for today (riddle type + title hook).
3. **نوري — writer**: pick TWO riddles: take the first unused entries in `bank.json` that fits the angle (or the first unused if none fit). If fewer than 10 unused remain, write 10 new riddles (question 2–3 short lines, answer ending "!", explanation 2 short lines), checked against used.json + bank.json at the idea level, and append them.
4. **هدى — checker**: answer correct and unambiguous, Libyan wording (never "بلاصة", "فتّيت"), each question line ≤ ~22 characters, not in `used.json` (`already_on_channel` + `published`, banned families: plane riddles, family-relation riddles). On failure send it back to نوري (next entry).
5. **خالد — editor**: for each of the two riddles, write `riddles/<id>.json`, run `python3 render.py riddles/<id>.json videos/<YYYY-MM-DD>_<id>.mp4` (setup if missing: `pip install --break-system-packages playwright`; uses system google-chrome). Extract frames at t=4, 8, 13, 16 with ffmpeg and look at them: text inside the card, no clipping, Arabic shaped. Never change template.html.
6. **أسماء — publisher**:
   - Title ≤ 70 chars in the style that works (see LEARNINGS.md; e.g. "اقرا السؤال كويس… فيه فخ!", "سؤال سهل لكن أغلب الناس تطيح فيه!"), not one of the last 3 titles, one emoji.
   - Description: `جاوب في التعليقات قبل ما يطلع الحل 👇\n#shorts #ألغاز #لغز #شغل_مخك #تحدي`
   - render.py adds the channel soundtrack (assets/track.wav, original, royalty-free) automatically; check the mp4 has an audio stream.
   - Commit + push the mp4 and updated used.json/bank.json to `main`; confirm `https://raw.githubusercontent.com/alhammali17-star/shorts-media/main/videos/<file>.mp4` returns 200.
   - Metricool `createScheduledPost`: blogId `7526793`, providers youtube, youtubeData {title, type:"short", privacy:"public", madeForKids:false, category:"ENTERTAINMENT"}, text = description, media = [raw URL], autoPublish true, one post per video: riddle 1 at 13:00, quiz at 16:00, riddle 2 at 19:00 Africa/Tripoli (if a slot is already past, now + 20 minutes; never two posts less than 3 hours apart unless both slots passed). Use two different title styles for the two videos.
   - Append to `used.json.published`: {date, id, title, file, plannerUrl}; commit + push.
7. End: one batch to the office (statuses, XP, history, log lines) and one short Libyan-Arabic message to the owner: all three videos, titles, times. If anything failed, say exactly which step and why; never post a broken or repeated video.

# Daily run — قناة "شغّل مخك" (YouTube @shaghelmokhak1)

Goal: publish ONE new riddle Short per day, automatically, in the exact channel template, and keep the office page (OFFICE.md) live while doing it. Read OFFICE.md and LEARNINGS.md first, and each employee's `staff/<id>` doc (its `skills` and `thinking`) before it works.

## Team, in order (each one: status working → do the work → done/error, per OFFICE.md)
1. **رحاب — trend researcher** (free sources only: WebSearch for current Arabic riddle/quiz Shorts trends, title hooks, formats). Write 3 short findings in her `task`/`thinking`. No vidIQ credits.
2. **طارق — trend filter**: keep only what fits the channel (family-safe riddle, Libyan dialect, our fixed template, not a repeat). Output: one angle for today (riddle type + title hook).
3. **نوري — writer**: take the first unused entry in `bank.json` that fits the angle (or the first unused if none fit). If fewer than 5 unused remain, write 10 new riddles (question 2–3 short lines, answer ending "!", explanation 2 short lines), checked against used.json + bank.json at the idea level, and append them.
4. **هدى — checker**: answer correct and unambiguous, Libyan wording (never "بلاصة", "فتّيت"), each question line ≤ ~22 characters, not in `used.json` (`already_on_channel` + `published`, banned families: plane riddles, family-relation riddles). On failure send it back to نوري (next entry).
5. **خالد — editor**: write `riddles/<id>.json`, run `python3 render.py riddles/<id>.json videos/<YYYY-MM-DD>_<id>.mp4` (setup if missing: `pip install --break-system-packages playwright`; uses system google-chrome). Extract frames at t=4, 8, 13, 16 with ffmpeg and look at them: text inside the card, no clipping, Arabic shaped. Never change template.html.
6. **أسماء — publisher**:
   - Title ≤ 70 chars in the style that works (see LEARNINGS.md; e.g. "اقرا السؤال كويس… فيه فخ!", "سؤال سهل لكن أغلب الناس تطيح فيه!"), not one of the last 3 titles, one emoji.
   - Description: `جاوب في التعليقات قبل ما يطلع الحل 👇\n#shorts #ألغاز #لغز #شغل_مخك #تحدي`
   - Commit + push the mp4 and updated used.json/bank.json to `main`; confirm `https://raw.githubusercontent.com/alhammali17-star/shorts-media/main/videos/<file>.mp4` returns 200.
   - Metricool `createScheduledPost`: blogId `7526793`, providers youtube, youtubeData {title, type:"short", privacy:"public", madeForKids:false, category:"ENTERTAINMENT"}, text = description, media = [raw URL], autoPublish true, publicationDate today 18:00 Africa/Tripoli (if already past, now + 20 minutes).
   - Append to `used.json.published`: {date, id, title, file, plannerUrl}; commit + push.
7. End: one batch to the office (statuses, XP, history, log lines) and one short Libyan-Arabic message to the owner: riddle, title, time. If anything failed, say exactly which step and why; never post a broken or repeated video.

# Daily run — قناة "شغّل مخك" (YouTube @shaghelmokhak1)

Goal: publish ONE new riddle Short per day, automatically, in the exact channel template. Owner approved fully automatic public posting.

## Team (do each role in order, in this session)
1. **Researcher** — choose the riddle.
   - Read `used.json` (`already_on_channel` + `published`). Never reuse an idea, even reworded, and avoid the banned families listed there (plane riddles, family-relation riddles).
   - Take the first entry in `bank.json` whose `id` is not in `published`.
   - If fewer than 5 unused entries remain, write 10 new short riddles in Libyan dialect (same JSON shape: question = 2–3 short lines, answer ending with "!", explanation = 2 short lines), check each against used.json and bank.json at the idea level, and append them to bank.json.
2. **Checker** — confirm the answer is correct and unambiguous, the wording is Libyan (not Tunisian/Algerian; no "بلاصة", "فتّيت"), each question line ≤ ~22 characters, and the riddle is family-friendly. If it fails, skip it and take the next one.
3. **Editor** — render: `python3 render.py riddles/<id>.json videos/<YYYY-MM-DD>_<id>.mp4` (write the riddle JSON first; hook defaults to "لغز صعب…/ركّز معايا!"). Setup if missing: `pip install --break-system-packages playwright` (uses system google-chrome). Then extract frames at t=4, 8, 13, 16 with ffmpeg and look at them: text must be inside the card, no clipping, Arabic shaped correctly. Never change template.html.
4. **Publisher**
   - Title (≤ 70 chars), trend style like the channel's best performers ("اقرا السؤال كويس… فيه فخ!", "سؤال سهل لكن أغلب الناس تطيح فيه!", "99% يغلطوا فيه… وإنت؟"). Rotate; don't repeat the last 3 titles in `published`. Add one fitting emoji.
   - Description: `جاوب في التعليقات قبل ما يطلع الحل 👇\n#shorts #ألغاز #لغز #شغل_مخك #تحدي`
   - Commit and push the mp4 + updated used.json/bank.json to `main`.
   - Public URL: `https://raw.githubusercontent.com/alhammali17-star/shorts-media/main/videos/<file>.mp4` — confirm it returns 200 before scheduling.
   - Metricool `createScheduledPost`: blogId `7526793`, providers youtube, youtubeData {title, type:"short", privacy:"public", madeForKids:false, category:"ENTERTAINMENT"}, text = description, media = [raw URL], autoPublish true, publicationDate today 18:00 Africa/Tripoli (if already past, now + 20 minutes).
   - Append to `used.json.published`: {date, id, title, file, plannerUrl}. Commit and push.
5. **Report** — one short message to the owner in Libyan Arabic: the riddle, the title, the scheduled time. If any step failed, say exactly which and why; do not post a broken video.

Do not spend vidIQ credits in the daily run.

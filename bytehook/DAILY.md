# Byte Hook — daily run

Channel: **Byte Hook** (@ByteHookShorts, channel id UCDHGcqiUpFiopPdH5P8sv3A), English Shorts on AI, tech and cybersecurity.
Goal: highest revenue per view, so every video must give real, specific, evergreen value. No news, no prices, no version numbers, nothing that expires.
Owner is Libyan; send him messages in Libyan Arabic only.

Two Shorts per day, scheduled in YouTube Studio (free) for **19:00 and 22:00 Africa/Tripoli** the same day (midday / afternoon US Eastern).

## Steps
0. If `used.json` already has 2 entries dated today (Africa/Tripoli), today is done: end with one short line, do nothing else.
1. `cd bytehook && python3 make_audio.py` only if `track.wav` is missing.
2. Read `used.json`. Pick 2 new topics that are NOT in it and not close duplicates. Rotate categories: one CYBERSECURITY (scams, accounts, privacy) and one AI or TECH (a tool feature, a phone/PC trick). Only facts you are sure are true and stable; if in doubt, pick another topic. No medical, legal or financial advice. Never name a person.
3. Write each script as `scripts/NNN_slug.json` (next number) with the same keys as `scripts/001_sim_swap.json`:
   - `hook`: max ~8 words, curiosity or danger, one word in `<em>` (red). It is the most important line.
   - `sub`: one short tease line.
   - 3 points, each `t` ≤ 4 words, `d` ≤ 8 words.
   - `fix`: the payoff in ≤ 9 words. `question`: a yes/no or A/B comment prompt.
   - `title` ≤ 60 chars ending with `#shorts`; `description` 1–2 sentences + 4–5 hashtags.
4. Render: `python3 render.py scripts/NNN_slug.json out/NNN_slug.mp4`. First run `--frames 1.5,6,12,17,20.5` to a scratch folder and LOOK at the stills: text inside the frame, nothing overlapping, no typos. Fix and re-render if needed.
5. Upload with Claude in Chrome (load its tools with one ToolSearch; tabs_context_mcp with createIfEmpty, own tab):
   - Open `https://studio.youtube.com/channel/UCDHGcqiUpFiopPdH5P8sv3A/videos/upload?d=ud`
   - `find` the hidden `input type=file` in the upload dialog, `file_upload` the mp4 from its absolute path in this container.
   - Title: select-all then type. Description. Choose "لا، الفيديو ليس مخصّصًا للأطفال".
   - Next ×3 to "مستوى العرض", choose **جدولة (Schedule)**, set today's date and the time (19:00 or 22:00, page shows Tripoli time), then click جدولة. Screenshot to confirm.
   - Close the tab you opened.
6. Append both entries to `used.json` (`{"id","date","hook","category","scheduled"}`), commit (`bytehook: YYYY-MM-DD`), `git pull --rebase`, push. Never commit `out/` (videos are gitignored).
7. Finish with one short SendUserMessage in Libyan Arabic: the two hooks and their times, or exactly which step failed and why.

If Chrome is not reachable (computer off): still write and render the scripts, commit them, and tell the owner in one line that the upload waits for the computer.

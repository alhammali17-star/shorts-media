# Sunday meeting — weekly report, plan, dev lab, levels

Read OFFICE.md first. CEO = سالمة runs the meeting; set her status working.

1. **Numbers**: `vidiq_balance` (free) — if under 10 credits, skip step 1b and say so in the report. 1b: `vidiq_user_videos` (channelId `UCbAmQO4sOpHb4g4GqR812lA`, limit 50, 5 credits) and `vidiq_user_channels` (free, subscribers). Save the snapshot as `stats/<YYYY-MM-DD>.json` and compare with the previous snapshot.
2. **Report** → `reports/latest` (set, with if_version): weekOf, updatedAt, headline {videos (published this week), views (channel total), viewsDelta (vs last snapshot), subs, subsDelta, likes (this week's videos)}, videos [{title, date, views, likes, comments}] for this week's videos plus the top 3 older ones, wins [], fails [] (include missed days from used.json.published), in plain Libyan Arabic.
3. **Plan** → same doc: focus [2–4 concrete goals for next week, e.g. title style to use more, riddle type to drop], plan [{day, what}].
4. **Lessons**: write proven lessons (data-backed, not guesses) to LEARNINGS.md with the evidence; credit the employee and add the lesson to their `skills` per OFFICE.md XP rules. Update every employee's `thinking` with one honest line on what to change.
5. **Dev lab — مهند**: search GitHub (WebSearch / WebFetch of api.github.com search, free) for popular, maintained, open-licence Claude/agent skills that would help this channel (titles/hooks, Shorts scripting, trend research, thumbnails, analytics). Read each candidate's SKILL.md before listing it; skip anything that needs paid keys or runs untrusted code. Write up to 5 to `devlab/latest` with status "proposed". Never install a skill without the owner's explicit OK.
6. **Levels**: apply the week's XP (OFFICE.md), add level-up log lines.
7. Commit + push stats/LEARNINGS.md; end with one short message to the owner with the headline numbers and "افتح المكتب واضغط على سالمة للتفاصيل".

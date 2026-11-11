# Posting schedule (Africa/Tripoli). The Sunday meeting owns this file.

| Time | Format |
|---|---|
| 16:00 | trap question (`riddle`, first unused `"type":"trap"` in bank.json) — experiment 2026-11-12 → the Sunday meeting; before that this slot was the daily tip |
| 19:00 | quiz on odd-numbered days of the month, odd (لقى المختلف) on even days |

**2026-11-11 — owner: "improve and publish without asking, I want a video past 10k".** The 16:00 tip is swapped for a trap question because trap questions are the only type that brought comments (6–11 each in October vs 0–1 on every November video). Tips stay in tips.json; the Sunday meeting compares trap vs tip at 16:00 and decides.

**2026-11-08 — owner approved: 2 posts a day, 13:00 riddle slot dropped** (see LEARNINGS.md). Riddles stay in the bank; one can replace a tip/quiz only after a Sunday meeting decides it.

## Why these times
- Metricool best-time data for this YouTube account (checked 2026-11-04): weekday peak 16:00 ≈12k, 13:00 ≈9.5k, 19:00 ≈7.2k, 23:00 only ≈2.8k.
- The channel's own posts agree so far: 23:00 «الديك» got 8 views in ~22 h, while the 18:50 post the same day got 394. Older posts that did well went out 14:00–21:00.
- Re-check `getBestTimeToPostByNetwork` (youtube, next 7 days) every Sunday. Change a slot only when Metricool's peak moves or a slot underperforms the channel median two weeks in a row; change one thing at a time and log why in LEARNINGS.md.
- Format check every Sunday: compare views per format; a format that loses to the others two weeks running gets replaced by the dev lab's proposal.

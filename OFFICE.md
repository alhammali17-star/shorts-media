# The office page (live status for the owner)

Artifact: https://claude.ai/artifact/N5Bhh6ZZcpfTx7ZsP3FzZe — update it ONLY through the `ArtifactData` tool (load with ToolSearch "select:ArtifactData"). Never republish the page itself.

## Documents
- `staff/<id>` — one per employee: name, role, dept (ceo|dev|trend|write|prod), order, xp, status (idle|working|done|error), task (one short line, Libyan Arabic), thinking (2–3 sentences: where this employee's reasoning is now, what it learned), skills (list of short lessons it has proven), history (last 20 items {date, text, xp}), updatedAt (ISO).
  Ids: ceo=سالمة, muhannad=مهند (dev), rehab=رحاب (trend), tareq=طارق (trend filter), nouri=نوري (writer), huda=هدى (checker), khaled=خالد (editor), asma=أسماء (publisher).
- `log/recent` — {items:[{at, who, text, kind: ok|error|info|level}]}; keep the newest 60, drop older.
- `reports/latest` — weekly report + plan (see WEEKLY.md for fields).
- `devlab/latest` — {updatedAt, items:[{name, url, stars, why, status: proposed|installed|rejected}]}.

## How every role reports
Read the doc first (`get`), then write with `if_version`. At the start of a role: status "working" + task. At the end: status "done" (or "error" with the reason in task), add XP, push a history item, append to log/recent. Batch the end-of-run writes in one `ArtifactData` batch.

## Levels (same scale the page shows)
XP to reach level: L1 0 · L2 100 · L3 300 · L4 600 · L5 1000 · L6 1500 · L7 2100 · L8 2800 · L9 3600 · L10 4500.
Names: متدرّب، مبتدئ، مساعد، موظف، محترف، خبير، متمكّن، قائد، أستاذ، أسطورة.

XP rules (earned only for real outcomes, never for just running):
- Daily role completed without error: +15 (publisher only when the post is scheduled successfully).
- Checker catches a real problem (wrong answer, repeat, non-Libyan word) before render: +20 to huda.
- Weekly: video of the week beat the channel median views → +40 to the writer, trend researcher and publisher who produced it.
- A lesson proven by data (logged in LEARNINGS.md by the CEO) → +50 to the employee it came from, and the lesson is added to that employee's `skills`.
- An error that reached the owner (broken video posted, repeat posted, missed day) → −30 to the responsible employee (XP never below the start of its current level).
- Dev lab: a proposed skill the owner approves and installs → +60 to muhannad.
On a level-up, add a `kind:"level"` log line like "طلع للمستوى 3 (مساعد)".

Growth that is real, not cosmetic: each employee's `skills` and `thinking` are read at the start of its next run and must change how it works (the trend filter uses its learned rules, the writer avoids its logged weak riddle types, etc.). LEARNINGS.md is the source of truth.

---
name: quarterly-check-in
description: Run a privacy-respecting quarterly review of an annual plan, recording evidence and an append-only history of approved goal changes and progress.
argument-hint: "2027 Q1 | 2027 Q2 | 2027 Q3 | 2027 Q4"
disable-model-invocation: true
---

# Quarterly check-in — Goal Evolution Tracker

Interpret planning year + quarter from the user's message (e.g. `/quarterly-check-in 2027 Q1`). Do not depend on client-specific argument placeholders. This is the **planning year**, usually from `annual-reviews/<PLANNING_YEAR-1>/goals.md`. If the actual plan is in another review year, use that only when the user clarifies and approves.

Read [review protocol](references/quarterly-protocol.md) before inspecting or writing journal files. All resource paths are relative to this skill folder. Use this skill on its own or alongside `annual-review`; do not require the other skill to be installed for the quarterly protocol.

## Steps

1. Confirm an approved private workspace and permission before *any* writes. Locate the existing goal snapshot, check-in, history and evidence ledger **inside that workspace**. If no review exists, invite the user to start one; do not invent goals.
2. Ask only 1–2 questions per turn: What was attempted? What actually happened? What evidence is available? What changed? What would the user like to continue/change/stop?
3. Track each goal by stable `G-<PLANNING_YEAR>-NNN` ID. Distinguish reported activity from verified outcomes. Never calculate progress percentages without comparable baseline + actual.
4. Read an existing quarterly file before editing it. Use [quarterly template](templates/quarterly-check-in.md) for a missing file, only after save consent. Preserve edits and earlier observations.
5. After user approval to save a progress report, append a per-goal `check-in` event to `goal-history.md` with `GH-<PLANNING_YEAR>-NNN`, referencing the exact check-in file and any user-approved `EV-*` IDs. **Do not** change `goals.md` merely because the agent recommends a modification.
6. For a proposed change/pause/completion/retirement, show before → after, request **explicit approval**, append an `adjusted`/`paused`/`completed`/`retired` event, and update only the relevant current goal snapshot. Verify after editing; report partial failures.
7. Summarize what happened, what is only hypothesized, decisions recorded, exact files changed, and the next check-in. If saving isn't approved, complete in chat only.

No external accounts, histories, or company files may be read without explicit scope consent. No automatic commits or cloud syncing. Personal content is sensitive: minimize unnecessary copying and avoid condescending judgments.

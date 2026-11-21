# Goal Evolution Tracker — stable IDs and append-only history

## Data model

- `goals.md` is the **current approved snapshot**, not a complete history.
- `goal-history.md` is the **chronological decision/event log**. Never overwrite or delete previous events during normal updates. Preserve manual notes.
- For new user-approved goals, assign stable IDs `G-<PLANNING_YEAR>-NNN`, e.g. `G-2027-001`. Reuse the ID through revisions, pauses and retirement; do not recycle.
- Every approved create/refine/pause/resume/change/retire/complete decision creates one event `GH-<PLANNING_YEAR>-NNN`, incrementing from existing records. Every *completed* quarterly check-in may also create a `check-in` event for each discussed goal with progress/evidence references, even if no goal changes; do not create events for questions with no user-provided progress.

## Event contract (`goal-history.md`)

Each `### GH-YYYY-NNN — ...` block contains:

- `Goal ID:` `G-YYYY-NNN`
- `Event type:` `created | refined | check-in | adjusted | paused | resumed | completed | retired | corrected`
- `Recorded at:` known date/period or `TBD`; don't claim current time unless available
- `Decision / observation:` accurate user-confirmed fact or choice
- `Previous state:` user-approved prior wording/status, or `none`
- `New state:` approved wording/status or `unchanged`
- `Reason / trade-off:` user-stated reason or `not provided`
- `Evidence refs:` `EV-*`, local file+heading, or `none provided`
- `Source check-in:` `check-ins/2027-Q1.md` or `none`
- `User approval:` `explicit in conversation` for changes; never infer from silence

For a progress-only `check-in` event, `User approval` means permission to **save the progress report**, not approval to revise the goal. Mark the absence of approval honestly.

## Write transaction (consistency)

1. Read the latest `goals.md`, `goal-history.md`, and relevant check-in before proposing edits. Check existing IDs for collisions and current status.
2. Propose precise changes (old value → new value), implications for processes/cadence, and any `stop/do less` trade-off. Ask for explicit approval.
3. For a new goal, append a `created` event and add the selected goal to `goals.md` with the same ID. For an approved revision, append an event with old/new state and update only that goal's current snapshot. For a check-in, append an event and leave `goals.md` unchanged unless a separate change was approved.
4. Reread both files; verify every new event references an existing, matching goal ID and that current snapshot reflects the latest **approved state-changing** event. Report file paths changed. If only one write succeeds, disclose the inconsistency and do not claim completion.
5. For a disputed event, append a `corrected` event referencing the earlier event ID; never rewrite past events, unless the user explicitly asks to delete private information.

## Legacy plans

If prior goals have no IDs or no history file, do **not** invent past decisions or timestamps. Offer a one-time **user-approved** migration that adds IDs to current goals and starts history with `created` events marked `Imported from pre-history snapshot — original creation date unknown` (or `corrected` as relevant). Do not assert these were recorded at the time of original approval.

## Read-only command

`history PLANNING_YEAR` reads the corresponding review directory and shows per-goal chronological events, latest approved state, evidence gaps and outstanding questions. No writes unless separately requested.

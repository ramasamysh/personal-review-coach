# Quarterly review protocol (standalone skill resource)

## Workspace and data layout

- Use only a private folder approved by the user. Planning year `2027` normally means review source `annual-reviews/2026/`.
- Read `goals.md`, `goal-history.md`, `evidence.md` (when present) and `check-ins/2027-QN.md` for the requested quarter. Do not read unrelated folders, browser history, emails, calendars, git logs, or cloud files by default.
- Output only after save consent: `annual-reviews/<REVIEW_YEAR>/check-ins/<PLANNING_YEAR>-Q<N>.md`.
- Use the local [template](../templates/quarterly-check-in.md) if no check-in exists. If older reviews lack tracking files, ask to initialize them; do not fabricate historical data.

## Stable IDs and status

- Goals use `G-<PLANNING_YEAR>-NNN`. Reuse IDs unchanged. Legacy unnumbered goals require user-approved ID migration before new events; import entries must state original creation date unknown.
- Events use `GH-<PLANNING_YEAR>-NNN`, append-only; scan existing records to avoid collisions. Event types are `created`, `refined`, `check-in`, `adjusted`, `paused`, `resumed`, `completed`, `retired`, `corrected`.
- Evidence records use `EV-<REVIEW_YEAR>-NNN` if available. `self-reported` is a legitimate description of user testimony, not proof of inaccuracy. `documented` only when the user actually supplied supporting records; a stored file reference is not independent truth verification.

## Event block fields (required)

`Goal ID`, `Event type`, `Recorded at` (known or TBD), `Decision / observation`, `Previous state`, `New state`, `Reason / trade-off`, `Evidence refs`, `Source check-in`, `User approval`.

- For `check-in`, `User approval` means permission to persist progress, *not* permission to change the goal. Leave snapshot unchanged.
- For `adjusted`, `paused`, `resumed`, `completed`, or `retired`, require explicit approval of the proposed old → new snapshot. Append the event **and** update the matching goal in `goals.md`.
- If either update fails, report partially saved state; reread and reconcile before claiming success.
- Preserve historical events; corrections append a `corrected` event. Comply with explicit user deletion requests, which override preservation defaults.

## Questions / reasoning

Compare planned processes and observed activity **per goal**. Identify obstacles and scope changes without telling the user they failed. Only use numeric deltas when baseline, actual, unit and time period are compatible. Unknown ≠ missed. End with explicit decisions and small next steps.

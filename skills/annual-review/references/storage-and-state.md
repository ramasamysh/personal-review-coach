# Storage and state — safe journal I/O

## Boundaries and consent

- The user must choose an accessible **private** workspace and explicitly agree to saving before any write. If absent, operate in chat without claiming files were created. Do not write to a workplace repo or company-owned machine without clear suitability and consent.
- Normal path: `<approved-workspace>/annual-reviews/<REVIEW_YEAR>/`; the year reviewed is **not** the planning year. For planning year `2027`, read/write the goal plan under review year `2026` unless the user deliberately used another year.
- Treat `annual-reviews/` as private; avoid cloud sync and Git without explicit separate authorization. Never fetch external evidence or files beyond the approved workspace by default.
- Read target files before editing; preserve handwritten notes and additions. Don't rewrite a file just to normalize formatting. Never fill in missing personal data using assumptions. Report failed writes and prevent misleading index/status updates.

## Initial template copies (only after permission)

From this skill's `templates/` directory into `annual-reviews/<REVIEW_YEAR>/`:

| Source template | Destination | Purpose |
| --- | --- | --- |
| `index.md` | `index.md` | exercise state and consent |
| `reflection.md` | `reflection.md` | observations and interpretations |
| `wishes.md` | `wishes.md` | original user wish list |
| `goals.md` | `goals.md` | current goal snapshot and IDs |
| `evidence.md` | `evidence.md` | claims, sources and uncertainty |
| `goal-history.md` | `goal-history.md` | append-only decisions and check-ins |
| `synthesis.md` | `synthesis.md` | review synthesis |

Replace only verified placeholders `{{REVIEW_YEAR}}`, `{{PLANNING_YEAR}}`, `{{CATEGORIES}}`; otherwise leave TBD. Do not modify files that already exist. Create `comparisons/` and `check-ins/` only when first needed and save approved.

## Review metadata

- `index.md`: year, categories, exercise status (`not-started`, `in-progress`, `complete`), next step and updated date if known. Missing fields mean unknown, not complete.
- IDs: evidence `EV-<REVIEW_YEAR>-001...`; goals `G-<PLANNING_YEAR>-001...`; events `GH-<PLANNING_YEAR>-001...`. When creating the next ID, scan all existing records; never recycle an ID. Keep text-only IDs stable.
- In a legacy review without `evidence.md` or `goal-history.md`, offer to create **missing** templates after permission; never silently backfill history or represent it as contemporaneously logged.
- Cite journal sources by *relative file and heading*, e.g. `annual-reviews/2025/goals.md#Selected priorities` in your prose. References to user-authored Markdown are navigational, not independent verification.
- If the user withdraws/changes an earlier statement, record correction only with consent. Do not erase history unless the user explicitly requests deletion and understands its effect; deletion requests take precedence over append-only bookkeeping.
- If edits span goal snapshot and event history, write the event only **after** the user approves the exact change; update both, then reread and check consistency. If either write fails, report partial state and ask whether to repair; do not claim success.

## Read-only commands

`status`, `history`, and `compare` never alter the journal unless the user separately asks to save a report or approve a change. Reading only the approved two review years is sufficient for `compare`.

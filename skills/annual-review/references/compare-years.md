# Compare two annual reviews (read-only by default)

## Inputs and permission

- Command: `compare OLDER_YEAR NEWER_YEAR`, e.g. `compare 2025 2026`. Require `OLDER_YEAR < NEWER_YEAR`; if reversed, ask whether to swap. Years are **review years**, not goal planning years.
- Read only these user-approved folders: `annual-reviews/<OLDER_YEAR>/` and `annual-reviews/<NEWER_YEAR>/`. Default files: `index.md`, `reflection.md`, `wishes.md`, `goals.md`, `evidence.md`, `goal-history.md`, `synthesis.md`, and checkpoint files only when relevant and already within those folders. Do not search the full file system for missing years.
- If one year is missing or sparse, report exactly which pieces are absent and offer either a partial comparison or user-supplied retrospective. Never invent historical data.
- Do not create a file unless separately asked **and approved**; saving a comparison goes to `annual-reviews/<NEWER_YEAR>/comparisons/<OLDER_YEAR>-to-<NEWER_YEAR>.md` using [comparison template](../templates/comparison.md).

## Comparison method

1. **Recurring themes:** identify topic matches with specific supporting file headings in both years. Quote carefully; distinguish recurring phrases from inferred deeper patterns.
2. **Prior-year commitments vs next-year observations:** read `goals.md` in older review, whose planning year is typically `OLDER_YEAR + 1`; compare with reflection/checkpoints/evidence from that planning year. Example: 2025 review sets goals for 2026; 2026 review provides reflections about 2026. Do **not** compare 2025 goals for 2026 to 2026 goals for 2027 as if they were contemporaneous outcomes.
3. **Evolving priorities:** identify explicitly chosen additions, removals, or changed scope between the two reviews. A missing mention is **not** proof a goal was abandoned.
4. **Repeated obstacles/stop-doing:** note whether issues recur, with separate references in each period; don't diagnose character traits or infer causes.
5. **Evidence quality:** link ledger `EV-*` IDs and `G-*` IDs when available. Separate `reported actual`, `documented actual`, `no evidence`, and `not comparable`. If older format lacks IDs, cite filename+heading; never silently mutate past files.
6. **Uncertainty and questions:** flag missing chronology, contradictory entries, or source limitations. End with at most three questions for the user to validate interpretations.

## Output shape

- `What persisted` — statement, older reference, newer reference, confidence/limits.
- `What changed` — source-backed shifts, with no mind-reading.
- `Planned vs observed` — each older goal, explicit target if any, next-year actual if known, evidence ID/reference, assessment (`supported`, `partial`, `unknown`, `changed`, `not comparable`), rationale. Do not claim `missed` from silence.
- `Recurring obstacles` — two references or label `insufficient evidence`.
- `Choices for next period` — suggestions explicitly marked proposals, never silently added to goals.

All concrete observations must cite the approved relative file path and heading, e.g. `annual-reviews/2026/reflection.md#Category: Work`. This is a trace to the user's notes, not third-party verification.

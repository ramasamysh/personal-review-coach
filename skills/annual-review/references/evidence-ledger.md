# Evidence Ledger — traceable, proportionate reflection

Purpose: help users distinguish *what happened* from *what it means*, not to demand proof of private experiences. Treat personal self-reports respectfully and identify them as such, not as “unverified facts.” Do not browse, inspect, or paste external personal files without explicit scoping and consent.

## When to use

- During reflection, propose one ledger entry for a major factual claim **only if the user wants it recorded** (e.g. "I shipped a feature" or "I practiced weekly"). Never require evidence for an emotional experience.
- When refining a goal, connect its outcome/indicator to evidence IDs, a missing baseline, and a future evidence collection method (opt-in).
- For `evidence YEAR`, read `evidence.md`, identify unsupported extrapolations, contradictions, and evidence gaps **without overwriting entries**.
- For a planned-vs-actual comparison, use user-approved goal targets and subsequent observations; distinguish not observed vs not achieved.

## Entry contract

Append records under `## Evidence records` in `evidence.md` using a monotonically increasing ID, e.g. `### EV-2026-001 — Shipped project milestone`.

Required fields:

| Field | Values / rules |
| --- | --- |
| `Claim (user-stated)` | Exact or faithful short paraphrase; never embellish |
| `Category` | User-chosen category, or `unspecified` |
| `When` | Date/period user knows, else `TBD` |
| `Source type` | `self-report`, `user-shared-document`, `manual-log`, `other-user-authorized-source`, or `none` |
| `Source reference` | Local filename/heading, user-approved external reference, or `none provided`; do not copy sensitive contents by default |
| `Evidence status` | `self-reported`, `documented`, `incomplete`, `contested`, or `withdrawn` |
| `Confidence / limits` | Brief reason or uncertainty; not a fabricated numerical score |
| `Related goal ID` | Stable `G-YYYY-NNN` if applicable, otherwise `none` |

`documented` means the user provided an actual relevant record that supports the narrow claim, **not** that the assistant independently validated its truth. `self-reported` does not mean false. `incomplete` means insufficient evidence for a narrower inference, not that a personal experience is invalid.

## Discipline

1. Ask permission to write the claim. Never create an entry from the assistant's example or hypothesis.
2. Keep sources optional; use `none provided` rather than manufacturing a citation, date, baseline, numerical estimate, or achieved percentage.
3. If an entry materially changes, add a `Correction / update` note with the date/period if known and link the earlier ID. Preserve the original record unless user asks to remove it.
4. A claim such as “260 people installed the plugin” supports an adoption/installation count *as reported*; it does **not** establish weekly active usage, productivity improvements, or measurable business benefit.
5. Distinguish planned goal indicators in `goals.md`, self-reported actuals, documented actuals, and unknowns. A difference can be computed only when both numbers and comparable units/dates are known.

## Output example (fictional)

`EV-2026-001` — Claim: "Published three essays"; Source type: `self-report`; Source reference: `none provided`; Evidence status: `self-reported`; Confidence / limits: "Count stated by user; publication links not supplied".

Don't save fabricated examples into real journals.

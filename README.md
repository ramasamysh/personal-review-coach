# Personal Review Coach — Claude Code + VS Code Copilot

**v0.3.0** · Agent Skills + Claude-format local plugin. An **independent implementation** inspired by the publicly described Reflect / 100 Wishes / Set Goals / Refine Goals exercises in [Product Talk](https://www.producttalk.org/personal-annual-review/). It is not affiliated with Teresa Torres, and does not contain the subscriber-only plugin.

## What's new in v0.3.0

1. **Evidence Ledger** (`/annual-review evidence 2026`): Optional `EV-2026-001` records with explicit source types and status. Distinguishes personal self-reports from documented support; never invents metrics, citations, or sources.
2. **Longitudinal Intelligence** (`/annual-review compare 2025 2026`): Read-only-by-default comparisons, with file+heading traces, prior plans vs subsequent observations, and `unknown` instead of fabricated missed-goal assessments. Optional approved comparison reports.
3. **Goal Evolution Tracker** (`/annual-review history 2027`): Stable `G-2027-001` goal IDs, append-only `GH-2027-001` decisions, current goal snapshot, and quarterly check-ins that log progress without silently changing the plan.

No external server, MCP dependency, TypeScript or database is required. **These are instruction-based workflows executed by an AI agent**, not deterministic software with a backend. Actual agent behavior varies and requires end-to-end evaluation.

## Commands

| Full plugin | Standalone Copilot skill | Behavior |
| --- | --- | --- |
| `/personal-review-coach:annual-review start 2026` | `/annual-review start 2026` | Create review after consent |
| `/personal-review-coach:annual-review reflect 2026` | `/annual-review reflect 2026` | Reflection and optional ledger entries |
| `/personal-review-coach:annual-review evidence 2026` | `/annual-review evidence 2026` | Review evidence claims and gaps |
| `/personal-review-coach:annual-review compare 2025 2026` | `/annual-review compare 2025 2026` | Compare two review years (no write by default) |
| `/personal-review-coach:annual-review goals 2026` | `/annual-review goals 2026` | Choose 2027 priorities with IDs |
| `/personal-review-coach:annual-review refine 2026` | `/annual-review refine 2026` | Refine approved goals, append history |
| `/personal-review-coach:annual-review history 2027` | `/annual-review history 2027` | Read chronological goal decisions |
| `/personal-review-coach:annual-review status 2026` | `/annual-review status 2026` | Report progress without edits |
| `/personal-review-coach:annual-review resume 2026` | `/annual-review resume 2026` | Continue partial work |
| `/personal-review-coach:annual-review wishes 2026` | `/annual-review wishes 2026` | Explore wishes in batches |
| `/personal-review-coach:annual-review synthesize 2026` | `/annual-review synthesize 2026` | Grounded synthesis |
| `/personal-review-coach:quarterly-check-in 2027 Q1` | `/quarterly-check-in 2027 Q1` | Quarterly progress / approved goal changes |

## Install in GitHub Copilot in VS Code (simple)

1. Extract **the companion Copilot workspace ZIP** into a **private** folder. It has `.github/skills/annual-review/` and `.github/skills/quarterly-check-in/`, including templates and references.
2. Open that folder in VS Code, start a new Copilot **agent** chat, and check skill discovery under **Chat: Open Customizations → Skills** if available.
3. Type `/annual-review start 2026`. If the slash command does not appear in your version, ask Copilot to **use the annual-review skill** to start a review for 2026.
4. Treat each proposed file change as subject to your editor's approval and privacy rules.

## Install as Claude Code local plugin

Extract this ZIP first and point at the **uncompressed directory** (not at the ZIP):

```bash
mkdir -p ~/personal-review-workspace
cd ~/personal-review-workspace
claude --plugin-dir /absolute/path/to/personal-review-coach
```

Then run `/personal-review-coach:annual-review start 2026`. Alternatively copy complete `skills/annual-review/` and `skills/quarterly-check-in/` directories to `~/.claude/skills/` for standalone installation.

## Review output, once approved

```text
<approved-private-workspace>/
└── annual-reviews/
    ├── 2025/                           # optional older review
    └── 2026/
        ├── index.md
        ├── reflection.md
        ├── wishes.md
        ├── goals.md                      # current approved snapshot (G-* IDs)
        ├── evidence.md                   # EV-* entries, source status
        ├── goal-history.md               # append-only GH-* events
        ├── synthesis.md
        ├── comparisons/
        │   └── 2025-to-2026.md           # only after explicit save consent
        └── check-ins/
            └── 2027-Q1.md
```

**Privacy:** This plugin ships only prompts/templates, not personal data. Do not store reviews in a company repository or publicly tracked folder. Local Markdown files do **not** mean local model processing. No automatic email, git, cloud sync, calendar or document retrieval is authorized. A source record is a user-approved pointer and not independent verification. User-directed deletion overrides the normal append-only pattern.

## Legacy v0.2 journals

Existing Markdown is preserved. A missing `evidence.md` or `goal-history.md` can be initialized **after user consent**. Existing goals lacking `G-*` IDs can be migrated one at a time with permission; use "imported legacy snapshot — original creation date unknown" rather than inventing an event timeline. `compare` works read-only even without ID migration, citing original file headings.

## Quality gates

- Run `python3 tests/validate_package.py` inside the extracted full package. It checks required files, manifest, front matter, relative resource links, and compatibility conventions.
- Follow [manual eval scenarios](tests/scenarios.md) on **both** Claude Code and Copilot. A static validator does not prove skill discovery or correct user-facing behavior.
- See [CHANGELOG](CHANGELOG.md).

## Documentation

- [Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Agent plugins in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-plugins)
- [Claude Code skills](https://code.claude.com/docs/en/skills)

# Progress

Last updated: 2026-10-15

## Status
- [x] Step 1: company list approved (64 public / 36 private+defunct, 12 cautionary, build at repo root)
- [ ] Step 2: research batches, one archetype per batch (12 batches)
- [ ] Step 4: independent verification pass
- [ ] Step 5: cards.csv, database.md, index.html, patterns.md
- [ ] Step 6: README.md

## Blockers
- 2026-10-15: the environment network policy blocked the source sites (sec.gov, investor-relations sites, press), so WebFetch could not open primary documents. The user switched Network access to Full, but the original container kept the old policy, so the work moves to a new session.

## Resume here (new session)
1. Read `SPEC.md` (full brief and decisions) and `companies.md` (approved list).
2. Check network first: WebFetch on an SEC EDGAR document must succeed before any research starts.
3. Start Step 2: one subagent per archetype, run in parallel. Each subagent writes `data/cards/<slug>.json` for its companies and runs `python3 scripts/validate_cards.py <slugs>`.
4. After each batch, update the Batches table below and commit/push to `claude/business-models-database-7k1o30`.

## Batches
| # | Archetype | Cards done | Gaps |
|---|---|---|---|

## Swaps
(none yet)

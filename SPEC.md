# Business Models Database: spec

This is the original brief, kept in the repo so that any session can resume the work.

## Goal
Build 100 company cards. Each card explains how the company makes money, its key figures, and its weak points. Accuracy matters more than polish: every number must be traceable to a source. The approved list is in `companies.md`.

## Decisions already made by the user
- Keep the 64 public / 36 private-or-defunct split.
- Keep all 12 cautionary companies.
- Build at the repository root.
- Figures: use the latest annual filing (mostly FY2025), plus newer quarters where they matter. Defunct companies use their last available period.

## Card schema (`data/cards/<slug>.json`)
```json
{
  "name": "", "slug": "", "archetype": "", "secondary_archetype": null,
  "status": "public|private|defunct", "cautionary": false,
  "hq": "", "founded": "",
  "one_liner": "what they sell, to whom, in one sentence",
  "customer": "who pays (vs. who uses, if different)",
  "revenue_streams": [{"stream": "", "share_pct": null, "pricing_mechanic": ""}],
  "unit_economics": "how one sale/customer makes money; take-rate, margins, CAC/LTV if known",
  "key_figures": [{"metric": "", "value": "", "period": "", "source_url": "", "source_type": "filing|company|press|research|estimate"}],
  "moat": "",
  "pivots": [{"year": "", "from": "", "to": "", "why": ""}],
  "weak_points": ["specific, evidence-based risks, not generic ones"],
  "lesson": "one transferable insight for a founder",
  "last_verified": "YYYY-MM-DD"
}
```
Archetype slugs are the values `scripts/validate_cards.py` accepts: marketplace, saas_subscription, usage_based_api, advertising, payments_take_rate, freemium_plg, hardware_services, licensing_ip, d2c_ecommerce, b2b_services, infrastructure_energy, fintech_lending_float.

## Sourcing rules (non-negotiable)
- Public companies: use the latest annual report / 10-K / 20-F / investor presentation first. Fetch the primary document; do not rely on aggregator summaries.
- Private companies: use company statements, credible press (FT, Bloomberg, Reuters, The Information, TechCrunch), or research firms. Mark anything unconfirmed as "estimate".
- Every key_figure needs a source_url and a period. If there is no source, leave the number out.
- Never invent figures. If share_pct is unknown, leave it null.
- Paraphrase; never copy source text.

## Workflow
1. Propose the list and wait for approval. (DONE)
2. Research in batches of about 10. Batches may run in parallel with subagents, one archetype per subagent. After each batch, write the JSON files and print a one-line status per company plus any gaps.
3. Save progress to `progress.md` after every batch so the run can resume if interrupted.
4. After all 100 cards: run a verification pass with a separate agent that did not write the cards. It re-opens every source_url, confirms each figure, and logs mismatches to `verification_log.md`. Fix or remove bad figures.
5. Build outputs:
   - `cards.csv`: flattened, one row per company.
   - `database.md`: all cards grouped by archetype.
   - `index.html`: a single self-contained page with search, filters (archetype, public/private, region, cautionary), expandable cards, and a "compare 2 companies" view. No external dependencies except a CDN font.
   - `patterns.md`: cross-company synthesis covering which archetypes have the best margins, common weak points per archetype, and the 10 most transferable lessons.
6. Write `README.md` covering methodology, source hierarchy, data date, and known gaps.

## Quality bar
- Weak points must be specific and evidenced ("70% of revenue from 3 customers per FY2025 10-K"), never generic ("competition is intense").
- Lessons must be actionable for an early-stage founder.
- Use consistent units: USD, noting the original currency if converted. Always state the fiscal period.
- If a company lacks enough reliable data for a solid card, swap it for another in the same archetype and note the swap in `progress.md`.

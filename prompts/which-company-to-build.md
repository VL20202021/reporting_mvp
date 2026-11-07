# Which Company to Build — Recommendation

Profile assumed: business/finance background, solo, bootstrapped, open to a staged exit
(mid-size strategic or serial acquirer first, Fortune 1000 / Mag 7 later). Research date: Nov 2026.

## The hard truth about Mag 7 buyers

Recent NVIDIA and Meta deals are almost all **AI research/infrastructure teams**: Groq (~$20B
license + hire, Dec 2025), Run:ai (~$700M), Kumo AI (2026), Manus (>$2B), PlayAI, WaveForms,
Limitless, ARI robotics. These are deep-tech teams, often venture-backed with $10M+.
A solo, bootstrapped, business-led founder will not realistically be a direct NVIDIA/Meta target.

The realistic path: **sell to a serial acquirer that consolidates a category** (Flexera, IBM,
DoiT, Collibra, CUBE, Banyan, Antares Vision). Those buyers are often themselves bought by,
or are, Fortune 1000 companies.

## What Antares Vision teaches

Antares Vision built an end-to-end traceability group by buying small specialists:
FT System (2019), Tradeticity (82.83%, 2020), Applied Vision (2020), Convel (2020),
Adents assets (2020), rfxcel (2021, with up to $30M earn-out), Pen-Tec and Tecnel (2021),
T2 Software, Smart Point (via rfxcel), plus stakes in Orobix and Isinnova.
(I verified ~11–13; the "18" figure includes smaller entities/stakes not confirmed here.)

The pattern: **small, specialist software tied to a mandatory regulation** (e.g., US DSCSA for
pharma serialization) that fills a gap in the buyer's stack. Buyers pay with earn-outs tied
to revenue, so **real paying customers matter more than technology**.

## Ranked options

| # | Company | Fit for you | Bootstrappable | Proven buyers | Main risk |
|---|---|---|---|---|---|
| **1** | **AI spend & unit-economics for finance teams** ("FinOps for AI, built for the CFO") | High — finance is the core skill | Yes — reads billing APIs, no heavy infra | IBM (Apptio $4.3–4.6B, Kubecost), Flexera (Spot, ProsperOps, Chaos Genius, Jan 2026), DoiT (Select, PerfectScale), Datadog, ServiceNow ecosystem | Crowded with engineering-first tools; need a sharp finance wedge |
| 2 | AI-governance / AI Act + DORA compliance for financial services | High | Mostly (services-led start) | CUBE (Kodex AI), Collibra (trail ML), LatticeFlow (AI Sonar), Proofpoint (Acuvity) | Regulatory timelines can slip; enterprise sales cycles |
| 3 | Regulation-driven traceability (EUDR, Digital Product Passport) — the Antares play | Medium (needs supply-chain domain) | Yes | Banyan (tec4U, Jun 2026), Antares-type groups, osapiens | EUDR already revised/delayed; regulation risk |

## Recommendation: #1 — AI Cost & Margin Intelligence for SaaS CFOs

**Problem:** Companies adding AI features can't answer "what does AI cost us per customer,
per feature, per plan — and is it destroying our gross margin?" Engineering tools show tokens
and GPU hours; finance needs **cost per customer, gross margin by plan, budget vs. actual,
chargeback, and pricing guidance**. The FinOps Foundation reports AI spend management going
from ~31% of FinOps teams two years ago to an expected ~98% (per Virtasant's State of FinOps
2026 summary).

**Wedge (narrow on purpose):** AI-native B2B SaaS companies with $5–100M ARR. Connect
OpenAI/Anthropic/Bedrock/Azure/GCP billing + Stripe + product usage → a monthly
**"AI gross margin report"** for the CFO and board.

**Why acquirers want it:** Flexera, IBM, and DoiT each made multiple FinOps acquisitions in
2024–2026 specifically to cover new cost categories (Kubernetes, Snowflake/Databricks, AI).
A finance-first AI-margin product with paying CFO customers fills the next gap.
Later Fortune 1000 / Mag 7 adjacency: ServiceNow, Datadog, Microsoft (Azure cost tooling),
NVIDIA's software stack (Run:ai lineage).

**Why you, solo:** It sells to CFOs (your language), can start as a done-for-you monthly
report (services revenue funds the product), and needs integrations, not research.

## 90-day validation plan

- **Weeks 1–2:** Interview 25 CFOs/finance leads at AI-heavy SaaS companies. Kill criterion:
  fewer than 8 say AI cost per customer is a top-3 problem.
- **Weeks 3–4:** Manually build the AI margin report for 3 companies from exported bills
  (spreadsheet + scripts). Charge something (even $500–1,500/month).
- **Month 2:** Automate the top 2 connectors (one LLM provider + Stripe). Get to 5 paying.
- **Month 3:** List in FinOps Foundation ecosystem / cloud marketplaces; publish a benchmark
  ("AI gross margin by SaaS category") to get on acquirers' radar. Target 10 paying, ~$10K MRR.

**Acquisition-readiness from day 1:** company owns all IP (contractor IP assignment),
clean cap table, SOC 2 roadmap, transferable customer contracts, tidy monthly financials.

## What to study (in this order)

1. **FinOps** — FinOps Foundation's FinOps Certified Practitioner; the FOCUS billing data spec.
2. **AI/cloud cost mechanics** — token pricing, caching, batch vs. real-time, GPU pricing models.
3. **SaaS metrics** — gross margin, NRR, CAC payback (e.g., SaaStr/ChartMogul/Bessemer reports).
4. **Light technical skills** — SQL + Python for data pipelines; enough to build connectors
   with AI coding tools.
5. **M&A from the sell side** — how earn-outs and acqui-hires work; read acquirer 10-Ks
   (IBM, Datadog, ServiceNow) and Flexera/DoiT press releases to see what they buy and why.

## Before committing, check

- Whether CloudZero, Vantage, Datadog, or LLM-observability tools (Langfuse, Helicone) already
  serve the **CFO** persona well in your target market.
- Whether you prefer EU or US customers; the EU makes option #2 more compelling.

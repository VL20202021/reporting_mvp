# Research notes: AI-native companies listing in India (and Indian AI cos listing abroad)

Scope agreed with user (2026-11-16):
- AI-native companies only (primary product is AI/ML).
- Window: Jan 2024 to now (2026-11-16), all stages (listed, SEBI-approved, DRHP filed, incl. confidential pre-filing).
- Mainboard NSE/BSE plus overseas listings/filings by Indian AI companies. SME excluded.
- Final report format: PDF (report.md rendered to report.pdf).

Network notes:
- Direct curl to sebi.gov.in and nseindia.com blocked by session proxy (CONNECT 403). Using web-fetch agent for fetching.

## Log
### Stage 1 — candidate discovery (web search)
- Fractal Analytics: IPO 9–11 Feb 2026, listed 16 Feb 2026 NSE/BSE, issue ~Rs 2,833.90 cr (fresh 1,023.5 + OFS 1,810.40), band Rs 857–900. [secondary: https://groww.in/blog/fractal-analytics-ipo-to-open-on-february-9 ; https://hdfcsky.com/news/fractal-analytics-lists-at-rs-876-on-nse-and-rs-900-on-bse] — TO VERIFY from RHP/exchange.
- C5i (ex-Course5 Intelligence): reported confidential DRHP, Rs 1,000–1,200 cr target. [secondary: https://maliktimes.in/c5i-ipo-enterprise-ai-firm-files-confidential-sebi-papers/] — TO VERIFY.
- Meganet Technologies Global: DRHP ~Rs 740 cr, AI/HPC servers (reported 2026-11-16). [secondary: https://www.marketscreener.com/news/indian-ai-infra-provider-meganet-files-for-78-6-million-ipo-ce785edfda89f025] — borderline AI-native (hardware); TO VERIFY.
- Search found no clear Indian-origin AI startup US IPO filing (first pass).
- Fractal DRHP dated 12 Aug 2025, reported Rs 4,900 cr (fresh 1,279.3 + OFS 3,620.7) [secondary: https://inc42.com/buzz/fractal-analytics-files-drhp-for-inr-4900-cr-ipo/ ; https://www.business-standard.com/markets/ipo/ai-firm-fractal-analytics-files-drhp-eyeing-to-raise-4-900-cr-via-ipo-125081300508_1.html]. Offer docs hosted at https://fractal.ai/docs/Investor-Relations/Offer-Documents/ (RHP dated 2 Feb 2026). Final size cut to ~Rs 2,834 cr vs DRHP.
- Bonbloc Technologies DRHP (Sep 2025, Rs 233 cr) — blockchain/IoT/data-science SaaS; NOT AI-native -> excluded. [https://www.business-standard.com/amp/markets/ipo/ai-company-bonbloc-technologies-files-ipo-papers-with-sebi-to-raise-233-cr-125092901057_1.html]
- Yotta Data Services: (a) Nasdaq de-SPAC via Nidar Infrastructure + Cartica Acquisition Corp; F-4 effective Nov 2025, Cartica EGM approved 4 Dec 2025, deal terminated 7 Jan 2026 [https://www.nasdaq.com/press-release/nidar-infrastructure-limited-yotta-data-services-and-cartica-acquisition-corp ; https://www.tipranks.com/news/company-announcements/cartica-acquisition-ends-merger-begins-liquidation-process ; SEC 424B3 https://www.sec.gov/Archives/edgar/data/2042648/000110465925107894/tm2426910-14_424b3.htm]. (b) Then reported planning Indian IPO up to $1.5bn, DRHP targeted Oct 2026 [https://inc42.com/buzz/ai-infra-provider-yotta-eyes-1-5-bn-ipo-by-march-2027-report/ ; https://www.dealstreetasia.com/stories/data-centre-operator-yotta-india-ipo-493935]. AI-native? GPU cloud ~50% revenue per CEO -> include as AI-infra.
- C5i: two filings — Course5 Intelligence DRHP Jan 2022 (Rs 600 cr; outside window, lapsed) and C5i confidential pre-filing mid-2026 (Rs 1,000–1,200 cr) [https://inc42.com/buzz/enterprise-ai-startup-c5i-files-confidential-ipo-papers-with-sebi/]. Confidential pre-filed DRHP is NOT public -> cannot fetch primary.
- Sarvam/Krutrim/Qure.ai/Uniphore/Netradyne: no IPO filing found in first pass.
- Direct curl to fractal.ai, sec.gov, bseindia.com, nsearchives also blocked (proxy 403); using web-fetch agent.

### Stage 2 — primary-document fetch: BLOCKED (2026-11-16)
- Added www.sebi.gov.in, www.nseindia.com, nsearchives.nseindia.com, www.bseindia.com, www.sec.gov, fractal.ai to the environment allowlist (user approved).
- curl download of https://fractal.ai/docs/Investor-Relations/Offer-Documents/Fractal-Prospectus.pdf was then DENIED by the session's auto-mode permission classifier (not by the network). Not retried by other shell means.
- web-fetch tool (WebFetch) cannot resolve any of these hosts (DNS ENOTFOUND), even after the allowlist change. Hosts that failed via WebFetch: fractal.ai, www.sec.gov, www.nasdaq.com, www.tipranks.com, www.marketscreener.com, srnnews.com, inc42.com, news.ventureintelligence.com, www.chittorgarh.com.
- Result: NO primary filing has been read yet. Every fact above is from search-result summaries and is UNVERIFIED.

### Additional candidates seen in search (unverified)
- Transline Technologies (AI surveillance/biometrics): SEBI observations 22 Jan 2026 per search summary; OFS-only. Unclear if AI-native.
- Multiplier AI: SME-board filing -> out of scope (SME excluded).
- 3AI: BSE SME (~Rs 25 cr) -> out of scope.
- Gupshup: founder signals 12–24-month listing window, considering redomicile to India; no filing. [https://inc42.com/features/gupshup-ai-rebuild-can-it-stay-ahead-of-the-platforms-it-runs-on/]
- Qure.ai, Sarvam AI, Neysa: described as prospective candidates only; no filing found.
- Jio Platforms DRHP (19 Jun 2026) mentions AI but is a telecom/digital conglomerate -> excluded (not AI-native). [https://www.medianama.com/2026/06/223-jio-drhp-ai-disclosures-ahead-ipo/]

### Stage 2 (resumed after user allowed curl, 2026-11-16) — PRIMARY DOCUMENTS READ
Fractal Analytics — VERIFIED from primary documents:
- Prospectus dated 11 Feb 2026 (https://fractal.ai/docs/Investor-Relations/Offer-Documents/Fractal-Prospectus.pdf), cover page and "Objects of the Offer" (p.203-204):
  - Offer price Rs 900 (price band Rs 857-900; Rs 85 discount for eligible employees).
  - Total offer 31,557,305 shares = Rs 28,339 mn (Rs 2,833.9 cr): fresh issue 11,441,751 shares = Rs 10,235 mn; OFS 20,115,554 shares = Rs 18,104 mn.
  - OFS sellers: Quinag Bidco Ltd (Apax) Rs 8,809 mn; TPG Fett Holdings Pte Ltd Rs 4,500 mn; GLM Family Trust Rs 4,500 mn; Satya Kumari Remala & Rao Venkateswara Remala Rs 295 mn.
  - Anchor bid 6 Feb 2026; bid/offer 9-11 Feb 2026. Listing on BSE and NSE; NSE designated exchange. BRLMs: Kotak, Axis, Morgan Stanley, Goldman Sachs.
  - Net proceeds Rs 9,593 mn (gross 10,235 less est. expenses 642): Fractal USA debt prepayment 2,649; laptops 571; new India offices 1,211; Fractal Alpha R&D + S&M 3,551; unidentified acquisitions + GCP 1,611.
  - Restated consolidated (Rs mn): Revenue from ops FY23 19,854; FY24 21,963; FY25 27,654; H1FY25 13,007; H1FY26 15,590. Profit/(loss): FY23 1,944; FY24 (547); FY25 2,206; H1FY25 729; H1FY26 709.
  - Self-description: "a globally recognized enterprise artificial intelligence ('AI') company (source: Everest Report)" (Business Overview).
- CORRECTION: news coverage said proceeds go to "AI/GenAI R&D". The prospectus shows only Rs 355.1 cr (37% of net proceeds) is for R&D + sales & marketing under Fractal Alpha; the largest single item is Fractal USA debt repayment (Rs 264.9 cr).
- CORRECTION: DRHP size Rs ~4,900 cr (news) vs final Rs 2,833.9 cr (prospectus) — offer was cut ~42%.
- Listing date 16 Feb 2026 on BSE and NSE: Annual Report FY2025-26 (https://fractal.ai/docs/Investor-Relations/Annual-Reports-and-Postal-Ballot-Notice/Fractal-Annual-Report-FY-2025-26.pdf), Directors' report / notes ("listed on ... NSE ... w.e.f. February 16, 2026"). BSE scrip 544700, NSE symbol FRACTAL (exchange filing letterheads).
- FY26 (audited, exchange filing dated 11 May 2026): revenue Rs 3,300 cr (+19%), net income Rs 287 cr (+30%). https://fractal.ai/docs/Investor-Relations/Stock-Exchange-Intimations/Fractal-PR-Audited-Consolidated-and-Standalone-Financial-Results-March-31-2026.pdf
- Q2 FY27 (press release 3 Nov 2026): revenue Rs 956.5 cr (+20% YoY), net income Rs 79.2 cr (+139%). https://fractal.ai/docs/Investor-Relations/Financial-Statements-and-Annual-Reports/2027/Q2/Fractal-Press-release-Q2-27.pdf
- Monitoring agency (CARE Ratings) report for qtr ended 31 Mar 2026: deviation Nil; Rs 43.3 cr used in Q4FY26 (Rs 2.6 cr Fractal USA; Rs 40.7 cr issue expenses); Rs 980.2 cr unutilised. https://fractal.ai/docs/Investor-Relations/Stock-Exchange-Intimations/Fractal-Monitoring-Agency-Report.pdf
- Listing-day price (Rs 876 NSE / Rs 900 BSE) — secondary only (https://hdfcsky.com/news/fractal-analytics-lists-at-rs-876-on-nse-and-rs-900-on-bse). NSE archive PDFs (press release PR_LIST_13022026) refused plain curl (empty reply / HTTP2 error) — NOT verified.

Blocked / not verifiable:
- SEC EDGAR (Nidar/Yotta 424B3): HTTP 403 "undeclared automated tool" — SEC requires a User-Agent with a contact email; I did not send the user's email without permission. Yotta facts remain secondary.
- NSE quote API: shell request denied by the permission classifier (browser-spoofing); not retried.
- SEBI draft-offer listing: first page readable; paginated AJAX query blocked by SEBI's WAF ("Unauthorized Activity"); stopped. Meganet DRHP (filed 16 Nov 2026) not yet on SEBI's first listing page.
- C5i: confidential pre-filing => no public document by design.

Other exclusions:
- Transline Technologies (DRHP Aug 2025, SEBI observation Jan 2026, OFS-only 1.62 cr shares): security/surveillance systems integrator with AI products -> not AI-native; excluded. [https://www.freepressjournal.in/business/transline-technologies-ipo-in-focus-ai-surveillance-firm-gets-sebi-nod-for-162-crore-share-offer]
- Roadzen, Zoomcar: Nasdaq de-SPACs in 2023 (outside window; not AI-native) — from model knowledge, not checked.
- No completed overseas listing of an India-based AI-native company found in Jan 2024–Nov 2026.

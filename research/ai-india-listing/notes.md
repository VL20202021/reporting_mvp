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

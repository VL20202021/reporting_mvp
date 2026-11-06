# One-Person AI Business: DIFC Dubai vs Bangalore (US entity) vs Paris (SASU)

**Prepared:** 6 November 2026
**For:** Indian citizen, solo founder, plans to raise venture capital (VC)
**Companion files:** `budgets_section7.csv`, `learning_plan.md`, `sources.md`

> **Disclaimer (stated once):** This is research, not legal or tax advice. Rules below change often. Confirm every point marked ⚠️ with a licensed professional before acting: a Chartered Accountant (CA) and FEMA lawyer in India, a CPA in the US, a UAE tax adviser, and an *expert-comptable* in France.

### How to read the labels
- **[VERIFIED]**: from an official or primary source, or several matching legal and professional sources.
- **[REPORTED]**: from a founder, the press, or a consultant's blog. Not independently confirmed.
- **[ESTIMATE]**: my own reasoning. The assumptions are shown.
- **[PRIOR KNOWLEDGE – verify]**: widely known but not re-checked in this research run.

### Assumptions I had to make (your profile had blanks)
| Field | Assumption used |
|---|---|
| Where you live now | Bangalore, Indian tax resident |
| Relocation | Open to moving to Dubai or Paris if it clearly pays off |
| Current skills | Some technical ability, little sales or industry depth yet |
| Hours per week | Full-time (45–55 hours) |
| Living costs | City estimates in Section 7 |
| Exchange rates | 1 USD = 3.6725 AED (pegged), ≈ ₹88, ≈ €0.87. INR and EUR are assumptions, so re-check |

If any of these are wrong, the conclusions on tax and budget change. Tell me and I'll redo those sections.

---

## SECTION 1 — EXECUTIVE SUMMARY

### Recommendation

**Structure**
- If you stay in Bangalore, do **not** use a Delaware or Wyoming *LLC*. It is a poor fit for VC. As an Indian resident it also gives you **almost no tax saving**: India taxes the LLC's profit as your personal income, and the US usually collects nothing you could credit against it.
- Use one of these instead:
  - **(a) An Indian Private Limited company** with DPIIT Startup India recognition. Use this if your first customers and investors are Indian or Gulf-based.
  - **(b) A Delaware C-Corp, owned through a proper RBI ODI filing.** Use this only if a US accelerator such as Y Combinator, or US customers, clearly need it.
- Indian unicorns now pay **USD 150M+** to move back to India. Razorpay is reported at [REPORTED $150M–300M]. So "flip later" is no longer a free option. Choose deliberately.
- **DIFC** is the right answer only if you will **actually live in Dubai**. It gives 0% personal income tax, a Gulf-facing brand, and a Golden Visa path. It costs about 3–5× more per year than Bangalore.
- **Paris SASU** is the weakest fit for an Indian solo founder. It brings high social charges, a 31.4% dividend flat tax, and the visa needs about €30k invested. Choose it only if your market is the EU or you get into Station F with a French co-founder.

**Industry**
- **Cross-border trade and logistics operations**, starting with the India ↔ UAE/GCC trade corridor.

**Idea**
- An **"AI operations agent for freight forwarders and customs brokers."**
- It reads shipping documents (invoices, packing lists, bills of lading), pre-fills customs and shipping filings, writes quotes, chases missing documents over email and WhatsApp, and flags compliance errors.

**First market**
- Mid-size freight forwarders in India (Mumbai, Chennai, Bangalore ICDs) and Dubai (Jebel Ali, DAFZA). The first 10 customers come from India.

**Money needed**
- **Launch:** about **USD 15–20k** (Bangalore, lean).
- **Reach a pre-seed round:** about **USD 35–55k** self-funded over 12–15 months, aiming for USD 5–15k monthly recurring revenue (MRR) with paying customers. In Dubai the same plan needs about **USD 80–120k**, in Paris about **USD 65–100k** [ESTIMATE, Section 7].

### Comparison table (1 = worst, 5 = best, for *your* profile)
| Factor | DIFC (live in Dubai) | Bangalore + US **LLC** | Bangalore + Delaware **C-Corp** | Bangalore + Indian Pvt Ltd (alt.) | Paris SASU |
|---|---|---|---|---|---|
| Setup cost | 2 | 5 | 4 | 5 | 3 |
| Yearly running cost | 2 | 4 | 3 | 4 | 2 |
| Tax on profits | 4 (0–9%) | 2 (taxed in India at your slab) | 3 (21% US + Indian issues) | 3 (≈25%, 80-IAC holiday possible) | 3 (15%/25%) |
| Tax when you take money out | 5 (no personal income tax) | 2 | 2 | 2 | 1 |
| Banking & payments | 3 | 3 | 4 (Stripe US) | 4 (Razorpay, Stripe India) | 4 |
| Visa / residency | 5 | n/a | n/a | n/a | 2 |
| Credibility with customers | 4 (Gulf) | 3 | 4 (US) | 4 (India) | 4 (EU) |
| Ease of raising VC | 3 | **1** | **5** (US VCs) | 4 (Indian VCs) | 3 |
| Ease of selling the company | 3 | 2 | 5 | 3 | 3 |
| Admin time per month | 3 | 3 | 2 (two countries) | 3 | 2 |
| Legal risk for a solo founder | 4 | 2 (FEMA/5472 traps) | 3 | 4 | 4 |

### Top 10 actions for the next 30 days
1. **Days 1–3:** Pick the industry (Section 5). Book 20 calls with freight forwarders and customs brokers using the interview script in `learning_plan.md`.
2. **Days 1–7:** Read *The Mom Test* and start a public build log on LinkedIn or X (one post every 2 days).
3. **Days 3–10:** Book paid consultations: a CA who knows FEMA/ODI, and a startup lawyer. Use the question list in Section 10.
4. **Days 7–14:** Decide on the entity using the decision tree in Section 2.2. **Do not** form a US LLC "just to get Stripe."
5. **Days 10–20:** Incorporate. Sign an IP-assignment deed from you to the company on day one.
6. **Days 10–25:** Build a narrow prototype: upload 5 documents, get a draft filing and quote. Use one model API and an evaluation set of 50 real documents.
7. **Days 15–30:** Get 3 forwarders to agree to a **paid pilot** (USD 200–500 per month) or a signed letter of intent (LOI).
8. **Day 20:** Open a business bank account and payment collection.
9. **Day 25:** Set up the metrics dashboard (Section 8).
10. **Day 30:** Write a one-page investor update and send it monthly to 10–20 angels and early-stage VCs. Building relationships early is the cheapest fundraising tool.

**What this means for me**
- For a Bangalore resident, the real choice is **Indian Pvt Ltd vs Delaware C-Corp**, not Delaware vs Wyoming LLC.
- Move to Dubai only once you have revenue or a funding offer. Then a DIFC holding company becomes sensible.
- Spend the first 30 days on customers, not paperwork. The entity takes about 2 weeks in any option.

---

## SECTION 2 — LEGAL & TAX DEEP DIVE

### 2.1 OPTION 1 — DIFC company with the Innovation / AI licence

**a) What it is**
- A DIFC private company (Ltd) on a non-financial **Innovation Licence**, or the separately marketed **"AI & Coding" licence**.
- DIFC is a common-law free zone, so it has its own courts and its own data protection law.
- It can sell worldwide.
- Selling to UAE "mainland" customers is generally allowed for services delivered remotely. Physical mainland trading needs extra permits ⚠️.
- The AI & Coding licence lets you work from the **DIFC Innovation Hub** [VERIFIED – UAE government portal].

**b) Setup steps (realistic timeline: 3–6 weeks)**
1. Apply through the DIFC client portal with your passport, business plan, CV and proof of address.
2. Reserve the name and get pre-approval.
3. Choose a workspace package in the Innovation Hub. A workspace lease is required [REPORTED – BusinessDubai, BSA Law].
4. Licence issued → establishment card → investor/employment visa → Emirates ID → medical.
5. Open a bank account. Wio, Mashreq NEO Biz and Emirates NBD are common choices. Expect 2–6 weeks and full KYC (know-your-customer checks) on your Indian income source ⚠️.

**c) Costs**
| Item | Low | Typical | High | Label |
|---|---|---|---|---|
| Incorporation fee | $100 | $100 | $8,000 (AI & Coding application) | [REPORTED] |
| Innovation Licence annual fee | $1,500 | $1,500 | $12,500+ (AI & Coding licence, per one consultant) | [REPORTED] |
| Innovation Hub desk/space | $4,000 | $6,000–10,000 | $20,000+ | [ESTIMATE – packages vary] |
| Visa + Emirates ID + medical (founder) | $1,300 | $1,800 | $2,500 | [ESTIMATE] |
| Accounting / tax return / ESR | $1,500 | $3,000 | $6,000 | [ESTIMATE] |
| Audit (if required) | $0 | $2,000 | $4,000 | [ESTIMATE] ⚠️ |
| Health insurance (mandatory in Dubai) | $700 | $1,200 | $3,000 | [ESTIMATE] |

- A BusinessDubai summary of the DIFC handbook (approved 29 Sept 2026) says the Innovation Licence fee is **USD 100 to incorporate and USD 1,500 a year**, rising to **USD 12,000 a year from year 8** [REPORTED – summary of official handbook, verify at difc.com].
- One setup consultant quotes the AI & Coding licence at **USD 8,000 application + USD 12,500+ a year**, with a year-1 total of **USD 28,950+**. I found **no official confirmation** of this. Some sources may be mixing up licence types ⚠️.

**d) Company taxes**
- **UAE Corporate Tax:** 0% on taxable income up to AED 375,000, and 9% above that [PRIOR KNOWLEDGE – verify on tax.gov.ae].
- **Small Business Relief:** businesses with revenue (not profit) ≤ **AED 3M** can elect to be treated as having no taxable income. You must claim it in the EmaraTax return. Once you exceed AED 3M you lose it permanently [VERIFIED – CMS, Fidinam].
  - ⚠️ **The end date conflicts:** some sources say tax periods ending by **31 Dec 2026**, others report an **extension to 2029** [REPORTED – Virtuzone, tbreak]. Check the Ministry of Finance decision.
- **Qualifying Free Zone Person (QFZP):** 0% on "qualifying income." It is mutually exclusive with Small Business Relief [VERIFIED – multiple]. Whether DIFC software or AI services count as "qualifying activities" depends on the Cabinet decision lists ⚠️. For a small startup, Small Business Relief is simpler.
- **VAT:** registration is mandatory above AED 375,000 of taxable supplies [PRIOR KNOWLEDGE – verify]. Exported services are often zero-rated ⚠️.
- **Other filings:** corporate tax registration is required even at 0%. Also keep an Ultimate Beneficial Owner (UBO) register.

**e) Personal tax**
- The UAE has no personal income tax on salary or dividends [PRIOR KNOWLEDGE].
- **India is the catch.** If you keep spending long periods in India, India can still tax you:
  - You are an Indian resident if you are in India ≥ **182 days**.
  - Or ≥ **120 days** if your Indian-source income is over ₹15 lakh and you spent ≥ 365 days in India in the previous 4 years. That case gives RNOR status (resident but not ordinarily resident).
  - Indian citizens with Indian income over ₹15 lakh who are **not liable to tax anywhere** can be "deemed resident." A UAE Tax Residency Certificate generally protects you from this [REPORTED – nriinformation, cleartax; statute at incometaxindia.gov.in].
- **Practical rule:** live in Dubai, keep India days under 120, get a UAE Tax Residency Certificate each year ⚠️.

**f) Banking & payments**
- Stripe is available in the UAE [PRIOR KNOWLEDGE – verify]. Paddle and Lemon Squeezy work as merchant of record.
- Common reasons banks reject applicants: no physical presence, crypto-linked activity, unclear source of funds, and mainly cash-based business models.

**g) Visa for an Indian citizen**
- The licence lets you sponsor your own residence visa, usually 2 years [PRIOR KNOWLEDGE].
- **Golden Visa (entrepreneur route):** needs proof of an innovative project, often an incubator letter. Reported thresholds include AED 1M annual revenue or a startup valuation of about AED 7M, and the visa runs 5 or 10 years. Sources conflict [REPORTED – GCS, Middle East Briefing; official: u.ae / ICP].
- **Cost of living:** a comfortable single life in Dubai Marina or Downtown is ≈ **AED 14,200/month (~$3,870)** [REPORTED]. A one-bedroom in the city centre averages ≈ **AED 8,974/month** [REPORTED – Numbeo via third party].

**h) Year-1 compliance calendar**
| Month | Action |
|---|---|
| M1 | Licence, establishment card, visa, bank. Corporate tax registration on EmaraTax |
| M2 | UBO register. Data protection: register with the DIFC Commissioner if required ⚠️ |
| M3 | Bookkeeping system live, and VAT threshold monitoring |
| M6 | Mid-year accounts check |
| M12 | Licence renewal and confirmation statement |
| Within 9 months after FY end | Corporate tax return (claim Small Business Relief) |
| Yearly | Apply for a UAE Tax Residency Certificate |

**i) AI-specific rules**
- **DIFC Data Protection Law No. 5 of 2020 + Regulation 10** governs personal data processed by "autonomous and semi-autonomous systems" (AI). Full enforcement started **1 January 2026** [VERIFIED – Mayer Brown Jan 2026, Clyde & Co].
  - High-risk commercial uses need certification and audit (rules from the DIFC Commissioner).
  - Processing must be for human-defined or human-approved purposes.
  - You must appoint an **Autonomous Systems Officer** where required.
  - Most duties fall on **deployers**.
- **UAE federal PDPL** applies to mainland customers' data [PRIOR KNOWLEDGE].
- If you sell into the EU, the EU AI Act also applies (see Option 3).

**j) Investor readiness**
- DIFC and ADGM companies are increasingly accepted by Gulf VCs and by Hub71 (Abu Dhabi).
- US VCs and YC usually prefer a Delaware parent. A DIFC holding company with an Indian subsidiary is a workable structure ⚠️.
- DIFC uses English common law, so share classes and ESOP schemes are flexible [PRIOR KNOWLEDGE].

**k) Top 5 risks**
1. Licence-type confusion causing overpayment → get the fee schedule in writing from DIFC.
2. Indian tax residency kept by accident → day-count tracker.
3. Small Business Relief ends → model 9% tax.
4. Bank account delays → apply to two banks in parallel.
5. Regulation 10 duties if you process personal data in high-risk ways → design for human approval steps.

### 2.2 OPTION 2 — Bangalore founder + Delaware/Wyoming LLC (and the C-Corp comparison)

**a) Entity**
- A US single-member LLC is a "disregarded entity" for US income tax unless it elects corporate status [VERIFIED – taxguru, HCVT].
- It can sell worldwide and take Stripe US.

**b) Setup (1–3 weeks US side, plus the India side)**
1. Form the LLC (state filing).
2. Appoint a registered agent.
3. Get an EIN (Form SS-4; non-residents can fax or call).
4. Open a US bank account (Mercury, Relay, Wise).
5. **India side, often missed:** before sending any money, file an **ODI** through your Authorised Dealer bank:
   - Get a Unique Identification Number (UIN).
   - Funds must be your own; borrowed funds are not allowed for start-ups.
   - The entity must be an **operating** company, not financial services, with no controlled step-down subsidiary for individuals.
   - The investment must fit inside the **LRS limit of USD 250,000 per financial year** [REPORTED – Razorpay, Taxguru, Taxmann; primary: RBI Overseas Investment Directions 2022].
   - File the **FLA return** every year.

**c) Costs**
| Item | Delaware LLC | Wyoming LLC | Delaware C-Corp | Label |
|---|---|---|---|---|
| State formation | ~$90 + agent | ~$100 + agent | ~$89+, or Stripe Atlas $500 all-in | [REPORTED] |
| Annual state fee | **$300 LLC tax, due 1 June** | **$60 min. annual report** (or $0.0002 × WY assets) | Franchise tax **$400 min.** (Assumed Par Value method) + $50 annual report, due 1 March | [VERIFIED – Stripe docs; multiple] |
| Registered agent | $50–300 | $25–150 | $50–300 | [ESTIMATE] |
| US tax prep | $500–1,500 (5472 + pro-forma 1120) | same | $1,000–3,000 (Form 1120) | [ESTIMATE] |
| Indian CA (ODI, FLA, Schedule FA) | $300–1,000 | same | same | [ESTIMATE] |

**d) US tax for a foreign-owned single-member LLC**
- It must file **Form 5472 + a pro-forma Form 1120** every year, even with no activity. The deadline is 15 April (extension with Form 7004).
- The penalty is **USD 25,000 per form**, with further penalties if you ignore IRS notices [REPORTED – several CPA firms; primary: IRS Form 5472 instructions].
- US federal tax is often **zero** if you have no US trade or business (effectively connected income, ECI) or US-source income [REPORTED – taxguru].
- **BOI reporting:** since FinCEN's March 2025 interim rule, US-formed companies are exempt from Beneficial Ownership reporting [PRIOR KNOWLEDGE – verify on fincen.gov].

**India side (critical)**
- You are an Indian resident, so you are taxed on worldwide income. India generally taxes a disregarded LLC's profit as **your personal income at your slab rate** (up to ~30%+ plus surcharge), whether or not you bring the money home [REPORTED – taxguru, globalsolo].
- **Foreign tax credit:** only for US tax actually paid. That is usually zero, so there is nothing to offset [REPORTED].
- **Treaty:** the Delhi ITAT, in *General Motors Co USA v ACIT* (2024), held that a fiscally transparent LLC can claim India–US treaty benefits. It is unclear whether this helps an individual owner [VERIFIED – itatonline, RSM].
- **POEM (Place of Effective Management):** for a *corporation* (for example, a Delaware C-Corp) run entirely from Bangalore, India can treat it as Indian-resident and tax it in India too. This is a big risk for solo founders who make every decision from India ⚠️.
- **Disclosure:** report the foreign asset in **Schedule FA** of your Indian income tax return. Missing it risks penalties under the Black Money Act ⚠️.
- **GST:** if you also invoice through an Indian entity, export of services is zero-rated under Section 16 IGST if all 5 conditions in Section 2(6) are met. File a **Letter of Undertaking (LUT, form RFD-11)** each financial year. Beware the "intermediary" classification, which brings 18% GST [REPORTED – CA blogs; primary: gst.gov.in].
- **Transfer pricing** applies if a US entity pays an Indian entity (for example, your Indian development company).

**Delaware vs Wyoming LLC vs Delaware C-Corp, plain verdict**
- **Wyoming LLC:** cheapest and most private. Fine for a lifestyle business or a holding company. **VCs will not invest in it.**
- **Delaware LLC:** also not investable by most VCs, because of the tax pass-through problems for their limited partners [PRIOR KNOWLEDGE].
- **Delaware C-Corp:** the standard for US VCs, YC, SAFEs and ESOPs. If you form a US entity at all, form this one.
  - Converting LLC → C-Corp later costs about **USD 1,000–5,000** in legal and filing fees, plus tax analysis [ESTIMATE].
  - That conversion is cheap compared with fixing a cap table later. So skip the LLC.

**Alternatives you asked me to compare**
| Route | Good for | Watch-outs |
|---|---|---|
| **Indian Pvt Ltd + DPIIT recognition** | India and Gulf customers, Indian VCs, cheapest compliance, no ODI needed | Corporate tax ≈25% [PRIOR KNOWLEDGE]. Angel tax (Sec 56(2)(viib)) **abolished** by Finance Act 2024 [VERIFIED – Inc42, Patron]. 80-IAC tax holiday: 100% of profit for 3 of the first 10 years, but only if the Inter-Ministerial Board approves [VERIFIED – incometaxindia.gov.in] |
| **Delaware C-Corp parent + Indian subsidiary** ("flip") | YC and US VCs, US customers | ODI compliance, transfer pricing, POEM, double compliance cost. A **reverse flip** later costs a fortune: PhonePe ≈ ₹8,000 Cr tax, Razorpay reported **$150M–300M**, Groww ≈ ₹1,340 Cr [REPORTED – IBS Intelligence, Dezerv, Mondaq] |
| **GIFT City IFSC** | Financial-services, fund and fintech-adjacent units | 20-year tax holiday (out of 25 years) announced in Budget 2026, then 15% [REPORTED – Business Standard, Angel One]. Eligible only for **IFSCA-regulated activities**, so it is generally *not* a home for a SaaS startup ⚠️ |

**Honest answer:**
- For a Bangalore-based founder who will raise VC, **start with an Indian Pvt Ltd**.
- Form a Delaware C-Corp parent **only when** an investor such as YC requires it, or US revenue dominates.
- The reverse-flip trend shows big companies paying heavily to come home, which argues against flipping by default.

**f) Banking & payments**
- **Indian Pvt Ltd:** Razorpay and Stripe India both support international cards, subject to RBI cross-border rules ⚠️.
- **US entity:** Mercury or Wise + Stripe US.

**i) Data rules**
- **India's DPDP Act 2023 + DPDP Rules 2025:** notified 13 Nov 2025 and phased over 18 months.
  - Consent Manager rules apply ~Nov 2026.
  - The main obligations apply from ~**13 May 2027** [VERIFIED – YourStory, Mondaq].
- **US:** state privacy laws (California CCPA/CPRA and others). State AI laws exist, for example Colorado's AI Act ⚠️ [PRIOR KNOWLEDGE].

**k) Top 5 risks (Option 2)**
1. Skipping ODI → FEMA penalties.
2. Missing Form 5472 → $25k penalty.
3. Not disclosing in Schedule FA → Black Money Act exposure.
4. A C-Corp run from India → POEM double taxation.
5. LLC chosen and then rejected by VCs → conversion cost and delay.

### 2.3 OPTION 3 — Paris SAS / SASU

**a) Which form to use**
| Form | Fit for a solo AI founder raising VC |
|---|---|
| **SASU** | Best. One shareholder now, converts to SAS automatically when investors join, and BSPCE stock options are available. You are "assimilé salarié" if paid: good social cover, but no unemployment insurance [VERIFIED – Keobiz, Finalib] |
| SAS | Same thing once you have 2+ shareholders |
| EURL | Lower social charges (TNS regime) but less flexible for investors |
| Micro-entreprise | Only for testing freelance consulting. Not investable |

**b) Setup (2–4 weeks)**
1. Draft the *statuts*: €500–1,500 through a professional [REPORTED].
2. Deposit share capital at a bank (€1 minimum by law; €1k–€30k is typical).
3. Arrange *domiciliation* (registered address).
4. Publish a legal notice.
5. File on the **guichet unique (INPI)**.
6. Get the Kbis extract (the company registration certificate).

Total admin cost is ≈ €200–2,000 [REPORTED].

**c) Yearly costs**
| Item | Typical |
|---|---|
| Expert-comptable | €1,500–3,500/year |
| CFE (local business tax) | €200–600 |
| Bank | €200–400 |
| Professional liability insurance (RC Pro) | €400–1,000 |

All [ESTIMATE].

**d) Company taxes**
- **Corporate tax (IS):** 15% on the first **€42,500** of profit (if revenue ≤ €10M and conditions are met), 25% above that [VERIFIED – CGI art. 219, Legalstart, Fiscaloo].
- **VAT:** 20% standard rate [PRIOR KNOWLEDGE].

**e) Personal tax and pay mix**
- **Salary:** total social charges ≈ **75–82% of net salary** [REPORTED – Keobiz, Copeps].
- **Dividends:** no social charges, but the flat tax (PFU) rose to **31.4%** (12.8% income tax + 18.6% social levies) after the 2026 social security budget (LFSS 2026) raised CSG by 1.4 points [VERIFIED – multiple French sources; check BOFiP].
- **Optimal mix** [ESTIMATE]:
  - Take a modest salary, enough to validate pension and health quarters, ~€1,000–2,000 gross per month.
  - Take the rest as dividends.
  - Too little salary risks URSSAF re-classifying the dividends as salary [REPORTED].
- **Unemployment benefits for founders (ARE/ARCE):** only if you previously worked in France. Not relevant unless you have.

**f) Startup support**
- **JEI (Jeune Entreprise Innovante, "young innovative company"):**
  - R&D must be **≥ 20% of deductible costs**. The proposal to raise it to 25% was not adopted.
  - Gives an exemption from employer social charges, up to 4.5× minimum wage per salary and 5× the social security ceiling (PASS, €240,300 in 2026) per establishment.
  - The company must be < 8 years old.
  - **JEIs created in 2024–2026 get no corporate tax exemption** [REPORTED – Hayot Expertise; URSSAF].
- **CIR/CII (research and innovation tax credits):** salaries exempted under JEI still count, but the credit base is reduced by the amount exempted [REPORTED].
- **Bpifrance:** Bourse French Tech and innovation loans. Check current amounts at bpifrance.fr ⚠️.
- **Station F:** founders programmes [PRIOR KNOWLEDGE].

**g) Visa for an Indian citizen**
- **Passeport Talent – création d'entreprise** (L.313-20-5°): reportedly needs **€30,000 personal investment**, a master's degree or 5 years' experience, and a serious business plan. Valid up to 4 years, prefecture fee ≈ €225 [REPORTED – integrationfrance, prefecture PDF].
- **Passeport Talent – projet économique innovant / French Tech Visa** (L.313-20-6°): needs recognition by a public body such as an approved incubator [REPORTED].

**i) AI rules**
- **EU AI Act:**
  - Bans have applied since Feb 2025.
  - General-purpose AI (GPAI) model obligations have applied since **2 Aug 2025**, unchanged.
  - Under the **Digital Omnibus** provisional deal (7 May 2026), *high-risk* Annex III systems move to **2 Dec 2027** and product-embedded systems to **2 Aug 2028** [VERIFIED – Gibson Dunn, Sidley, CMS].
- **For you:** a freight-documents agent is **not high-risk**. You'd mainly have transparency duties (tell users they're dealing with AI; label generated content).
- **GDPR and CNIL guidance** apply to any EU personal data.

**k) Top 5 risks (Option 3)**
1. High cost of paying yourself.
2. Visa capital requirement.
3. Paris living costs.
4. Slow bank KYC for non-EU founders.
5. Thin French networks for an India–Gulf trade product.

**What this means for me (Section 2)**
- For your plan, the **Indian Pvt Ltd** (or a Delaware C-Corp done through proper ODI) beats any LLC.
- **DIFC** becomes the best *personal* tax outcome once you relocate and stay outside India long enough. Plan that for Year 2, after traction.
- **Paris** only makes sense with an EU-first market. It doesn't match an India–Gulf trade product.

---

## SECTION 3 — CASE STUDIES: REAL ONE-PERSON AI BUSINESSES

**Honesty note:**
- I could verify only a **small number** of solo AI businesses with public revenue figures. Most numbers are **self-reported**.
- I found **no verifiable UAE-based solo AI business** with public revenue. Dubai's AI startups listed on ecosystem directories are funded teams, for example a legal-AI platform with a $2M pre-seed [REPORTED – eChai].
- For **France**, the only well-documented case is a French founder who lives abroad.
- I have **not** padded these lists to reach 8 per region.

### 3.1 Table
| Name | Founder | Base / entity | Sells | Price | Customer | Launch | Revenue (label) | Team | Main channel | Key metric | Stack | Funding | Background | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Base44** | Maor Shlomo | Israel | AI app builder (no-code) | Freemium → subscriptions | Non-developers, SMBs | ~Dec 2024 | Acquired by **Wix for ~$80M cash**, June 2025 [VERIFIED – multiple press] | 1 (first hire just before sale) | Word of mouth, X, community | Users, paid conversion | LLM APIs | Bootstrapped | Serial founder, engineer | Entrepreneur.com, whatastartup |
| **Photo AI** | Pieter Levels | Dutch, nomadic | AI photo generation | ~$19–99/mo | Consumers, creators | 2023 | ~$132K MRR (≈$1.65M ARR) late 2025, >87% net margin [REPORTED – public dashboard] | 1 | Build-in-public on X, SEO | MRR, profit | PHP, jQuery, Replicate-hosted models | Bootstrapped | Self-taught maker | cipherprojects, mean.ceo |
| **HeadshotPro** | Danny Postma | Netherlands | AI professional headshots | One-off $29–59 | Professionals, teams | 2023 | $1M ARR in < 1 year. Reported $300K/month at peak, later sold for 7 figures [REPORTED] | 1 | SEO, affiliates | Revenue, conversion | Fine-tuned image models | Bootstrapped | Marketer-developer | mean.ceo, cipherprojects |
| **Marc Lou portfolio** (ShipFast, CodeFast, DataFast, TrustMRR) | Marc Louvion | **French**, lives in Bali | Boilerplates, courses, analytics, verified-revenue marketplace | $99–299 one-off; SaaS plans | Indie developers | 2023–2025 | **$1.032M in 2025**. Jan 2026: TrustMRR $31.4K, CodeFast $23.5K, DataFast $17.5K, ShipFast $17.2K/month [REPORTED] | 1 | X build-in-public, YouTube, launches | Monthly revenue per product | Next.js, Stripe | Bootstrapped | Developer, failed ~30 projects first | yespress, ibtimes |
| **SiteGPT** | Bhanu Teja Paccha | **India** | Custom chatbots trained on a site's data | ~$39–499/mo | SMBs, SaaS | 2023 | ~$95K MRR reported by one source; another cites $222,969 total [REPORTED – conflicting] | 1 | X build-in-public, SEO | MRR | OpenAI API, RAG | Bootstrapped | IIT Madras graduate, developer | crazyburst, Indieniche |
| **AudioPen** | Louis (India) | **India** | Voice → clean text notes | Subscription | Consumers, writers | 2023 | Headline claims $15K MRR [REPORTED, unverified] | 1 | Product Hunt, X | MRR | Whisper + LLM, no-code | Bootstrapped | Built 15–20 small tools first | Medium |
| **SalesRobot** | (IIT Delhi founder) | **India** | LinkedIn + email outreach automation | Subscription | B2B sales teams | ~2020 | ~$1M ARR [REPORTED – directory] | Small | SEO, content | ARR | — | Bootstrapped | IIT Delhi | indiemakerlist |
| **Hirevire** | — | **India (Mumbai)** | Async video screening | Subscription | Recruiters | — | $14K MRR [REPORTED – directory] | Solo/micro | SEO, integrations | MRR | — | Bootstrapped | — | indiemakerlist |
| **Medvi** | Matthew Gallagher | **USA** | Telehealth (AI-run operations) | — | Consumers | — | "On track for $1.8B revenue" [REPORTED – **unverified, treat with caution**] | 2 | Paid acquisition | Revenue | AI agents for ops | ~$20K self-funded | — | abargon |
| **Polsia** | Ben Broca | — | AI agency/ops for client companies | — | 1,100 client companies | — | >$1M ARR [REPORTED] | 1 | — | ARR | AI agents | — | — | mean.ceo |
| **Physio prior-auth agent** (unnamed) | — | USA | AI agent automating prior authorisations for physiotherapy clinics | Per clinic | Clinics | — | $41K MRR in 14 months [REPORTED – single blog] | 1 | Direct outreach | MRR | — | — | — | foundra |

**By region**
- **USA:** Medvi, the physio prior-auth agent, plus the global ones that sell mainly to the US.
- **India:** SiteGPT, AudioPen, SalesRobot, Hirevire.
- **France:** Marc Lou (French founder, foreign base).
- **UAE:** none found.

### 3.2 Breakdowns of the most relevant cases

**1. Base44: the solo exit that proves VC-scale is possible**
- **Problem and buyer:** non-developers who want working apps. They pay a subscription.
- **First customers:** a free tier, then sharing on X and LinkedIn, then fast word of mouth. Wix bought it about 6 months after launch.
- **What AI automated:** coding, support, onboarding.
- **Skills that mattered:** a deep technical builder plus relentless public shipping.
- **Copy:** speed and public iteration.
- **Don't copy:** a horizontal "build anything" product. The big AI labs and Lovable/Replit compete there, so platform risk is very high.

**2. Physio prior-authorisation agent: the closest template for you**
- **Problem and buyer:** clinics lose staff hours on insurance paperwork. The clinic pays per location.
- **Why it works:** a boring workflow, a clear return on investment (ROI) in staff-hours saved, and buyers who don't follow AI Twitter.
- **Copy:** pick one paperwork-heavy workflow in one industry and charge per seat or per location.
- **Adapt:** use trade documents instead of insurance forms.

**3. SiteGPT: the Indian solo founder template**
- **Problem and buyer:** website owners want a chatbot trained on their own content.
- **First customers:** came from building in public on X.
- **Pricing:** tiered monthly plans.
- **What to learn:** an Indian founder can sell globally in USD from India.
- **Risk:** this category is now commoditised, because every helpdesk ships it. So **don't copy the product**. Copy the GTM.

**4. Marc Lou: distribution as a moat**
- **First customers:** 100k+ followers built over years. Each launch converts that audience.
- **Pricing:** one-off purchases with a low support load.
- **Copy:** owned audience, plus revenue transparency as marketing.
- **Don't copy:** products aimed at other indie hackers. That market is small and not venture-scale.

**5. HeadshotPro and Photo AI: consumer AI cash machines**
- **Lesson:** extremely high margins are possible when a model does the work.
- **Warning:** both depend on image-model quality that Google and OpenAI now give away. Platform risk is extreme.
- **For a VC-backed B2B path, copy only:** SEO landing pages and fast pricing experiments.

**6. SalesRobot and Hirevire: Indian B2B micro-SaaS**
- **Lesson:** SEO plus integrations get to $10k–80k MRR without funding.
- **Copy:** "alternative to X" SEO pages and a marketplace listing (Zapier, HubSpot).

**What this means for me (Section 3)**
- The repeatable solo pattern is a **narrow workflow, a clear ROI, and owned distribution**.
- Venture-scale solo exits (Base44) exist but are rare. Plan for **vertical B2B**, not consumer.
- No UAE solo case is public, so Dubai founders are building with small teams. That is less competition for a Gulf-facing vertical tool.

---

## SECTION 4 — PATTERNS: HOW SOLO AI BUSINESSES WIN

### 4a) Success metrics
| Metric | Healthy for a solo AI B2B business | Investors at pre-seed | Investors at seed | Label |
|---|---|---|---|---|
| MRR | $5–30K in year 1–2 for strong niche founders | $5–20K MRR, or 3–10 paying design partners | $50–150K MRR ($0.6–1.8M ARR) | [ESTIMATE; a blog benchmark gives $10–30K MRR in 1–2 years as a strong outcome] |
| Month-over-month growth | 10–20% early | 15%+ | 10–15% sustained | [ESTIMATE] |
| Gross margin after AI costs | ≥ 70% | Shown and improving | ≥ 70% | [ESTIMATE] |
| AI inference cost as % of revenue | < 15–20% | Tracked | < 15% | [ESTIMATE] |
| Logo churn (B2B) | < 3%/month | — | < 2%/month | [ESTIMATE] |
| Net revenue retention (NRR) | > 100% | — | > 110% | [ESTIMATE] |
| CAC payback | < 6 months | — | < 12 months | [ESTIMATE] |
| Revenue per employee | $500K–1.5M+ (solo) | — | — | [REPORTED – Photo AI ~$1.65M/1 person] |

Context from Carta's Solo Founders Report 2025 (published 9 Dec 2025) [VERIFIED – carta.com]:
- Solo-founded startups rose from **23.7% (2019) to 36.3% (H1 2025)** of new startups.
- They got only **14.7% of priced-round cash** (2024 cohort, 30% of startups).
- Their median time to first hire is **399 days**.

### 4b) GTM playbooks, ranked by evidence in the cases above
1. **Build in public on X or LinkedIn** (Levels, Marc Lou, SiteGPT, Base44). Strongest for developer and SMB tools, weaker for traditional industries.
2. **SEO and programmatic SEO** (HeadshotPro, SalesRobot, Hirevire). Compounds over 6–18 months.
3. **Direct outreach to a narrow vertical** (physio prior-auth). Best for vertical B2B, and it fits your idea.
4. **Product Hunt and launch platforms** (AudioPen). A one-time spike.
5. **Marketplaces and integrations** (Zapier, HubSpot, Shopify, Chrome Web Store).
6. **"AI search" visibility:** structured comparison pages and FAQs so ChatGPT and Perplexity cite you [ESTIMATE – emerging].
7. **Communities:** WhatsApp and Telegram groups of forwarders, CHA (customs house agent) associations, Gulf trade groups.
8. **Partnerships and resellers:** freight software vendors, customs brokers' associations, bank trade-finance desks.
9. **Government and enterprise procurement:** slow. Leave it for after seed.

### 4c) Regional differences [ESTIMATE, from experience; verify with interviews]
| | India | UAE/GCC | USA | France |
|---|---|---|---|---|
| Buying style | Price-sensitive, relationship-led, demo on WhatsApp | Relationship and trust-led, in person, references matter | Self-serve OK, ROI-led | Formal, French language, GDPR questions early |
| Payment habits | UPI, annual prepay discounts | Bank transfer, annual contracts | Card, monthly SaaS | SEPA, annual contracts |
| Language | English + Hindi/regional | English + Arabic | English | French |
| Typical SMB SaaS price | ₹2,000–15,000/month ($25–170) | AED 500–3,000/month ($135–820) | $100–1,000/month | €100–800/month |

### 4d) Margins and platform risk
- **Best margins and lowest risk for one person:** vertical workflow tools priced per seat or per document, sold to non-tech industries, with private data and integrations.
- **Dies on a big-lab feature release:** generic chatbots, writing tools, headshots and image apps, "chat with PDF," general coding agents.

**What this means for me (Section 4)**
- Track **MRR, gross margin after inference cost, logo churn, and paying design partners** from month 1.
- Your GTM is **direct outreach + WhatsApp + one SEO cluster**, not Twitter virality. Use LinkedIn build-in-public to attract investors.
- Pick a workflow that ChatGPT can't do alone because it needs integrations and private documents.

---

## SECTION 5 — BEST INDUSTRY AND SKILLS PLAN FOR ME

### 5a) Industry ranking (1–5 scores) [ESTIMATE, reasoning shown; funding evidence cited]
| # | Industry | Market size | Pain | Willingness to pay | Slow AI adoption (= opportunity) | Low platform risk | Fundable | Learn fast | Indian founder edge | **Total /40** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Trade & logistics ops (forwarders, customs brokers)** | 5 | 5 | 4 | 5 | 5 | 5 | 3 | 5 | **37** |
| 2 | SME finance & accounting ops | 5 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 31 |
| 3 | Insurance ops (brokers, claims) | 5 | 5 | 5 | 4 | 4 | 5 | 2 | 3 | 33 |
| 4 | Healthcare admin & billing (US) | 5 | 5 | 5 | 3 | 4 | 5 | 2 | 4 (outsourcing know-how) | 33 |
| 5 | Real estate & construction docs (Gulf) | 4 | 4 | 4 | 5 | 4 | 3 | 3 | 4 | 31 |
| 6 | Legal & compliance | 4 | 4 | 4 | 3 | 2 | 4 | 2 | 3 | 26 |
| 7 | Recruiting/HR | 4 | 3 | 3 | 2 | 2 | 3 | 4 | 4 | 25 |
| 8 | Remittances & cross-border payments | 5 | 4 | 3 | 3 | 4 | 3 | 2 | 5 | 29 (heavy regulation) |
| 9 | Manufacturing (procurement, quality) | 4 | 4 | 4 | 5 | 4 | 3 | 2 | 4 | 30 |
| 10 | Education | 4 | 3 | 2 | 3 | 2 | 2 | 4 | 4 | 24 |

**Why trade and logistics wins for you**
- Investors are funding AI agents in freight right now:
  - **HappyRobot** raised a $44M Series B at a ~$500M valuation. Customers include DHL, Ryder and Flexport.
  - **Cargofy** raised an $11M Series A in June 2026 for AI freight-dispatch workers.
  - **Loop** raised a $95M Series C [REPORTED – getcoai, aifunding.me, PYMNTS; verify on Crunchbase].
- The work is document-heavy, multilingual, and run over email and WhatsApp. That is exactly what LLM agents now do well.
- Big labs will not build customs-specific workflows.
- **Your edge:**
  - The India ↔ UAE corridor is one of India's largest trade relationships, under the India–UAE CEPA (signed 2022) [PRIOR KNOWLEDGE – trade volumes: check the Ministry of Commerce].
  - Indian back-office talent costs less.
  - You can serve both ends of the corridor.
- **Runners-up:** insurance and US healthcare billing have higher willingness to pay, but they're harder to learn and more regulated.

### 5b) Skills audit
| Skill | Why it matters long-term | How AI changes its value (5–10 years) | "Good enough" for a solo founder |
|---|---|---|---|
| 1. Selling and customer discovery | Traction = funding. Building is getting cheaper | **Rises.** Trust and closing stay human | 20+ interviews per month, close paid pilots, write a pricing page that converts |
| 2. Domain expertise (trade/logistics) | Your moat against generic AI | **Rises.** Knowing the workflows and rules is scarce | Explain HS codes, Incoterms, a bill of lading, a customs declaration flow and its pain points like a 5-year ops manager |
| 3. Applied AI engineering | Lets you ship without hiring | **Shifts.** Writing code gets cheaper, but evaluation and reliability get more valuable | Ship an agent with document extraction, tool calls, an eval suite at ≥95% field accuracy, and a known cost per document |
| 4. Owned distribution | Cheapest customer acquisition (CAC) and attracts investors | **Rises.** AI content floods channels, so a trusted voice is worth more | 2–5k targeted LinkedIn followers in the industry, plus a monthly newsletter |
| 5. Finance & legal literacy | Avoids expensive mistakes | Stable | Read a SAFE/term sheet, model dilution, know your unit economics |
| 6. Judgement/taste | Decides what not to build | **Rises most** | Kill or keep decisions using metrics every 2 weeks |

**Skills losing value** (spend little time on these): hand-coding boilerplate, low-level ML research and model training, generic content writing, memorising frameworks, and no-code tool tricks as a core identity.

### 5c) 12-month learning plan
See **`learning_plan.md`**: a month-by-month plan with projects, hours and progress checks.

### 5d) Gaining domain expertise fast
- **Customer interviews:** 50 in 60 days. The script is in `learning_plan.md`.
- **Trade bodies and events** [PRIOR KNOWLEDGE – check dates]:
  - FFFAI (Federation of Freight Forwarders' Associations in India)
  - Customs brokers' associations in Mumbai and Chennai
  - Dubai Chamber
  - Gulf logistics expos in Dubai
  - US: the Customs Brokers association (NCBFAA)
- **Hands-on:** work 2 weeks unpaid or cheaply inside a forwarder's documentation desk. This is the fastest route to real knowledge.
- **Advisor:** a retired ops head from a forwarder, for 0.25–1% equity with vesting.
- **Data:** public customs tariff schedules, ICEGATE documentation, UAE customs guides.
- **Paid pilots:** charge from day one, even a small amount. Payment proves the pain is real.

### 5e) What investors look for in a solo founder
- **Evidence of speed:** shipping logs, a public changelog.
- **Customer pull:** paying pilots and retention.
- **Domain insight:** a sharp memo on the industry.
- **Ability to recruit:** advisors, a planned first hire or co-founder.

Carta's data shows solo founders get fewer VC dollars [VERIFIED]. The usual counters are strong traction, credible advisors, and a stated plan to add a technical or commercial co-founder or first hire at seed.

**What this means for me (Section 5)**
- Commit to **trade and logistics ops** for at least 12 months.
- **Selling + domain knowledge first, AI engineering second.** Build only what pilots pay for.
- Use LinkedIn posts about the forwarding industry as your investor signal.

---

## SECTION 6 — WHAT I SHOULD BUILD

### Five ideas in trade & logistics, plus 2 wildcards
| # | Idea | Customer | Problem | Offer | Price | First channel | Time to revenue | 12-month ARR (cons/base/upside) [ESTIMATE] |
|---|---|---|---|---|---|---|---|---|
| **1** | **DocOps agent for forwarders and customs brokers** | Forwarders and CHAs with 10–200 staff (India, UAE) | Staff re-type data from invoices, packing lists and bills of lading into customs/ERP systems. Errors cause penalties and delays | Upload or email documents → extraction → draft customs entry and shipment record → exception flags → WhatsApp chaser for missing documents | $300–1,500/month per branch, or $0.50–2 per document | Direct outreach + associations | 1–3 months | $36k / $120k / $300k |
| 2 | Quote & rate desk agent | Forwarders | Slow spot quotes lose deals | Reads quote requests, pulls rates, drafts quotes in under 5 minutes | $200–800/month | Same | 2–4 months | $24k / $80k / $200k |
| 3 | Export compliance checker for SME exporters | Indian SME exporters | HS-code mistakes, missed duty drawbacks and CEPA benefits | Classify goods, check certificate of origin and CEPA eligibility | ₹3–10k/month | Export councils, CAs | 2–4 months | $15k / $60k / $150k |
| 4 | Trade-finance document checker | Banks' trade desks, exporters | Letter-of-credit discrepancies | Checks documents against LC terms | Enterprise | Bank partnerships | 6–12 months | $0 / $50k / $250k |
| 5 | Shipment visibility + customer-update agent | Forwarders' customers | "Where is my shipment?" emails and calls | Auto status updates over WhatsApp and email | $100–500/month | Upsell from idea #1 | 3–6 months | $10k / $40k / $120k |
| W1 | US healthcare billing denial-appeal agent | US clinics | Denied claims | Drafts appeals | $500–2,000/month | Outreach | 3–6 months | $30k / $120k / $400k |
| W2 | Insurance broker submission agent (Gulf) | SME brokers | Manual submissions | Extract and pre-fill | $500+/month | Outreach | 3–6 months | $20k / $90k / $250k |

### Detail for the recommended idea (#1)
- **Market size:** I didn't find a sourced market figure for forwarder documentation software. Do bottom-up sizing during interviews: number of licensed customs brokers in India and the UAE × price [ESTIMATE].
- **Competitors:**
  - HappyRobot ($44M Series B) focuses on voice and email agents for large US freight operators.
  - Cargofy ($11M Series A) focuses on dispatch.
  - Incumbent freight ERPs (CargoWise and local Indian ERPs) have weak AI.
  - None is clearly focused on the **India–GCC customs paperwork** workflow [REPORTED funding; positioning is my ESTIMATE – verify].
- **Defensibility:**
  - A corpus of labelled documents (with permission).
  - Integrations with ICEGATE, Dubai Trade and Mirsal, and the freight ERPs.
  - WhatsApp-native workflows.
  - Switching costs once it's embedded in daily operations.
- **Indian founder edge:** you can serve both ends of the corridor, build at low cost, and do human-in-the-loop quality checks cheaply in India.
- **Skills used most:** selling, then domain knowledge, then AI engineering (evals).
- **Questions an investor will ask:**
  1. Accuracy on messy scans?
  2. Time saved per shipment?
  3. Is pricing per document or per seat?
  4. How do you go from India and the UAE to the US and EU?
  5. Why won't CargoWise build this?
  6. Gross margin after model costs?
- **Path to USD 1M+ ARR:** 150 branches × $600/month ≈ $1.08M ARR [ESTIMATE].

**Why the others lose**
- **#2** is a feature of #1, so upsell it later.
- **#3** has lower willingness to pay.
- **#4** has slow enterprise sales.
- **#5** is easy to copy.
- **Wildcards:** good, but you'd start from zero domain knowledge and without your corridor advantage.

**What this means for me (Section 6)**
- Build **idea #1**, starting with a single document type: commercial invoice + packing list → customs entry draft.
- Charge from pilot one. Target 10 paying branches by month 6.
- Add the quote desk (#2) as an upsell once retention is proven.

---

## SECTION 7 — HOW MUCH MONEY I NEED

The full line-by-line tables are in **`budgets_section7.csv`** (USD, plus local currency). Everything here is **[ESTIMATE]**, built from the fees cited in Section 2 plus my assumptions for tech, marketing and living costs.

### 12-month totals (USD)
| Option | LEAN | RECOMMENDED | COMFORTABLE |
|---|---|---|---|
| Bangalore + Indian Pvt Ltd | **$15,600** (₹13.7 L) | $35,000 (₹30.8 L) | $70,000 (₹61.6 L) |
| Bangalore + Delaware C-Corp (via ODI) | $17,250 (₹15.2 L) | $37,500 (₹33 L) | $74,100 (₹65.2 L) |
| Bangalore + Wyoming/Delaware LLC | ~$16,500 | not recommended | not recommended |
| DIFC (live in Dubai) | **$53,600** (AED 197k) | $82,100 (AED 302k) | $152,600 (AED 560k) |
| Paris SASU (live in Paris) | **$42,100** (€36.6k) + €30k visa investment* | $66,600 (€57.9k) | $109,600 (€95.4k) |

\*The Passeport Talent business-creation route reportedly needs €30k invested in the project [REPORTED]. That capital can fund the business, but you must have it upfront.

### Break-even and runway (base revenue case, idea #1) [ESTIMATE]
- **Base revenue path:**
  - Month 3: 3 pilots × $300.
  - Month 6: 10 × $450.
  - Month 9: 20 × $500.
  - Month 12: 30 × $550 ≈ $16.5K MRR.
- **Bangalore lean (~$1.3K/month all-in):** revenue covers costs around **month 5–6**. Bangalore recommended (~$2.9K/month): around **month 7–8**.
- **Dubai lean (~$4.5K/month):** around **month 9–10**.
- **Paris lean (~$3.5K/month):** around **month 8–9**.

### Minimum capital to start (one line each)
| Option | Minimum to start |
|---|---|
| Bangalore Pvt Ltd | **≈ $5k** to launch + 6 months' living ≈ **$10k** |
| Bangalore + Delaware C-Corp | **≈ $6k** + 6 months' living ≈ **$11k** |
| DIFC | **≈ $15k** setup + first year fixed + 6 months' Dubai living ≈ **$30k** |
| Paris SASU | **≈ €30k** (visa investment) + 6 months' living ≈ **€45k (~$52k)** |

### "How much do I need to SUCCEED?"
**Success** here means reaching a fundable pre-seed milestone: **USD 5–15K MRR from 10–30 paying B2B customers, retention above 90%, and month-over-month growth of 15% or more.** This usually takes **9–15 months** [ESTIMATE].

| Option | Self-funded amount to reach pre-seed | Months | Round to raise next | Restructuring cost before the raise |
|---|---|---|---|---|
| Bangalore + Indian Pvt Ltd | **$35–55k** | 12–15 | India pre-seed **₹1–4 Cr ($120–500k)** [REPORTED – blog ranges]. Venture Intelligence data implies ~$1M average pre-seed deal in 2025 [REPORTED, my arithmetic] | $0 if Indian VCs. Flip to Delaware for YC/US VCs: ~$10–30k legal + tax analysis [ESTIMATE] ⚠️ |
| Bangalore + Delaware C-Corp | **$38–58k** | 12–15 | US pre-seed **$500k–1.5M** [ESTIMATE]. YC: **$500k** ($125k for 7% + $375k uncapped MFN SAFE) [REPORTED – multiple] | ~$0 (already investable) |
| DIFC | **$80–120k** | 12–15 | Gulf pre-seed $250k–1M [ESTIMATE]. Hub71 Access: reportedly AED 250k cash on a SAFE + AED 250k in-kind (requires an Abu Dhabi presence) [REPORTED] | Possibly add an ADGM/Delaware parent for US investors: ~$5–20k [ESTIMATE] |
| Paris SASU | **$65–100k** | 12–15 | French pre-seed €300k–1M + Bpifrance matching [ESTIMATE] | Low (SASU → SAS is automatic when investors join) |

**What this means for me (Section 7)**
- **The cheapest path to a fundable company is Bangalore + Indian Pvt Ltd: about $35–55k all-in.**
- Moving to Dubai first roughly **doubles** the money you need before traction.
- Keep 3 months of costs as an untouchable buffer. Fundraising takes 3–6 months.

---

## SECTION 8 — SOLO-FOUNDER OPERATING SYSTEM

### Tool stack [ESTIMATE – prices change monthly; check vendor sites]
| Function | Tools | Approx. cost/month |
|---|---|---|
| Development | An AI coding agent (Claude Code, Cursor or similar), GitHub, Vercel/Render, Postgres (Supabase/Neon) | $40–200 |
| AI models | A frontier model API for hard documents + a cheaper model for simple fields. Use an OCR/vision model for scans | $50–600, usage-based |
| Evals and monitoring | An open-source eval harness (e.g., Langfuse or Promptfoo) + error logging | $0–100 |
| Sales | LinkedIn Sales Navigator, Apollo or similar, a CRM (HubSpot free) | $0–150 |
| WhatsApp | WhatsApp Business API through a provider (Twilio/Gupshup/Meta Cloud API) | $20–100 + per-message |
| Support | Shared inbox + an AI help-doc bot | $0–50 |
| Marketing | Newsletter tool, Canva, LinkedIn | $0–50 |
| Finance | Zoho Books (India) / Xero, Stripe or Razorpay, a bank | $15–50 |
| Legal admin | Templates from Clerky/YC (US) or an Indian startup lawyer | one-off |

### Outsourcing [ESTIMATE]
- Document labelling and QA in India: ₹15–40k/month part-time.
- Designer: $300–1,000 per project.
- CA or accountant: as in Section 7.

### Weekly rhythm (50 hours)
| Activity | Hours/week |
|---|---|
| Customer calls, demos and sales | 15 |
| Building | 15 |
| Evals and quality | 5 |
| Content (2 LinkedIn posts + 1 newsletter per month) | 5 |
| Learning | 5 |
| Admin/finance | 2 |
| Weekly review | 3 |

**Friday dashboard:** MRR, new pilots, documents processed, field accuracy, cost per document, gross margin, churn, pipeline value, cash runway.

### Before the first paying customer
- Terms of service and a privacy policy.
- A Data Processing Agreement (DPA), needed for GDPR and DPDP. Your customers' documents contain personal data.
- An SLA (service level agreement) with an accuracy disclaimer and human-review language.
- An IP assignment from you to the company.
- Professional indemnity / errors & omissions (E&O) insurance once you're processing customs filings ⚠️.

**What this means for me (Section 8)**
- Under $500/month of tooling is enough until about $10k MRR.
- Evals are not optional: wrong customs data costs your customers money.
- Get the DPA and the "human approves before filing" workflow right. It also meets DIFC Regulation 10 and EU AI Act transparency expectations.

---

## SECTION 9 — 90-DAY EXECUTION PLAN

| Week | Focus | Exit checkpoint |
|---|---|---|
| 1 | Industry immersion. Book 20 interviews. Read *The Mom Test* | 20 calls booked |
| 2 | 10 interviews done. Map the document workflow. Collect 50 sample documents (anonymised, with permission) | Top 3 pains ranked |
| 3 | CA + lawyer consults. Choose the entity. Incorporate. IP assignment | Entity filed |
| 4 | Prototype: invoice + packing list → structured JSON → draft entry | ≥85% field accuracy on 50 documents |
| 5 | Bank, payments, DPA/ToS. 5 more interviews | 3 pilot verbal yeses |
| 6 | Pilot onboarding (2–3 forwarders), done by hand behind the scenes | **Day 45: 3 paying pilots at ≥$200/month, or change the document type or segment** |
| 7 | WhatsApp chaser feature | Time saved measured per shipment |
| 8 | Eval suite to 200 documents, cost per document tracked | ≥93% accuracy, < $0.15 per document [ESTIMATE target] |
| 9 | Pricing test: per-document vs per-branch | One pricing model chosen |
| 10 | Case study #1 published (LinkedIn + one landing page) | 5 inbound leads |
| 11 | Outreach sprint: 100 targeted messages | 15 demos |
| 12 | Investor relationship-building: monthly update to 20 angels and VCs | 5 investor coffee chats |
| 13 | Review: retention, margin, pipeline | **Day 90: 6–10 paying customers, $2–5K MRR, or pivot to idea #2/#3** |

**What this means for me (Section 9)**
- Hard kill or pivot checkpoints at **day 45 and day 90** stop you drifting.
- Do things that don't scale (manual review) in the first 60 days. Automate only what's proven.
- Start investor updates in week 12, *before* you need money.

---

## SECTION 10 — RISKS, RED FLAGS & SOURCES

### Top 15 risks
| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | FEMA/ODI not filed for a foreign entity | Medium | High | AD bank ODI + UIN *before* funding. Annual FLA |
| 2 | Form 5472 missed (US LLC) | Medium | High ($25k) | Avoid the LLC, or use a CPA from day 1 |
| 3 | POEM: a C-Corp run from India taxed as Indian | Medium | High | Board decisions and documentation. Get advice |
| 4 | Indian tax residency kept after moving to Dubai | Medium | High | Day-count tracking, UAE Tax Residency Certificate |
| 5 | UAE Small Business Relief ends | Medium | Low–Medium | Model 9% above AED 375k |
| 6 | DIFC licence fee or type misunderstood | Medium | Medium | Written quote from DIFC |
| 7 | Bank account rejection | Medium | Medium | Two banks in parallel, clean source-of-funds file |
| 8 | Customs data errors cause customer penalties | Medium | High | Human approval step, E&O insurance, SLA limits |
| 9 | Data protection breach (DPDP/GDPR/DIFC DPL) | Low–Medium | High | DPA, encryption, data minimisation, retention limits |
| 10 | Incumbent ERP (e.g., CargoWise) ships similar AI | Medium | Medium | Win on the India–GCC niche, WhatsApp, speed, service |
| 11 | LLM price or quality shifts | High | Low–Medium | Model-agnostic design, evals, routing |
| 12 | Slow sales cycles in traditional industries | High | Medium | Associations, referrals, low-risk paid pilots |
| 13 | Solo-founder bias in fundraising | High | Medium | Traction, advisors, co-founder/first-hire plan |
| 14 | Burnout | Medium | High | 50-hour cap, weekly review |
| 15 | Reverse-flip cost if you flip to Delaware and later want an Indian IPO | Low (early) | Very high | Don't flip unless an investor requires it |

### Scams and bad advice to avoid
- "Zero tax forever with a Wyoming LLC from India." False for an Indian resident.
- "Golden Visa guaranteed with the licence." Thresholds apply.
- Nominee directors or shareholders to "hide" ownership. Illegal or risky under UBO rules.
- Agents quoting DIFC "AI licence" packages with no official fee schedule.
- "Get Stripe US without an EIN or entity."
- Fake "government grants" requiring upfront fees.

### Questions to ask professionals before signing
**India CA / FEMA lawyer**
1. Is my foreign entity an "operating entity" under the OI Rules 2022?
2. What is the ODI/UIN process at my bank?
3. Does POEM apply to my structure?
4. Schedule FA reporting?
5. Pvt Ltd vs Delaware for my investor plan?
6. Can I get 80-IAC?

**US CPA**
1. Do I have ECI or US-source income?
2. Form 5472 or 1120 obligations?
3. Delaware franchise tax method?
4. State nexus from US customers?

**UAE adviser**
1. Exact DIFC licence and fee schedule in writing?
2. Small Business Relief end date?
3. Do my activities qualify for QFZP?
4. Tax Residency Certificate requirements?
5. Do I need to register under Regulation 10?

**Expert-comptable**
1. Optimal salary/dividend split with PFU at 31.4%?
2. JEI eligibility at ≥20% R&D?
3. CIR/CII?
4. Talent Passport capital rules?

### Sources
See **`sources.md`**, grouped by section, with publishers and dates.

---

## Confidence by section
| Section | Confidence | Not verified / weak spots |
|---|---|---|
| 1 Summary | Medium | Depends on the profile assumptions above |
| 2.1 DIFC | **Low–Medium** | AI & Coding licence fees (one consultant source), Hub desk prices, Small Business Relief end date (2026 vs 2029), QFZP qualification, AED 375k thresholds from prior knowledge |
| 2.2 India/US | Medium | Primary RBI/IRS text not read directly. BOI status from prior knowledge. POEM application needs professional advice |
| 2.3 France | Medium | PFU 31.4% effective-date details, €30k Talent Passport threshold (secondary sources), Bpifrance amounts |
| 3 Case studies | **Low–Medium** | Almost all revenue is self-reported. No UAE cases found. Only one French founder. Medvi figure doubtful |
| 4 Patterns | Medium | Benchmarks are mostly my estimates. Carta data verified |
| 5 Industry/skills | Medium | Funding rounds from secondary aggregators. Corridor trade volume not verified |
| 6 Ideas | Medium–Low | No sourced market-size figure. Competitor positioning is my estimate |
| 7 Money | Medium | Fees partly verified. Living, tech and marketing costs are estimates. Exchange rates assumed |
| 8–9 Ops & plan | Medium–High | Practices, not facts. Tool prices change |
| 10 Risks | Medium | Legal points need professional confirmation |

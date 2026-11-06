# 12-Month Learning Plan: Solo AI Founder (Trade & Logistics Ops)

Companion to `one_person_ai_business_report.md`, Section 5.

**Time budget:** about 5 hours a week of structured learning. The rest is learning by doing: customer calls and building.

**Order of priority:**
1. Selling and customer discovery
2. Domain knowledge (trade and logistics)
3. Applied AI engineering
4. Distribution
5. Finance and legal

> **About prices:** prices and availability change. Items marked "check price" were not verified in this research run. Free resources come first.

---

## Month-by-month

| Month | Main focus | Learn (free first) | Hands-on project | Hours/week | Progress check |
|---|---|---|---|---|---|
| 1 | Customer discovery | *The Mom Test*, Rob Fitzpatrick (book, ~$10–20, check price). YC Startup School videos on talking to users (free) | 20 interviews with freight forwarders and customs brokers | 5 + calls | 20 interview notes. Top 3 pains ranked by cost |
| 2 | Trade basics | Incoterms 2020 summaries (ICC, free summaries). HS code basics. ICEGATE help docs (India customs, free). Dubai Customs / Dubai Trade guides (free) | Map one shipment's full document flow end to end | 5 | Explain an import file to a forwarder without mistakes |
| 3 | Applied AI: document extraction | Model provider docs and cookbooks for vision/PDF extraction and structured outputs (free). DeepLearning.AI short courses (free) | Prototype: invoice + packing list → structured JSON | 6 | ≥85% field accuracy on 50 real documents |
| 4 | Evaluations | Free eval guides from AI practitioners (e.g., Hamel Husain's blog). Open-source eval tools' docs (Promptfoo, Langfuse). Optional paid course on AI evals (check price) | Build a 200-document eval set with expected fields | 5 | Accuracy and cost per document tracked automatically |
| 5 | Selling and pricing | YC Startup School on sales and pricing (free). Pricing teardown posts. Practise objection handling | Run a per-document vs per-branch pricing test with 5 prospects | 5 | 3+ paid pilots signed |
| 6 | Agents and tool use | Provider docs on tool use and agents (free). WhatsApp Business Platform docs (free) | Agent that requests missing documents over email and WhatsApp | 5 | 30% fewer manual follow-ups in pilots |
| 7 | Distribution | LinkedIn writing practice: study 10 top logistics voices. Newsletter basics | 2 posts a week + monthly newsletter about forwarding ops | 4 | 1,000 targeted followers. 5 inbound leads per month |
| 8 | Finance literacy | YC SAFE documents and explainers (free). Carta's guides on dilution and cap tables (free) | Model the cap table for pre-seed and seed | 4 | Can explain your dilution and runway in 2 minutes |
| 9 | Legal and compliance | India DPDP Act and Rules summaries (MeitY, free). DIFC Regulation 10 summaries. EU AI Act summaries (Commission site, free) | Write the DPA, privacy policy and human-approval workflow | 4 | DPA signed with all pilots |
| 10 | Reliability and cost control | Provider docs on caching, batching and model routing (free) | Cut cost per document by 30% with no loss of accuracy | 5 | Gross margin ≥ 70% |
| 11 | Fundraising | YC library on fundraising (free). Read 10 public pre-seed decks | Write the deck and data room. Monthly investor update | 5 | 10 investor meetings booked |
| 12 | Judgement and review | Re-read your interview notes and metrics. Founder retrospectives | Write a "what to stop doing" memo. Plan the next 12 months | 3 | Kill/keep decisions written for each feature and channel |

**Optional paid budget:** USD 200 (lean) to USD 3,000 (comfortable) a year. This matches `budgets_section7.csv`.

---

## Customer interview script (30 minutes)

Use with ops heads, documentation executives and owners of forwarding or customs-broking firms.

1. "Walk me through the last shipment file you handled, from first email to clearance."
2. "Which documents do you receive, and in what form? PDF, scans, photos on WhatsApp?"
3. "Where do you re-type the same data? Into which systems?"
4. "How long does one file take? How many files a month per person?"
5. "What was the last costly mistake? What did it cost (penalty, demurrage, a lost customer)?"
6. "What have you tried to fix this? Software, extra staff, outsourcing?"
7. "What do you pay today for software and data-entry staff?"
8. "If this took half the time, who would decide to buy it, and how?"
9. "Can you share 5 anonymised sample files?"
10. "Can I come back in 3 weeks with a prototype? If it works, would you pay for a pilot?"

**Rules (from *The Mom Test*):**
- Ask about past behaviour, not opinions.
- Never pitch in the first 20 minutes.
- Treat a "yes" without money or time committed as a "no."

---

## Ways to build domain expertise fast

- **Spend 1–2 weeks at a forwarder's documentation desk.** Offer free help in exchange for learning.
- **Join an industry association** and attend its events in India and Dubai:
  - FFFAI and local customs broker associations in India
  - Dubai Chamber logistics events
- **Recruit one advisor:** an ex-ops head, for 0.25–1% equity with 2-year vesting.
- **Read public sources:** customs tariff schedules and trade-portal documentation (ICEGATE, Dubai Trade).
- **Use pilots as paid learning.** Charge something from the first pilot.

---

## Skills to deprioritise (losing value because of AI)

- Hand-coding boilerplate
- Training models from scratch
- Generic content writing
- Collecting framework certificates
- No-code tricks as a core skill

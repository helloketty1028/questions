# Fact Update Proposal — input for Resume Project (Career & Resume)

**From:** Interview Bank · `prompts/05_Import_Legacy.md` · batch `inbox/2026-10-25_old-qa/` · **sub-batch B (Singtel)** · 2026-10-26
**Baseline actually read:** local `master\v2.0-draft\` — 03 v4.1 · 02 v3.1 · fact-check v2.4 · skills inventory v2.3
**Nothing below has been written to `resumes\`.** Sources: `Singtel_BCC…HR初筛面试准备_2026-10-19.docx` (#13), `…-1.docx` (#14), `10月23日 1329 B1录音` transcript (#21).
**Related earlier file:** `prep/_story-build/Fact_Update_Proposal.md` (IB-01 – IB-16). SB-04 below would close IB-01; SB-01 would strengthen S-009 / S-010.
**Later sub-batches (A / C / D) will append to this file.**

## A. New facts — not in 03 / 02

| Temp ID | Type | Related ID | Statement | Source | Proposed icon | Target § | Used in (Interview Bank) |
|---|---|---|---|---|---|---|---|
| SB-01 ✅ **applied → 03 v4.2 PA-03.5 (2026-10-26)** | ADD | PA-03, X-06 | For each production change, personally prepares the change request (raised as a CRQ in the bank's change-management system) and presents it at the CAB meeting | #13 [CONF 2026-10-19] | ✅ | 03 PA-03 | A-Q0010 |
| SB-02 | ADD | X-06 | Handles ad-hoc / urgent changes after P1 and P2 incidents: checks production logs and the database to confirm whether the issue is in his system; if so, or unclear, brings in the architect and other stakeholders to find the root cause and agree the fix; ships it as an urgent change | #13 [CONF 2026-10-19] | ✅ | 03 X-06 | A-Q0007 |
| SB-03 | ADD | PA-01 | The ISO 20022 programme had no formal performance-test (PET) phase and no pre-production rehearsal; testing simulated sending messages and receiving success and failure responses for each path | #13 [CONF 2026-10-19] | ✅ | 03 PA-01 §6 | A-Q0013 |
| SB-04 ⏳ **still open — not in 03 v4.2** | ADD | X-06, PA-02 (closes IB-01) | P1-type incident: a payment stuck in "pending in process". Splunk logs and payment records showed it was initiated and sent downstream, but the hub never received the response; downstream confirmed the payment was processed; the response was blocked in the messaging channel back to the hub. Containment: downstream team cleared the blocked messages and the affected payments recovered. Permanent fix: messaging channel optimised — **owner open (we vs channel team)**. No rollback involved | #13 [CONF 2026-10-19] | ✅ (owner of fix ❓) | 03 X-06 | A-Q0017; future S-029 |
| SB-05 | ADD | 02 §1 | **Notice period: one month — standard answer from now on [CONF 2026-10-26]**; the "about 2 weeks" offer made on 2026-10-23 is withdrawn | #13 [CONF 2026-10-19]; #21 | ✅ | 02 §1 | A-Q0003 |
| SB-06 | CLARIFY | 02 §2 / TL-3, §6.3 | Reason for leaving GBD (Jul 2022): caring for parents (health). External wording stays "family reasons" | #13 [CONF 2026-10-19] | ✅ | 02 §6.3 | A-Q0022 |
| SB-07 | CLARIFY | 02 §3 | PMP exam not yet scheduled (as of 2026-10-19) | #13 [CONF 2026-10-19] | ✅ | 02 §3 | A-Q0011 |
| SB-08 | ADD | X-02 | MVP-prioritisation practice, extra step: if the parties still cannot agree, present the trade-offs and seek a decision from the appropriate senior stakeholder | #14 only (no CONF marker) | ❓ | 03 X-02 | A-Q0014 |
| SB-09 | ADD / HOLD | PA-16 / PA-11 / PA-18? | "In internet companies, I led tech and infra team for website environment build" | #13 (no source, no CONF) | ❓ | — | A-Q0026 (removed) |
| SB-10 | CLARIFY | skills OQ-3.8 | Oracle used at UOB (payment records checked "in Oracle") — Oracle currently has no employer anchor | #13 | ❓ | skills inventory | A-Q0017 (removed) |
| SB-11 | ADD | PA-03, PA-02 | Release practice: deploy the package and config to the standby environment and verify it first; brief the production-support side on what's changing; prepare rollout and rollback plans; Splunk and server monitoring after go-live | #21 (spoken, 2026-10-23) | ❓ | 03 PA-03 | A-Q0013 |
| SB-12 | CLARIFY | X-02, X-05 (resolves SC-01) | **UOB's technical team engineers come from the four IT service vendors.** Affects how "lead 25 engineers", "1:1s, mentoring and performance management" and "vendor governance" are worded | Wilson in Interview Bank session [CONF 2026-10-26] | ✅ | 03 X-02, X-05, §0A row 2 | A-Q0001, A-Q0008, A-Q0020 |

## B. Conflicts — things said or written that disagree with 03

| Temp ID | Type | Related ID | Said / written | 03 says | Handling in Interview Bank |
|---|---|---|---|---|---|
| SC-01 | CONFLICT → see SB-12 | X-02, X-05 | "lead two app teams which are from 4 tech vendors" (#13 Q1) | 25 onshore/offshore engineers; separately chairs governance of 4 vendors | Old wording not used until SB-12 is applied |
| SC-02 | CONFLICT | PA-01.1, §0A | "went live 2 months ahead of the deadline" (spoken, #21) | MX-rich May and Aug 2025 vs SWIFT Nov 2025; "2 months ahead of plan" belongs to **Baidu** (PA-17.1) | Trap note in Q-0007 / A-Q0007 |
| SC-03 | CONFLICT | PA-02.3, CF-N3 | "our … team is the production support team" (spoken, #21) | No separate SRE / production-support team; his teams own production support | Trap note in Q-0013 / A-Q0013. Possibly an ops / L1 desk exists alongside — please clarify |
| SC-04 | CONFLICT | PA-05, PA-01, PA-11.2 | "customer relationship management and cross-border payment platforms with trans & reconciliation functions" (#14 Q9) | Customer-360 ≠ CRM; the hub does initiation/validation/enrichment/status, not reconciliation; reconciliation evidence = VV (PA-11.2) | A-Q0009 uses the corrected bridges |

## C. Internal names said aloud in interviews (no fact change — for awareness)
- #21: the internal platform name was said aloud ("CW") and an internal server-environment name was used. Interview Bank answers say "our payment-initiation platform / hub".

## D. Resolved in Interview Bank (no Resume Project action needed)
- 2026-10-26: "OK with after-hours releases" (A-Q0012) and "no location constraint — anywhere in Singapore" (A-Q0024) confirmed by Wilson. Preferences, not career facts.

---

# Sub-batch A (JPM) — 2026-10-26
**Sources:** #1 `14 questions.docx` · #2 `JPMC_Lead_SWE_Post_Trade_Interview_Prep-1.docx` · #3 `JP-interview-trade off- analysis.docx` · #4 `previous…/JP tradeoff interview questions.docx` · #5 `JPM_First_Round_Interview_analysis.docx` · #6 `Q9 — Outbox Saga Consistency.docx` · #17 `6月18日 JP Morgan 技术面试.txt` (spoken, 2026-06-18)
**Baseline:** 03 v4.2 · 02 v3.1 · fact-check v2.5

## E. New facts

| Temp ID | Type | Related ID | Statement | Source | Proposed icon | Target § | Used in (Interview Bank) |
|---|---|---|---|---|---|---|---|
| **SA-01** | ADD | PA-01 (§2, §6), PA-01.2 | Payment-initiation hub design: (a) every payment carries a **unique business reference enforced in the database**, plus an **explicit state machine**, so retries never create duplicates; (b) **reference data replicated locally / managed**, keeping source systems off the critical path (trade-off: freshness); (c) **asynchronous hand-off downstream with retry and an exception queue**; on a timeout, **check downstream status before resending**; (d) runs on Java / Spring Boot with DB and **MQ** | #4 Q4, #1 Q4 · **[CONF 2026-10-26] Wilson: "是真实情况"** | ✅ | 03 PA-01 §2 / §6 + new safe-wording row | A-Q0029, A-Q0036 (parked blocks 【SA-01 入库后启用】) |
| **SA-03** | ADD | PA-07 | AI code-review service controls: agent runs in an **isolated, read-only environment with no outbound network access**; code **never leaves the bank's network**; **model endpoint in-region**; **prompts and outputs fully logged**; review rules kept in the repository under normal change approval; **rejection rate tracked; false-positive suppression** | #1 Q3, #4 Q3 (+ follow-ups) · **[CONF 2026-10-26] Wilson: "是真实情况"** | ✅ (please confirm each sub-point when applying — "rejection-rate tracking" and "false-positive suppression" are the least specific) | 03 PA-07 §3–§6 | A-Q0030, A-Q0032 (parked) |
| SA-04 | CLARIFY | PA-07, C4 | Rollout: started with one squad/team, tuned prompts to reduce unnecessary findings, then expanded; other squads asked for it | #1, #2, #4 | ❓ (C4 adoption scope still open) | 03 PA-07, §6.2 C4 | A-Q0030 (parked) |
| SA-11 | ADD | 02 §6.1 / skills | UOB environment is mainly private (not public cloud); hands-on AWS comes from GBD / VV | #2 Q12 | ❓ | skills inventory | A-Q0039 (not used) |
| SA-13 | ADD | PA-03 | A "BAU" environment with production-like data exists; GenAI used to generate test data | #17 (spoken) | ❓ | — | A-Q0037 (not used) |
| SA-14 | ADD | PA-21 / skills OQ-3.8 | Outside work, built a Spring AI architecture locally and on AWS | #17 (spoken) | ❓ | PA-21 / skills | A-Q0028 (not used) |
| SA-17 | ADD | X-06 | Legacy application produced production incidents almost every month | #17 (spoken) | ❓ | X-06 | A-Q0017 (not used) |

## F. Conflicts / risky wording

| Temp ID | Type | Related ID | Said / written | 03 says | Handling |
|---|---|---|---|---|---|
| SA-02 | CONFLICT | PA-01, CF-N4 | Hub does **routing** (rail and correspondent bank), **KYC** enrichment, **compliance validation**, a duplicate-check service and a SWIFT gateway service (#2 Q5, #5) | Hub = initiation, validation, enrichment (FX, account, customer), authorisation, pain.002 status tracking; processing / settlement outside | Not used; trap in Q-0029. Please confirm whether any of these are actually in the hub |
| SA-05 | CONFLICT | PA-07.3 | "review quality went up around 80% by our internal measure" (#2 Q3) | Senior **review time** cut by an **estimated** ~80% | Corrected in A-Q0030 |
| SA-06 | CONFLICT | X-02, §0A | "I currently lead a team of around 10 engineers" (#4 Q1, 2026-10-09) | 25 (15 + 10) | Not used. Was this the CCD team only? |
| SA-07 | NUMBER | §0A | "around ten years in large tech companies… serving millions of users" (#4 Q1) | Not in §0A | Not used |
| SA-08 | CONFIDENTIAL | 01 §7 / rule 12 | "It handles around millions of payments a day" (#4 Q4) | UOB volumes never external | Not used; trap in Q-0029 |
| SA-09 | CONFLICT | PA-01.1 | "We migrated data in batches over several weekends, validated with a small volume of real transactions, then switched over in a planned maintenance window" (#2 Q10) | Phased Blue/Green-style coexistence; MX-rich May / Aug 2025; coexistence retired Aug 2026 | Not used. If a data-migration-by-weekends step really happened inside the coexistence plan, please add it to PA-01 |
| SA-10 | CLARIFY | skills OQ-3.8 (= SB-10) | "In banking my main database has been Oracle" (#2 Q11; #4 Q7) | Oracle has no employer anchor | Not used |
| SA-12 | CONFLICT | PA-01 §3 | Spoken (#17): UOB uses Kafka / Redis to reduce access time; "UOB has a separate team managing Kafka"; an SFTP-type gateway; OpenAPI web services | UOB stack = Java, Spring Boot, Apache Camel, event-driven integration; Kafka / Redis anchored at VV / AI Park | Not used for UOB. Please confirm UOB's actual messaging (MQ? Kafka?) — relates to SA-01(d) |
| SA-15 | SENSITIVE | — | Spoken (#17): "budget reduced every year; my vendor team will be almost zero once the project closes; no new projects" | — | Trap in Q-0004 / A-Q0004: never use this framing |
| SA-16 | WORDING | PA-11, PA-10 | "Before UOB I worked in the e-commerce & payment-gateway industry" (#1 Q9.1) | VV payment subsystem; GBD multi-channel payments — no "payment gateway" | Not used |
| SA-18 | UNVERIFIED | — | Incident example "payment delay → DB connection-pool misconfiguration → pool governance → automated detection script" (#5) | Not in 03 — looks like a template example | Not used unless real |

## G. Internal names
- #1, #4, #5 use **CEW** throughout; #4 Q1 calls C360 "customer relationship management" (= SC-04). Interview Bank answers use "payment-initiation hub" / "customer-360 platform".

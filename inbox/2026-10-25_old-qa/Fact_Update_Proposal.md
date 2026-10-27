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
| SB-05 | ADD | 02 §1 | **Contractual notice: two months. Wilson is currently in the resignation process, so availability ≈ one month after offer [CONF 2026-10-26, SD-08]**; the "about 2 weeks" offer made on 2026-10-23 is withdrawn | #13 [CONF 2026-10-19]; #21 | ✅ | 02 §1 | A-Q0003 |
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

---

# Sub-batch C (IFS) — 2026-10-26
**Sources:** #7 `IFS_模拟面试复盘_口语优化版_v7.docx` (finalised 2026-09-29) · #8 `Q2_WhyIFS_WhyLeave_优化版.docx` · #9 `previous…/interview of IFS Capital.docx` (2026-09-20/21) · #10 `previous…/HR questions.docx` · #11 / #12 (identical files, "lean team")
**Baseline:** 03 v4.2 · 02 v3.1 · fact-check v2.5

## H. New facts

| Temp ID | Type | Related ID | Statement | Source | Proposed icon | Target § | Used in |
|---|---|---|---|---|---|---|---|
| **SI-01** | ADD | PA-11 (new sub-ID); closes **IB-04** | At VV Technology, **a lead who ran several teams, including the big-data team** [CONF 2026-10-26, SD-16], underperformed: gaps in planning and upward reporting, brought personal emotion into the team; his team blocked the project (business analysts waited for technical support for months); people disengaged and some left. Wilson gave facts, agreed clear goals and a review period with real support; goals not met → let him go; team moving again within weeks | #7 HRD Q1 (Wilson's own story, finalised 9/29) · **[CONF 2026-10-26] "是真实情况"** | ✅ | 03 PA-11 | A-Q0052 (parked block); future story |
| **SI-02** | ADD | PA-11, PA-11.2 | VV-Life 0-to-1 approach: product and operations teams ran market research before building; small MVP; small steps; **every new feature behind a toggle** (pull back in minutes); architecture designed for iteration; some features missed and were fixed from feedback; core model worked and users stayed. Web + mobile APIs + backend on AWS; CI/CD and Splunk monitoring | #7 Q6, #9 CEO Q2 · **[CONF 2026-10-26] "是真实情况"** | ✅ | 03 PA-11 §6–§7 | A-Q0048 (parked) |
| **SI-03** | ADD | PA-01 §6 | During MT/MX **coexistence, both sides (MT and MX) were reconciled** — mandatory, otherwise mismatched records could not be explained in compliance reporting. **Open: which team ran it and at which stage** (03 CF-N4 says the hub itself does not reconcile) | #7 Q8 follow-up, #9 CEO Q5 · **[CONF 2026-10-26]** (owner ❓) | ✅ fact / ❓ owner | 03 PA-01 §6 | A-Q0037, A-Q0051 (parked) |
| SI-04 | ADD | X-02 | People practice: hire for the gap not the title; assign goal, deadline and boundary; regular 1:1s, early feedback; argue for fair pay; technical mentoring; **helped squad leads grow into managers** | #7 HRD Q7 | ❓ (last point especially) | 03 X-02 | A-Q0054 (not used) |
| SI-05 | ADD | X-05 | Vendor practice: interview embedded vendor staff like hires; customer data stays in-house; contracts cover source-code ownership, documentation, exit clause, audit rights; track defects at delivery, repeat defects and production stability; daily stand-ups and weekly reviews with vendor teams | #7 JD-2 | ❓ | 03 X-05 | A-Q0020 (method only) |
| SI-06 | ADD | X-02 | BAU vs project backlog reviewed with the business every two weeks | #7 JD-1 | ❓ | 03 X-02 | A-Q0058 (generalised) |
| SI-07 | CLARIFY | PA-01 §3, skills | UOB tech list: Spring Boot ✅, Spring Batch ✅, Camel ✅, Linux ✅ — plus **shell, FTP, Kafka, gateway, Oracle, MySQL, Redis, MongoDB, Axway, OAuth/JWT, Spark/Hadoop, RAG / vector DB** (no anchors) | #9 Q3 | ❓ | skills inventory; 03 PA-01 §3 | A-Q0062 (only anchored items) |
| SI-09 | ADD | PA-07 / X-04 | "AI writes the first pass on code and tests, so engineers review instead of type" — team practice? | #7 Q4 | ❓ | 03 PA-07 | A-Q0049 (not used) |

## I. Conflicts / held numbers (from #7 Appendix A "five core numbers" and #8 / #9)

| Temp ID | Type | Said / written | 03 says | Handling |
|---|---|---|---|---|
| SI-08 | WORDING | "built customer-facing super-apps and data platforms" (#8) | VV-Life local-life platform (PA-11); data platform PA-12 ⚠️ | Not used |
| SI-10 | CONFLICT (= SA-06) | "I lead a team of about ten engineers at UOB" (#7 Q1, App. A) | 25 (15 + 10) | Not used |
| SI-11 | HELD (HR-3 / HR-9) | "I've led teams of over a hundred engineers"; "built a team of 100+" (#7 HRD Q7, App. A; #9 Q5/Q6/CEO Q3) | VV 140 = total headcount, pending OQ-2.3 / B1 | Not used |
| SI-12 | HELD (CF-11 / IB-09) | GBD "one platform covering payments and KYC across 200-plus regions" (#7 Q2/Q7, App. A; #8; #9 CEO Q6) | "regions" = live-usage claim; §0A row ⚠️ | Not used; "designed for multi-country coverage" |
| SI-13 | HELD (§0A ⛔) | "A lean team handled millions of transactions a day"; "VV-Life grew to millions of transactions a day across several regions" (#7 App. A; #9 CEO Q2/Q3) | "multi-million daily transactions" ⛔ hold | Not used |
| SI-14 | HELD (HR-10) | "AI Park covered 1,000+ car parks" (#9 CEO Q3) | ⛔ | Not used |
| SI-15 | PROHIBITED (HR-1) | "18 years spanning **CTO**, Architect and PM roles" (#9 Q4) | No CTO title | Not used; trap in Q-0063 |
| SI-16 | CONFLICT | Weakness: "no lending product experience"; experience incl. "quantitative trading" (#9 Q5) | PA-04 retail unsecured lending servicing + collections; PA-20 ⛔ | Not used |
| SI-17 | CONFLICT (= SA-05, C3) | "review quality / efficiency +80% on our internal measure"; "new joiners 30–40% faster" (#7 Q3, App. A; #9 CEO Q1) | Senior review **time** cut by an **estimated** ~80%; C3 open | Corrected |
| SI-18 | OWNERSHIP | "My team built an AI-assisted code-review service" (#9 CEO Q1) | O1 + O2 — Wilson designed and built it | Corrected to "I built" |
| SI-19 | WORDING | "In a big bank, getting AI into production takes years of approvals" (#7 Q5) | PA-07 went live May 2026 after formal approval | Reworded in A-Q0008 |
| SI-20 | CONFLICT (= SC-04) | C360 = "regional customer relationship management" (#7 Q1, #9 Q1) | Customer-360 platform | Not used |

## J. Not stored (by design)
- Salary figures and floor (#7 HRD Q5) — personal; strategy only.
- IFS company specifics and interviewer names (CEO / HRD), brands, markets — application prep material, not career facts.

---

# Sub-batch D (general + other interviews) — 2026-10-26
**Sources:** D1 transcripts — #16 Visa recruiter (2026-05-13) · #18 Cloudera screen (2026-07-10) · #19 BoA tech (2026-07-21) · #20 SGX tech (2026-08-11) · D2 — #15 `previous…/questionaires.docx` (internal cards-transfer script skipped by decision)
**Baseline:** 03 v4.2 · 02 v3.1 · fact-check v2.5

## K. New facts

| Temp ID | Type | Related ID | Statement | Source | Proposed icon | Target § | Used in |
|---|---|---|---|---|---|---|---|
| **SD-01** | ADD | X-02 (closes **IB-03**) | Conflict: offshore developers in India and Singapore business users clashed because requirements changed often and expectations were unclear. Wilson introduced a requirement-clarification workshop before each sprint (BA, dev lead, QA, business users) to agree acceptance criteria and scope, plus a change-impact assessment for late changes. Escalations fell, trust improved, sprint delivery became more stable | #15 Q2 · **[CONF 2026-10-26] "真实事件"** | ✅ | 03 X-02 / PA-01 | A-Q0014 (parked); future story |
| **SD-02** | ADD | X-06 | Incident command practice: single point of coordination in the first 15 minutes; war-room channel; hold-or-fail-over decision within 10 minutes; engineers assigned to logs / database and messaging / downstream; hourly sync; first stakeholder update within 30 minutes, then hourly; DevOps or security pulled in if not resolved within an hour; high-severity issues resolved within half a day; blameless postmortem within 48 hours | #15 · **[CONF 2026-10-26]** | ✅ | 03 X-06 | A-Q0017 (parked) |
| SD-03 | ADD | PA-07 / PA-08 | Used AI to refactor legacy middleware code (extracting repeated patterns into reusable APIs); prototyped automated test generation from user stories | #15 | ❓ | 03 PA-07 / new | A-Q0076 (parked) |
| SD-04 | ADD | PA-07 | Researched inward / outward ISO 20022 payment flows and reports; proposed AI-agent ideas to his manager (2025); department formed an AI team from May 2026 — Wilson is a member and writes code | #20 SGX (spoken) | ❓ | 03 PA-07 | A-Q0072 (not used) |
| **SD-05** | ADD | X-01, PA-01 | Data migration included **entitlement data** — users, companies, groups, roles (a user can belong to several groups across companies); each batch approved in the old system → exported as JSON → validated record by record on the new side against related applications (user accounts, remittance) → loaded by Spring Batch jobs. #15 also: the hub supported migration of payment data and entitlement data from legacy | #20 SGX, #15 · **[CONF 2026-10-26] "真实事件"** | ✅ | 03 X-01 / PA-01 | A-Q0073 (parked) |
| SD-06 | ADD | X-02 | Two squads, each with a squad lead; daily stand-up 20–30 min; two-week sprints; retrospectives | #19 BoA (spoken) | ❓ | 03 X-02 | A-Q0069 (generic) |
| SD-07 | CLARIFY (→ IB-11) | PA-03.2 | "JUnit coverage at least 90% / 90+%"; third-party company produces penetration-test reports; Jenkins deploys JAR; Aldon (Rocket) manages packages | #19 BoA (spoken) | ❓ | 03 PA-03 | A-Q0068 (number not used) |

## L. Conflicts / risky wording

| Temp ID | Type | Said / written | 03 / 02 says | Handling |
|---|---|---|---|---|
| SD-08 | RESOLVED | Notice "2 months, can reduce to 1" (Visa, Cloudera) | — | Contract 2 months; resigning; ≈1 month → SB-05 updated |
| SD-09 | CONFLICT | "Moved to Singapore 6 years ago" (Cloudera, 2026-07) | VV Technology (Singapore) from Apr 2019 | Use the real year |
| SD-10 | CONFLICT + positioning rule | "I started my career as a (big) data engineer, about two years" (BoA, SGX) | 02: Renren Senior R&D Engineer 2008–12; standing rule: not positioned as a big-data engineer | Not used |
| **SD-11** | **HIGH RISK** (PA-20 ⛔, TL-4, OQ-1.8) | Cloudera saw the Pureland consultant role on LinkedIn; Wilson said he still consults and would stop on joining | Disclosure plan not decided | **Decide in Resume Project before next interview:** still active? disclosed to / approved by UOB? LinkedIn / resume alignment. Q-0066 has a template only |
| SD-12 | PROHIBITED / CONFLICT | #15 post-interview intro (SCB WRB, 2026-08-28): "technical architect" as title; hub does "routing" (SA-02); Pureland "VWAP… OTC-adjacent" advisory (⛔ PA-20); "one served over ten million daily users" (⛔ FU-1); "Flink-based real-time profiling with causal inference" (⚠️ CF-07); "GenAI code-review agent using Spring AI" (03: Spring Boot + headless Claude Code) | — | Not used |
| SD-13 | CONFLICT | #15 intro: VV "100+ tech team" (HR-3); "due to Covid the companies moved to China" (02: CEO moved team; Wilson stayed for family); "angel round to Series B & C"; C360 customers = "small & middle merchant clients" (PA-05: wealth cross-sell & client management); "Java/Python" strengths (Python unanchored) | — | Not used |
| SD-14 | NUMBER (X-04 rule) | "roughly half of my time is technical" (#15); "half" (SGX) | X-04: never claim a coding-time share | Trap added |
| SD-15 | NUMBER / WORDING | "UOB IT department has 3000+ employees"; "UOB is still a local bank" (#15) | Not in 03; inaccurate / disparaging | Not used |
| SD-16 | RESOLVED | SI-01 person: "team leader" (#7) vs "big-data team lead" (#15) | — | [CONF 2026-10-26]: a lead of several teams incl. the big-data team → SI-01 updated |
| SD-17 | NUMBER | "That eliminates 60% of causes" (#15 latency) | Invented statistic | Not used |
| SD-18 | CLARIFY (→ SI-07) | UOB uses an SSL hardware gateway and Axway API gateway with JWT (BoA, spoken) | No anchor | Not used |
| SD-19 | CONFLICT | Baidu high-concurrency system on Spring Cloud with Redis and Kafka (Cloudera, spoken) | PA-17: Dubbo, Resin, MongoDB, Redis, ZooKeeper, Solr | Not used |

## M. Not stored (by design)
- Salary figures (Visa, Cloudera); citizenship plans and remarks about other countries / age (Cloudera); personal relationship behind the Pureland role (Cloudera).

## N. Decision 2026-10-26 — Pureland (resolves SD-11, OQ-1.8, TL-4)

| Temp ID | Type | Related ID | Decision / statement | Source | Target § |
|---|---|---|---|---|---|
| **SD-20** | **REMOVE + CLARIFY** | PA-20, 02 §2 row 2, 02 §6.2, TL-4, OQ-1.8, SD-11 | **Remove Pureland Holding (Jewelake) from the work history.** The advisory arrangement **ended before Wilson joined UOB (Oct 2022)**; no outside work now. LinkedIn / resume alignment: **not now** (Wilson's decision). Note for the record: in the Cloudera screen (2026-07-10) Wilson said he was "still the consultant" — inconsistent with this decision; interview answer is "it ended before I joined UOB; my profile is out of date" | [CONF 2026-10-26] | 02 §2 (row 2 → end date before Oct 2022 or removed), §6.2; 03 PA-20 → retire; fact-check TL-4 / OQ-1.8 → close; 02 positioning |

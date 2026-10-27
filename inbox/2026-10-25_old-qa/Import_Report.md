# Import Report — inbox/2026-10-25_old-qa/

**Prompt:** `prompts/05_Import_Legacy.md` · **Fact source read:** 03 v4.1 · 02 v3.1 · fact-check v2.4 (local, unchanged since 2026-10-20)
**Original files:** read only — not modified, moved or deleted. docx converted to text in a session scratch folder outside the user's folders.

## 0. Batch plan and status

| Sub-batch | Sources (#) | Status | Q-IDs |
|---|---|---|---|
| **B Singtel** | #13, #14, #21 | ✅ imported 2026-10-26 | Q-0001 – Q-0027 |
| A JPM | #1 – #6, #17 | ✅ imported 2026-10-26 | Q-0028 – Q-0047 |
| C IFS | #7 – #12 | ✅ imported 2026-10-26 | Q-0048 – Q-0063 |
| D General + other interviews | #15, #16, #18 – #20 | ✅ imported 2026-10-26 (split D1 transcripts / D2 #15) | Q-0064 – Q-0079 |
| — | #22 WhatsApp audio (mp4) | ⏭ skipped (user decision 2026-10-26: no transcript) | — |

**Decisions (2026-10-26):** salary / notice / PR questions imported as strategy only — no salary figures stored · internal cards-team transfer script in #15 skipped, generic questions only · answers written with ATL / TPM / SM versions + industry angles (BNK incl. fintech / INT / TEL); admin questions share one version.

## 1. Sub-batch B — source → Q-ID mapping

★ = actually asked in the 2026-10-23 HR screen (#21) → `asked_at: "Singtel 2026-10 HR"`

| Original (#13 / #14 numbering) | Q-ID | ★ | Fact-check verdict | Answer handling | Closest old version |
|---|---|---|---|---|---|
| #Q1 Tell me about yourself | Q-0001 | | ✅ core · ⚠️ SC-01 · 🔒 "C360" | Rewritten (#14 base) | TPM |
| Q2 Current and expected salary | Q-0002 | ★ | 🔒 salary figures excluded | Strategy only | — |
| Q3 Notice period | Q-0003 | ★ | ❌ SB-05 | Placeholder | — |
| #Q4 Why leaving UOB | Q-0004 | ★ (follow-up "is the programme ending?") | ✅ | Reused (#14 final) + role versions | TPM |
| #Q5 Why Singtel / role | Q-0005 | | ✅ (external fact Singtel28 verified) | Reused (#14) + generic template | TPM |
| #Q6 Questions for me | Q-0006 | ★ | — | Reused; reverse list by round | — |
| Q7 Major and ad-hoc releases | Q-0007 | ★ (variant "most complex release") | ✅ PA-01.1/01.5 · ❌ SB-02 · ⚠️ SC-02 · 🔒 internal name said aloud | Rewritten | TPM |
| Q8 VP with 25 engineers — narrower role | Q-0008 | | ✅ X-02, X-05 | Reused (#14) | TPM |
| Q9 Telco / BSS / billing experience | Q-0009 | | ✅ PA-04.1, PA-05.3, PA-11.2 · ⚠️ SC-04 | Rewritten (#13 base) | TPM |
| Q10 CAB and change management | Q-0010 | | ❌ SB-01 | Rewritten — key sentence parked | TPM |
| Q11 PMP | Q-0011 | | ✅ 02 §3 · ❌ SB-07 | Reused | TPM |
| Q12 After-hours releases | Q-0012 | | ❓ never confirmed | Conditional draft | — |
| Q13 Release readiness | Q-0013 | ★ ("how did you ensure releases succeed") | ✅ · ❌ SB-03, SB-11 · ⚠️ SC-03 | Rewritten | TPM |
| Q14 Stakeholder conflict on release scope | Q-0014 | | ✅ X-02 · ❌ SB-08 | Rewritten (#14 STAR, escalation removed) | TPM |
| Q15 Citizen or PR | Q-0015 | ★ | ✅ 02 §1 | Reused | — |
| Q16 Strengths and weakness | Q-0016 | | ✅ | Reused + role versions | TPM |
| Q17 Release that went wrong | Q-0017 | | ❌ SB-04, SB-10 | Rewritten — case parked until 03 updated | TPM |
| Q18 Interviewing elsewhere | Q-0018 | ★ (stage / prioritise us) | — | Reused | — |
| Q19 3–5 years | Q-0019 | | — (aspiration) | Reused + role versions | TPM |
| Q20 Vendors | Q-0020 | | ✅ X-05, X-02 | Reused | TPM |
| Q21 Agile or Waterfall | Q-0021 | | ✅ PA-05, PA-01, PA-10 | Reused | TPM |
| Q22 Job changes | Q-0022 | | ✅ · ❌ SB-06 | Reused | TPM |
| Q23 Delivery tools | Q-0023 | | ✅ PA-03 §3, skills §11 | Reused | TPM |
| Q24 Location / arrangement | Q-0024 | | — | Placeholder | — |
| Q25 Gaps 2015 / 2022 | Q-0025 | | ✅ 02 TL-2/TL-3 | Reused | — |
| Q26 Network / infra teams | Q-0026 | | ✅ PA-02 · ❌ SB-09 | Rewritten (2nd sentence removed) | TPM |
| — (new in #21) Family members in the group | Q-0027 | ★ | — | New | — |
| Reverse questions 1–6 | inside A-Q0006 | | — | Reused | — |

**Totals (sub-batch B):** 27 new questions · 0 merged (bank was empty) · 3 sections discarded (below) · 27 answers, all `approved: []`.

## 2. Discarded in sub-batch B (and why)
| Item | Source | Reason |
|---|---|---|
| "JD × 你的证据" table and release-flow image | #13 | Belongs to a JD prep pack (`prep/<folder>`), not the question bank; no `resumes\applications\` folder exists for Singtel |
| Public salary data (Glassdoor / Indeed figures) | #13 Q2 | Dated market data; salary numbers not stored (decision 2026-10-26) |
| "旧版本表述的应对" table | #13 | Resume-version management; the risky claims it lists will become RISK questions via batch A/D and `prompts/02` |
| Probability chart / percentages | #13 | Heuristic estimates; Interview Bank uses `priority` P1–P3 instead |
| Salary and bonus figures, budget figures | #21 | Personal / sensitive; not stored |

## 3. Fact-check summary (sub-batch B)
- ❌ new-fact candidates: **SB-01 – SB-11**; SC-01 answered → **SB-12**. All in `Fact_Update_Proposal.md` (this folder).
- ⚠️ conflicts: **SC-01 – SC-04**.
- 🔢 numbers: SC-02 ("2 months ahead").
- 🔒 internal names: "C360" (written), internal platform name and server name (spoken, #21).
- Each answer lists its parked statements under **待确认**; none of them is in the answer text.

## 4. Stories missing / follow-ups
- Waiting for 03: CAB story (SB-01), urgent-change story (SB-02), pending-payment incident story (SB-04 → S-029).
- Cross-batch merges to check: Q-0008 ← IFS "VP2 with 18 years, why this role" (C) · Q-0017 ↔ JPM "production incident" (A) · Q-0014 ← "Tell me about a conflict" (D, #15).
- New domain note: `domain-notes/TEL_billing-charging.md`.

## 5. Change log
| Date | Change |
|---|---|
| 2026-10-26 | Answer length standard set by Wilson: 30s short version + **60s default** per role (ATL / TPM / SM); admin questions flexible. Template and `prompts/03` updated; all 27 answers' headings renamed to 60s; over-length sections trimmed and short ones extended using 03 facts only. |
| 2026-10-26 | 03 v4.1 → v4.2 (PA-03.5 CRQ / CAB). SB-01 applied: A-Q0010 rewritten; PA-03.5 added to A-Q0005, A-Q0007, A-Q0013, A-Q0016, A-Q0020, A-Q0021 and story S-009; all stories `facts_version` → "03 v4.2". SB-04 still not in 03 → A-Q0017 unchanged in substance. |
| 2026-10-26 | Wilson confirmed: notice period one month (A-Q0003); after-hours releases OK (A-Q0012); no location constraint (A-Q0024); weakness = a real gap chosen per role / industry (A-Q0016, selection table added). |

## 6. Sub-batch A (JPM) — 2026-10-26

**Sources:** #1 – #6, #17 · ★ = asked in the JPM 2026-06-18 technical screen (#17) → `asked_at: "JPM 2026-06 tech"`
**Totals:** 20 new questions (Q-0028 – Q-0047) · 6 merged into existing (variants / asked_at appended) · 20 new answers + 6 updated · 4 new domain notes · all `approved: []`.
**Decisions (2026-10-26):** allocation and tags approved; SA-01 and SA-03 confirmed true by Wilson (parked in answers as 【SA-0x 入库后启用】 until 03 includes them); Q-0029 trap: no volumes, no internal system names.

| Original (source) | Q-ID | ★ | Verdict | Handling |
|---|---|---|---|---|
| Role and responsibilities at UOB / Introduce yourself (#1, #2, #4, #17) | Q-0001 (merged) | ★ | ⚠️ SA-02, SA-06, SC-04 · 🔢 SA-07 | Pending items added |
| What are you looking for / why leave UOB (#2, #4, #17) | Q-0004 (merged) | ★ | ⚠️ SA-15 | ATL version replaced with your #4 wording |
| Why JPM / Post Trade (#2, #4) | Q-0005 (merged) | | ✅ external | BNK line added |
| Questions for me (#2, #17) | Q-0006 (merged) | ★ | — | JPM reverse questions + interviewer's answers |
| How do you test and deploy / QA team? (#17) | Q-0013 (merged) | ★ | ❌ SA-13 | Follow-ups added |
| Production support / recurring issue (#2, #17) | Q-0017 (merged) | ★ | ❌ SA-17 · ⚠️ SA-18 | Follow-ups added |
| How hands-on are you (#1, #2, #4, #17) | Q-0028 | ★ | ✅ X-04, PA-07.1 · ❌ SA-14 | New — ATL / SM |
| Walk me through your architecture (#1, #2, #4, #5, #17) | Q-0029 | ★ | ✅ PA-01.2/01.3 · ❌ SA-01 (parked) · ⚠️ SA-02 · 🔒 SA-08, CEW | New — ATL / TPM / SM |
| AI-assisted tools / adoption (#1, #2, #4) | Q-0030 | | ✅ PA-07 · ❌ SA-03 (parked), SA-04 · ⚠️ SA-05 | New |
| Validate AI-generated code (#1, #2, #4) | Q-0031 | | ✅ | New — ATL |
| Responsible AI / sensitive data (#1, #2, #4) | Q-0032 | | ✅ PA-07.2 · SA-03 parked | New — ATL / SM |
| Measure AI impact / resisters (#2) | Q-0033 | | ✅ PA-07.3 | New — SM / ATL |
| Post-trade knowledge (#1, #2, #4) | Q-0034 | | transferable · SA-16 | New |
| Kafka two services one topic (#1, #2, #4, #5, #17) | Q-0035 | ★ | ✅ PA-11.4/16.4 · ⚠️ SA-12 | New — ATL |
| Consistency / duplicates (#2, #4, #5, #6) | Q-0036 | | ✅ PA-11.2 · SA-01 parked | New — ATL |
| Release safely / test what UAT can't (#2, #4, #17) | Q-0037 | ★ | ✅ PA-01.1, PA-03.5 · ⚠️ SA-09 · ❌ SA-13 | New — ATL / TPM |
| MongoDB (#1, #2, #4) | Q-0038 | | ✅ PA-17/18/16 stack · ⚠️ SA-10 | New — ATL |
| AWS / resilience (#2, #3, #4) | Q-0039 | | ✅ PA-10.1/10.3, PA-11.1 · ❌ SA-11 | New — ATL |
| Settlement / reconciliation design (#1, #2, #4) | Q-0040 | | ✅ PA-11.2 | New — ATL |
| Vendor / start-up evaluation (#2, #3, #4) | Q-0041 | | ✅ X-02, X-05 | New — SM / TPM / ATL |
| Technical disagreement (#2, #3, #4) | Q-0042 | | ❌ no story (IB-03) | Skeleton only, `variants: []` |
| Mentoring / raise the bar (#2, #3, #4) | Q-0043 | | ✅ X-04, X-02, PA-03 | New — ATL / SM |
| Latency / performance (#2, #17) | Q-0044 | ★ | ✅ PA-01.4 (no figure) · ⚠️ SA-12 | New — ATL |
| Distributed caching / Redis (#17) | Q-0045 | ★ | ✅ PA-11.4, PA-16.4, PA-18.1 | New — ATL |
| Live Java coding (#2, #3, #4) | Q-0046 | | — | Practice notes |
| "You interviewed with us in June — what's changed?" (#2) | Q-0047 | | — | New (placeholders) |
| HR: notice / salary / PR (#2 Q23) | → Q-0002 / Q-0003 / Q-0015 | | — | No change (already covered) |

**Discarded in sub-batch A:** #3 probability map, candidate scorecard and "5 main lines" analysis (meta-analysis; key points folded into question notes) · #5 template incident example (SA-18) · #2 "three rules on the day" (folded into Q-0028 note) · Kafka ASCII cluster diagram (#1) — covered by `domain-notes/COM_distributed-consistency.md`.
**New domain notes:** `BNK_post-trade.md` (T+1 dates verified) · `BNK_iso20022-reconciliation.md` · `COM_distributed-consistency.md` · `BNK_mas-incident-availability.md` (MAS Notice FSM-N03 verified).

## 7. Sub-batch C (IFS) — 2026-10-26

**Sources:** #7 (base), #8, #9 (earlier draft), #10 (subset of #7), #11 = #12 (identical). No interview transcript in this batch → no `asked_at`.
**Totals:** 16 new questions (Q-0048 – Q-0063) · 10 merged · 16 new answers + 10 updated · all `approved: []`.
**Decisions (2026-10-26):** allocation approved; SI-01 and SI-02 confirmed true (parked as 【SI-0x 入库后启用】); SI-03 confirmed (MT/MX reconciliation mandatory during coexistence) — owner open; domain note `BNK_compliance-flow.md` approved and created 2026-10-26 (one page; marks Wilson's hub boundary).

| Original (source) | Q-ID | Verdict | Handling |
|---|---|---|---|
| Introduce yourself + why this role (#7 Q1, #9 Q1) | Q-0001 (merged) | ⚠️ SI-10, SI-20 · 🔢 SA-07 | Pending items |
| Salary + lower level (#7 HRD Q5, #9 HRD Q6) | Q-0002 (merged) | 🔒 figures excluded | Three-step strategy added |
| Why leave UOB (#7 Q2, #8, #9 Q2/Q7) | Q-0004 (merged) | ✅ · SI-08 | Fintech line added |
| Why IFS (#7 Q2, #8) | Q-0005 (merged) | ⚠️ SI-12 | IFS example line |
| Reverse questions (#7 HRD Q6, #9) | Q-0006 (merged) | — | CEO / HRD questions added |
| VP2, why this level, how long (#7 Q5, #9 HRD Q1) | Q-0008 (merged) | ⚠️ SI-19 | SM version replaced with your #7 Q5 wording; counter-offer follow-up |
| Strengths / weakness (#9 Q5) | Q-0016 (merged) | ⚠️ SI-11, SI-16 · ⛔ PA-20 | Old answer discarded |
| Choose and manage outsourcing vendors (#7 JD-2) | Q-0020 (merged) | ❓ SI-05 | Follow-up (method) |
| AI project / real problem or piling on tech (#7 Q3, #9 CEO Q1) | Q-0030 (merged) | ⚠️ SI-17, SI-18 | Pending items |
| Risk control / stability during change (#9 CEO Q5, #7 Q8) | Q-0037 (merged) | ✅ · SI-03 parked | SM version added |
| Bet without enough data / 0→1 (#7 Q6, #9 CEO Q2) | Q-0048 | ✅ PA-11 · SI-02 parked · ⛔ SI-13 | New — SM / ATL |
| Lean team, no budget (#7 Q4, #9 CEO Q3, #11/#12) | Q-0049 | ✅ · ❓ SI-09 · ⚠️ SI-11, ⛔ SI-13 | New — SM |
| Five markets: standardise vs localise (#7 Q7, #9 CEO Q6) | Q-0050 | ✅ PA-10.1/10.2 · ⚠️ SI-12 | New — SM / ATL (old answer was struck out by you; rewritten) |
| Legacy system — what first (#7 Q8) | Q-0051 | ✅ PA-17.1, PA-01.1 · SI-03 | New — SM / ATL / TPM |
| Hard people decision (#7 HRD Q1, #9 HRD Q2, #10) | Q-0052 | SI-01 parked | New — SM / TPM |
| Leaner than a Tier-1 bank (#7 HRD Q2, #9 HRD Q3, #10) | Q-0053 | ✅ | New — SM |
| Hire / assign / appraise / keep (#7 HRD Q3+Q7, #9 HRD Q4, #10) | Q-0054 | ✅ X-02 · ❓ SI-04 · ⚠️ SI-11 · SB-12 | New — SM / TPM |
| Speed vs compliance (#7 HRD Q4, #9 HRD Q5, #10) | Q-0055 | ✅ PA-03, PA-07 | New — SM / TPM |
| Management style (#7 HRD Q8, #9 HRD Q7, #10) | Q-0056 | — | New — SM / TPM |
| Motivate people (#7 HRD Q9, #9 HRD Q8, #10) | Q-0057 | — | New — SM |
| BAU vs projects (#7 JD-1) | Q-0058 | ✅ X-06, X-02 · ❓ SI-06 | New — TPM / SM |
| Remote / hybrid team (#7 JD-3) | Q-0059 | ✅ X-02 | New — SM / TPM |
| Big bank → small company worries (#7 JD-4) | Q-0060 | ✅ PA-03 | New — SM |
| AI in lending / risk; data + AI and human connection (#7 Q3, #9 CEO Q4) | Q-0061 | ✅ PA-07.2 | New — SM / ATL |
| Technologies at UOB (#9 Q3) | Q-0062 | ✅ anchored items only · ❓ SI-07 | New — ATL |
| What can you bring / good fit (#9 Q4, Q6) | Q-0063 | ⛔ SI-15 · ⚠️ SI-11 | New — ATL / TPM / SM |

**Discarded in sub-batch C:** IFS company specifics and interviewer names/values (prep-pack material; no `applications\` folder for IFS) · #7 Appendix A "five core numbers" (see SI-10 – SI-17) · pronunciation tables and rescue phrases (#7 Appendix B / C / E — practice tools) · #9 "cross-interviewer alignment" notes (folded into question notes) · buy-vs-build vendor names kept only as external examples in A-Q0049.

## 8. Sub-batch D — 2026-10-26

Split to respect the 30-item limit: **D1** = transcripts #16 Visa, #18 Cloudera, #19 BoA, #20 SGX (20 items) · **D2** = #15 questionaires (16 items; internal cards-transfer script skipped).
**Totals:** 16 new questions (Q-0064 – Q-0079) · 15 existing questions updated (variants / asked_at / notes) · 16 new answers + 14 updated · new domain note `COM_incident-severity.md` · all `approved: []`.
**Decisions (2026-10-26):** allocation approved; SD-01, SD-02, SD-05 confirmed true (parked as 【SD-0x 入库后启用】); SD-08 notice = contract 2 months, resigning, ≈1 month; SD-16 = lead of several teams incl. big-data; severity note approved.
**asked_at added:** Visa 2026-05 recruiter · Cloudera 2026-07 screen · BoA 2026-07 tech · SGX 2026-08 tech.

| Original (source) | Q-ID | ★ | Verdict | Handling |
|---|---|---|---|---|
| Intro / current role (Visa, Cloudera, SGX; #15 ×5) | Q-0001 | ★ | ⚠️ SD-10, SD-12, SD-13 | Pending items |
| Salary (Visa, Cloudera) | Q-0002 | ★ | 🔒 | asked_at |
| Notice (Visa, Cloudera) | Q-0003 | ★ | SD-08 resolved | Answer rewritten (2-month contract, ≈1 month) |
| Motivation for change (Visa, Cloudera; #15) | Q-0004 | ★ | ⚠️ SD-15 | Industry lines + pending |
| Why this role (#15) | Q-0005 | | ✅ | variant |
| Questions for us (all four; #15) | Q-0006 | ★ | — | Interviewer answers recorded |
| Open to IC role (Cloudera) | Q-0008 | ★ | ✅ | Follow-up |
| Conflict at work (#15) | Q-0014 | | SD-01 parked | TPM STAR parked block |
| Status / sponsorship / when moved (Visa, Cloudera) | Q-0015 | ★ | ⚠️ SD-09 | Follow-ups |
| Strengths / weakness (#15) | Q-0016 | | ✅ · ⛔ quant | Pending note |
| Incident affecting payments — lead the team (#15) | Q-0017 | | SD-02 parked | TPM parked block |
| Hands-on / day-to-day / AI vs yourself (SGX, Visa; #15) | Q-0028 | ★ | 🔢 SD-14 | Follow-ups |
| AI project (Visa; #15 proud) | Q-0030 | ★ | ⚠️ Spring AI | Pending note |
| MongoDB vs Oracle (BoA) | Q-0038 | ★ | ⚠️ SA-10 | Follow-up answer |
| Latency investigation (#15) | Q-0044 | | 🔢 SD-17 | Follow-up |
| Highly scalable system (Visa) | Q-0064 | ★ | ✅ · ⚠️ SD-19 | New — ATL |
| Manager, architect or IC? (Visa, Cloudera) | Q-0065 | ★ | ✅ · ⚠️ SA-06 | New — ATL / TPM / SM |
| Outside consulting / conflict of interest (Cloudera) | Q-0066 | ★ | ⛔ SD-11 | **Template only** — decision needed |
| Data-platform engineering depth (Cloudera) | Q-0067 | ★ | gap | New — ATL |
| CI/CD pipeline (BoA) | Q-0068 | ★ | ✅ · ⚠️ SD-07 | New — ATL / TPM |
| Scrum team (BoA) | Q-0069 | ★ | ✅ · ❓ SD-06 | New — TPM |
| SQL with Java (BoA) | Q-0070 | ★ | ✅ 02 CF-N6 · ⚠️ SD-10 | New — ATL |
| Python vs Java concurrency (BoA) | Q-0071 | ★ | gap · SD-18 | New — ATL |
| Most proud of / main contribution (SGX; #15) | Q-0072 | ★ | ✅ · ❓ SD-04 | New — ATL / TPM / SM |
| Data migration (SGX) | Q-0073 | ★ | ✅ X-01 · SD-05 parked | New — ATL / TPM |
| Middleware design (#15) | Q-0074 | | ✅ design | New — ATL |
| Fixed deadline, scope won't fit (#15) | Q-0075 | | ✅ | New — TPM / SM |
| AI use cases beyond code review (#15) | Q-0076 | | ✅ PA-08 · SD-03 parked | New — SM / ATL |
| Pressure (#15) | Q-0077 | | ✅ | New — TPM / SM |
| How colleagues describe you (#15) | Q-0078 | | — | New — 30s only |
| Meeting deadlines on challenging projects (#15) | Q-0079 | | ✅ | New — TPM / SM |

**Discarded in sub-batch D:** #15 internal cards-transfer script (decision) · "银行零售支付数据中台架构设计方案" (design exercise; C360 facts already in PA-05) · empty Q17 / Q18 answers (#15) folded into Q-0017 / Q-0072 variants.

## 9. Batch closed — 2026-10-26
All sub-batches B, A, C, D imported. Bank now: **79 questions · 79 answers · 28 stories · 7 domain notes**. #22 (WhatsApp audio) skipped by decision. Fact-update candidates for Resume Project: SB-01 – SB-12, SC-01 – SC-04, SA-01 – SA-18, SI-01 – SI-20, SD-01 – SD-19 (see `Fact_Update_Proposal.md`).

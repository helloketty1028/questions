# Fact Update Proposal — input for Resume Project (Career & Resume)

**From:** Interview Bank · `prompts/01_Build_Stories.md`, scope = all · 2026-10-25
**Baseline actually read:** local `master\v2.0-draft\` — 03 v4.1 (2026-10-17) · 02 v3.1 (2026-10-17) · fact-check v2.4 (2026-10-20) · repo HEAD `6727187`
**Nothing below has been written to `resumes\`.** Interview Bank only reads the resume library. Please process these in the Career & Resume project through the usual fact-updates flow.
**Stories affected:** `stories/S-001` – `S-028` (status: draft). Each one points to these IDs in its Open questions.

## A. New statements from Wilson (this session)

| Temp ID | Type | Related ID | Current wording in 03 | Wilson's statement 2026-10-25 | Question to settle | Source | Target § |
|---|---|---|---|---|---|---|---|
| IB-11 | CLARIFY | PA-03.2, §0A "99% SonarQube coverage gate" | "99% SonarQube coverage gate" 📄 (❓ new-code vs overall) | "UOB's CI/CD pipeline uses SonarQube 100%" | Is this a different metric — SonarQube **used in 100% of pipelines** (adoption) vs a **coverage threshold**? If so, what is the coverage gate value, and does it apply to new code or overall? Is the 99% figure right? | [CONF 2026-10-25] | 03 §0A, PA-03 §8, PA-03.2 |
| IB-12 | CLARIFY | X-04, §0A "~50 code modules", C6 | "~50 code modules reviewed daily; ~20 core modules in depth"; scope CEW vs CEW+CCD ❓ C6 | "CEW has 50+ code components" | (a) "~50" → "50+"? (b) Scope = the payment-initiation hub only → closes the module part of C6. (c) Is "~20 core modules reviewed in depth" unchanged? External wording must stay "the payment-initiation hub" (no "CEW"). | [CONF 2026-10-25] | 03 §0A, X-04, §6.2 C6 |

## B. Evidence gaps — stories exist but are thin (please supply a sanitised fact if one exists)

| Temp ID | Type | Related ID | Gap | Stories / question types affected |
|---|---|---|---|---|
| IB-01 | ADD | X-06, PA-02 | No specific, **sanitised P1 incident**: timeline, root-cause type, workaround, permanent fix, what changed afterwards | S-008 · "worst incident", "walk me through a P1" |
| IB-02 | ADD | X-05 | No specific vendor performance issue and how it was resolved | S-013 · "a vendor issue you resolved" |
| IB-03 | ADD | PA-01 §6 (trade-off forums) | No specific **conflict or disagreement** event (architecture trade-off, business or vendor pushback) | No story yet · BEH high-frequency |
| IB-04 | ADD | X-02 (1:1s, mentoring, performance management) | No specific **people-management** event (underperformer, promotion, hiring, attrition) | S-012 · SM high-frequency |
| IB-05 | CLARIFY | PA-01.4, C7 | No latency figure; no root-cause detail; own part O1 vs O2; C7 concurrency-control module | S-004 |
| IB-06 | CLARIFY | PA-02.1, PA-02.2 | DR drill frequency, scope, RTO/RPO; MTTR before/after | S-006, S-007 |
| IB-07 | CLARIFY | PA-05.1, C5 | Cloudera: alternatives considered and evaluation criteria; C5 — led the 2022 launch or took over after Oct 2022 | S-015 |
| IB-08 | CLARIFY | PA-04, X-02, C6 | PA-04 technology, challenges and outcomes not recorded; which team owns lending / collections; one concrete instance of the two-line schedule conflict | S-011 · no standalone lending story possible |
| IB-13 | ADD | PA-17.1 | What was wrong with the Baidu project at takeover ("struggling" is in the Interview field but has no facts) | S-027 |
| IB-14 | ADD | PA-11.2 | VV reconciliation design detail (frequency, exception handling) | S-022 |
| IB-15 | CLARIFY | PA-07, C1–C4 | C1 defect wording; C2 R₀ (pre-service review rounds); C3 ramp-up measure; C4 remainder (all 25 users? own initiative?); noise / false-positive handling | S-016, S-017 |
| IB-16 | ADD | PA-01.1, PA-01.5 | Cutover-readiness gate criteria; any dependency near-miss on the CBPR+ critical path | S-001, S-003 |

## C. Internal conflicts in 03 (found while building stories)

| Temp ID | Type | Related ID | Version A | Version B | Interview Bank handling until resolved |
|---|---|---|---|---|---|
| IB-09 | CONFLICT | §0A vs PA-10.2 (CF-11) | §0A: "KYC supporting 200+ countries" ⚠️ | PA-10.2 safe wording uses "supporting 200+ countries" 📄 | Number not used (S-019) |
| IB-10 | CONFLICT | §0A vs PA-10.3 (OQ-2.3; earlier TU-04/B1) | §0A: "40-person project team" ✅ | PA-10.3: `{40-person — OQ-2.3}` ❓ slot | Number not used (S-020) |

## D. Notes for the index script (not fact changes)
- PA-15 (project row: "📄 cloud ⚠️") and PA-12 (⚠️) make any project-level reference fail validation. S-024 therefore cites only PA-15.1 / PA-15.2. Once CF-08 is settled, the PA-15 row icon can be updated.

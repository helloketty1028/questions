# Taxonomy — 分类代码

代码与简历库（`05_JD_Keyword_and_Matching_Rules.md` §2、`03_Achievement_Library.md` §1）保持一致，题库与简历库可以直接互相引用。新增代码时先改本文件，再改 `scripts/build_index.py` 里的 `TAX`。

## 1. 行业 `industry`（可多选）
| 代码 | 含义 | 与简历库的对应 |
|---|---|---|
| `BNK` | 银行 / Fintech / 金融基础设施（MAS、SGX 等） | lens BNK |
| `INT` | 互联网 / 电商 / SaaS / 消费科技 | lens INT |
| `TEL` | Telecom（运营商、BSS/OSS、计费） | 简历库无此 lens，默认 `evidence: transferable` |
| `COM` | 跨行业通用 | — |

## 2. 岗位 `role`（可多选）
| 代码 | 你的分类 | 典型职位 | 面试重点 |
|---|---|---|---|
| `ATL` | 技术专家 / 技术 Leader | Tech Lead、Principal Engineer、Solution / Payments Architect | 技术深度、架构取舍、故障排查、动手能力 |
| `TPM` | 项目经理 / Delivery Manager | Technical Delivery Manager、Programme Manager、Service Delivery | 计划、RAID、依赖、变更与发布治理、供应商与 SLA、汇报 |
| `SM` | 技术高管 | Head of Engineering / Technology、Director、CTO 级岗位 | 战略、组织、预算与投资、人才、治理、业务价值 |

> 注意：`SM` 指目标岗位的层级。个人经历中不把 "CTO" 说成曾任职位（03 §0）。

## 3. 题型 `qtype`（单选）
| 代码 | 含义 |
|---|---|
| `BEH` | 行为题（Tell me about a time…） |
| `DEEP` | 技术深挖（原理、实现、取舍） |
| `SYSDES` | 系统设计 |
| `SITU` | 情景假设题（What would you do if…） |
| `DOMAIN` | 行业知识（支付、清算、计费等） |
| `MOTIV` | 动机类（why leave / why us / career goal） |
| `RISK` | 简历高风险追问：简历里的说法会被质疑或深挖（如 03 §0A 标为 high interview risk 的项） |
| `REVERSE` | 我向面试官提的问题 |

## 4. 证据等级 `evidence`
| 值 | 含义 |
|---|---|
| `direct` | 03 中有直接证据（✅ / 📄） |
| `transferable` | 可迁移经验，必须明说是迁移，不能说成"做过" |
| `gap` | 没有经验，只能回答学习计划、相邻经验或思路 |

## 5. 优先级与状态
- `priority`：`P1` 高频、必须准备 · `P2` 常见 · `P3` 偶发
- 题目 `status`：`draft` · `active` · `retired`
- 故事 `status`：`draft` · `verified`（已对照 03 核实）· `retired`
- 答案：`variants` 列出已写的版本，`approved` 列出已经你审核通过的版本

## 6. 主题 `topics`（受控词表，可多选）
<!-- TOPICS:BEGIN -->
- 支付与金融：`payments` `iso20022` `rtgs` `settlement-recon` `lending-collections` `regulatory-trm` `core-banking`
- 稳定性：`resilience-dr` `incident-rca` `observability-sre` `security`
- 技术：`architecture` `system-design` `microservices` `data-platform` `high-concurrency` `cloud` `devops-quality` `ai-engineering` `ai-governance`
- 交付：`agile-delivery` `programme-governance` `risk-raid` `release-change` `vendor-sow` `estimation-planning`
- 管理：`stakeholder` `team-leadership` `hiring-talent` `org-building` `budget-investment` `strategy` `performance-mgmt` `offshore-teams`
- 行为：`conflict` `failure-learning` `influence` `decision-making` `motivation`
- 行业：`ecommerce-order` `saas-multitenant` `iot` `billing-charging` `oss-bss`
<!-- TOPICS:END -->

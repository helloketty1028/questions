# BNK — 银行支付合规链路（行业知识，不是个人事实）

**用途**：A-Q0029（架构，被追问"hub 在合规链里处于哪一环"）、A-Q0061（AI 在借贷 / 风控里的位置）、fintech / 借贷公司问"你懂不懂合规流程"。
**来源**：你的旧准备稿 #9（IFS，2026-09），按通用银行知识整理。**这是行业知识，不是你做过的事。**

## 1. 一笔跨境支付的合规链路
```
客户 ──► KYC / 客户风险评级
          │
          ▼
       发起支付 ◄══════ 【你的 hub：initiation · validation · enrichment · authorisation · status tracking】
          │
          ▼
       制裁筛查（Sanctions Screening，常接外部名单 / 服务商）
          │
          ▼
       AML / 交易监控
          │
          ▼
       风险评分 ──► 审批 / 调查（命中时人工处理）
          │
          ▼
       支付处理与清算结算（下游系统；SGD 大额 / RTGS 经 MEPS+，外币经代理行）
          │
          ▼
       审计留痕 / 监管报告
```
**一句话**：银行合规 = 客户合规（KYC）+ 交易合规（制裁、AML）+ 数据合规（保护、驻留）+ 流程合规（审批、变更、审计）+ 监管报告。

## 2. 你的边界（被追问时这样说）
| 环节 | 是不是你做的 | 依据 |
|---|---|---|
| 支付发起、校验、增强（FX、账户、客户参考数据）、授权、pain.002 状态跟踪 | **是** | 03 PA-01.2 / 01.3 / 01.7 |
| 安全控制（API 与数据库加密、凭证管理）、数据迁移 | **是** | 03 X-01 |
| 变更治理：每次生产发布的 CRQ 与 CAB | **是** | 03 PA-03.5 |
| 事故分析报告，**作为**银行向 MAS 报告的输入 | **是（只提供输入）** | 03 X-06 |
| KYC、制裁筛查、AML、风险评分、清算结算 | **不是**——由上下游系统或其他团队负责 | 03 CF-N4（hub 不做清算结算）；03 没有制裁 / AML 的记录 |

**安全说法**："My hub sits at the initiation point of that chain — it validates, enriches, authorises and tracks payments, and hands them downstream. Screening, AML and settlement are owned by other systems."
**不要说**：hub 做了制裁筛查 / AML / 清算结算；"cross-border payments settle via MEPS+"（CF-N7）。

## 3. 与其他 note 的关系
- 对账：`BNK_iso20022-reconciliation.md`
- 事故通报与可用性：`BNK_mas-incident-availability.md`

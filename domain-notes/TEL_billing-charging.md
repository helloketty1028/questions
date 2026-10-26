# TEL — Billing, Charging & BSS（行业知识，不是个人事实）

**用途**：Q-0005、Q-0009、Q-0026 等 TEL 题的背景知识。本文件只放外部事实，不放个人经历。
**核实日期**：2026-10-26。标"推断"的是观点，面试时要当作观点来说。

## 1. Telco billing 覆盖什么
```
用量记录（CDR / 计费数据记录，常由 mediation 预处理）
   └─► Rating：按套餐、资费、折扣、税定价
         └─► Charging：预付 = 实时扣费（余额低于阈值可限制服务）· 后付 = 通常按月出账
               └─► Invoicing：账单生成与投递、调账
                     └─► 财务：收款跟踪与匹配、credit 管理、debt collection（催收）、税
```
- **Convergent billing**：多种服务，一个账户、一张账单。
- 来源：[Wikipedia — Telecommunications billing](https://en.wikipedia.org/wiki/Telecommunications_billing)

## 2. BCC
- **BCC = Billing, Customer & Charging**。这是 Singtel Delivery Manager 岗（2026-10）所在 squad 的名称，来源是 JD 和 HR 初筛（10-23）的说法。
- HR 初筛描述的岗位日常：合并即将上线的计费系统变更、定发布范围和时间线；跟踪 SIT / UAT 等测试阶段；变更文档、风险评估和 CAB；协调业务、开发、网络、基础设施、运营和外部供应商；部署就绪和回滚预案；按月汇报发布状态。

## 3. Singtel28（2024-05-23 发布）
- 两个核心：**lifting business performance**（整合 Singtel Singapore 和 Optus 的消费者与企业业务；扩大 NCS、Nxera、Paragon 等增长引擎）和 **smart capital management**（资产回收，约 S$6 billion 的可变现资产储备）。
- 原文提到："simplifying product offerings to remove complexity for customers"，以及用 AI "to improve customer experiences"。
- 新闻稿**没有提到 IT 或计费系统**。"产品简化最终会落到计费系统"是**推断**。
- 来源：[Singtel 新闻稿（SGX 公告，2024-05-23）](https://links.sgx.com/1.0.0/corporate-announcements/02YS858QEAUJO0HK/804234_NR-20240523-LaunchingSingtel28.pdf) · [TelecomTV 转载](https://www.telecomtv.com/content/digital-platforms-services/launching-singtel28-a-new-growth-plan-50445/)

## 4. 和银行支付的类比（只能说"问题相似"，不能说"一样"）
| 支付（你的经验） | Telco billing | 你的证据 |
|---|---|---|
| 交易准确、可追溯、cut-off 窗口 | 计费准确、账期 | PA-01 |
| 下游状态回传处理 | 计费结果和账单状态 | PA-01.3 |
| 信用卡与贷款的贷后催收 | receivables / collections | PA-04.1 |
| 支付子系统对账 | 收款匹配、账务平衡 | PA-11.2（VV，不是 UOB） |
| Spring Batch 定时任务 | 账期批处理（bill run） | PA-05.2 |

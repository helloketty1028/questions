# BNK — Securities Post-Trade（行业知识，不是个人事实）

**用途**：Q-0034、Q-0040、Q-0038 等 post-trade / 证券类题的背景。**你没有直接的证券 post-trade 生产经验**，面试时一律"先承认，再桥接"（A-Q0034）。
**核实日期**：2026-10-26。

## 1. 交易生命周期
```
Execution（成交）
  └─► Confirmation / Matching（确认与匹配）
        └─► Clearing（清算；常经 CCP，novation + netting）
              └─► Settlement（结算；通常 DvP = 券款对付，在 CSD）
                    └─► Custody & Asset Servicing（托管、公司行为）
Reconciliation 与 Regulatory Reporting 贯穿全程
```
- 报文：证券结算常用 SWIFT **MT54x**；ISO 20022 有对应的 **sese / semt** 报文，在逐步推广。**没有像 CBPR+ 那样统一的强制截止日**，不要这么说。

## 2. T+1
| 市场 | 切换时间 | 来源 |
|---|---|---|
| 美国 | 2024 年 5 月（已完成） | 公开事实 |
| 欧盟、英国、瑞士 | **2027-10-11** | [The TRADE](https://www.thetradenews.com/uk-confirms-october-2027-alignment-with-eu-and-switzerland-for-t1-transition) |
- 影响：留给确认、匹配和资金安排的时间更短 → 更依赖 STP、自动化的异常处理，以及当天修复 break。

## 3. 哪些能迁移，哪些不能（与你的支付经验对照）
| 能迁移（你的证据） | 迁移不过去（要学） |
|---|---|
| 交易生命周期和状态处理（PA-01.3） | CCP 与 novation |
| 报文标准与 ISO 20022 迁移（PA-01.1） | DvP 与结算周期 |
| 对账与 break 处理（PA-11.2，VV） | 托管、sub-custody、公司行为 |
| cut-off 窗口、异常处理、审计（PA-01、X-06） | 保证金与抵押品 |

## 4. 数据存储取舍（来自旧稿 #1 / #4，作为思路参考）
- 结构固定、强事务、需要对平（头寸、总账、资金清算）→ 关系库。
- 结构多变、按 key 查询、高吞吐（交易事件、结算指令、确认报文、对账结果、审计轨迹）→ 文档库。
- 混合架构：关系库作为 system of record，通过 CDC 和 Kafka 同步到文档库，支撑查询（CQRS）。

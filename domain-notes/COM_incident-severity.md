# COM — 事故分级 Sev1–4（行业通用框架，不是个人事实）

**用途**：A-Q0017（出过问题的发布 / 事故带队）、A-Q0058（BAU 和项目排优先级）、TEL / BNK 服务交付类岗位。
**来源**：你的旧准备稿 #15（2026-08-30），按行业通用做法整理；MAS 的部分已对照 MAS Notice FSM-N03 核实（见 `BNK_mas-incident-availability.md`）。各家公司的具体时限不同，**以下是常见做法，不是 UOB 的制度**。
**你的事实锚点**：在 UOB 处理 P1–P3 事故并为 MAS 报告提供技术分析（03 X-06）；在 VV 和 AI Park 亲自定义过事故分级和分层应急预案（03 PA-11.5、PA-16.5）。

| 维度 | Sev-1（Critical） | Sev-2（High） | Sev-3（Medium） | Sev-4 / 5（Low） |
|---|---|---|---|---|
| 典型定义（银行） | 核心 / 支付 / 清结算系统全停或大面积客户不可用；数据完整性受损；重大安全事件 | 关键服务严重降级，有 workaround；单一渠道中断 | 局部功能异常，影响可控 | 轻微或无客户影响 |
| 确认时限 | 数分钟（5–15 min），7×24 立即 paging | 约 15–30 min | 工作时间内数小时 | 下一个工作日 |
| 解决目标 | 以分钟 / 小时计，全员优先 | 数小时 | 1–2 个工作日 | 进 backlog |
| 指挥结构 | 立即启动 Incident Commander + war room；业务、风控、对外沟通待命 | IC 或资深 on-call 主导 | on-call 工程师处理 | 常规工单 |
| 升级路径 | CIO / CISO，必要时到 CEO / 董事会 | 部门负责人 | Team lead | 不升级 |
| 沟通节奏 | 每 15–30 min | 每 30–60 min | 每日或按里程碑 | 关闭时通报 |
| 监管（新加坡 MAS） | 构成 relevant incident 时：**1 小时内**通知 MAS，**14 天内**提交根因与影响报告 | 视是否构成 relevant incident | 一般不触发 | 不触发 |
| 事后复盘 | 强制 blameless postmortem + 改进项跟踪 | 强制或按需 | 可选 | 免 |

## 支付事故特有的收尾
- **止血先于查因**，但要先评估止血动作本身会不会造成数据不一致（例如回滚后交易状态和下游对不上）。
- **技术恢复不等于事故结束**：还要确认有没有重复扣款、消息丢失（例如 pain.002 回执没回来）、需要人工处理的挂单——通常要和 Ops / Finance 一起对账。

## 面试用法
讲事故题时，可以一句带出你知道分级的意义："Severity sets the response — who's on the call, how often we update, and whether the regulator needs to hear from us within the hour." **你亲自定义过分级是在 VV 和 AI Park，不是 UOB**（UOB 用的是银行既有的事故框架，X-06）。

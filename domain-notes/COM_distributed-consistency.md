# COM — 分布式一致性与 Kafka（技术知识，不是个人事实）

**用途**：Q-0035、Q-0036、Q-0029 的追问。来源：旧稿 #2 / #6（Q9 Outbox / Saga，2026-10），按通用技术知识整理。
**你的 Kafka 生产经验来自 VV、AI Park（PA-11.4、PA-16.4）。** UOB 的 hub 是否用 Kafka，03 没有记录（SA-12）。

## 1. 一致性四层
| 层 | 解决什么 | 要点 |
|---|---|---|
| Outbox | 写库成功但消息丢了 | 业务变更和 outbox 记录在同一个本地事务里；由 relay / CDC 负责发布 |
| 幂等消费 | at-least-once 带来的重复 | 唯一消息 ID，加唯一约束；"处理"和"记为已处理"在同一个事务里 |
| Saga | 跨服务的多步流程 | 每步都有补偿动作；编排式或协同式 |
| 对账 | 设计正确也可能出错 | 和账本或对手方核对，break 进 exception queue |
- 为什么不用 2PC：需要 XA 支持，协调者是单点，锁持有时间长，跨服务、跨云不现实。

## 2. Kafka consumer 要点
- 同一个 group 里，一个 partition 只分给一个 consumer → 并行度不超过分区数；不同 group 各自消费全量数据。
- 顺序只在单个分区内保证 → 按业务 ID 做 key。
- 配置：`enable.auto.commit=false`（处理成功后再提交）；`max.poll.records` / `max.poll.interval.ms`（处理太慢会触发 rebalance）；`auto.offset.reset`；`isolation.level=read_committed`。
- Producer：`acks=all`、`enable.idempotence=true`。
- 毒消息：有限次重试 → 重试 topic → DLQ，加告警。

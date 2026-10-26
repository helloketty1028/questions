# Prompt 01 — 从简历库生成或刷新 STAR 故事

先读 `CLAUDE.md`、`governance/taxonomy.md`、`governance/templates/story.md`，再按 CLAUDE.md §2 的顺序读取 `03_Achievement_Library.md`、`02_Candidate_Profile.md` 和 `fact-check-and-open-questions.md`。列出实际读取的文件和版本号。

**本次范围**：<全部 / 指定 ID，如 PA-01, PA-02, X-06 / 刷新 facts_version 落后的故事>

## 阶段一：提出故事清单（输出后暂停）
1. 只从 ✅ / 📄 / 🔶 的子成就中选材；⚠️ ⛔ 一律排除；❓ 只用 `{ }` 以外的部分。
2. 一个故事 = 一个可以讲 2 分钟的具体事件或项目片段，可以组合同一项目下的多个子 ID。不要一个项目只写一个笼统的故事：生产事故、DR 演练、供应商冲突应分开写。
3. 优先选 03 §1 中对应岗位为 ●●● 的条目，以及 "Strongest evidence by target role" 里列出的条目。
4. 用表格列出：拟定 S-ID | 标题 | facts | roles | industries（BNK direct；INT / TEL 是否可迁移）| 可回答的典型问题（取自 03 各项目的 Interview 字段）| 数字（只列 §0A 中有的）| 风险（❓ 项、内部名称、对外措辞限制）
5. 指出 03 中证据不足、讲不成故事的地方，作为回灌简历库的候选。

## 阶段二：确认后写入
- 按模板创建 `stories/S-xxx.md`，`status: draft`，`facts_version` 填当前 03 的版本号。
- Action 段写我的个人行为，所有权等级以 03 的 O1–O5 为准，不放大。
- Result 段只用 §0A 的数字并保留限定词；没有数字就写定性结果。
- 运行 `python scripts/build_index.py`，修复所有 ERROR。
- 汇报：新增或修改的文件、仍需我确认的点。由我逐条确认后再改为 `verified`。

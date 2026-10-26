# Prompt 02 — 新增题目 / 面试复盘入库

先读 `CLAUDE.md`、`governance/taxonomy.md`、`governance/templates/question.md`、`governance/templates/answer.md` 和 `index/questions.md`。

**输入（选一种）**：
- A. 题目清单：<粘贴问题，可附行业、岗位、出处>
- B. 面试复盘：<公司 · 岗位 · 轮次 · 面试官类型 · 被问到的问题 · 我当时的回答要点 · 面试官的反应>
- C. 种子导入：从 `03_Achievement_Library.md` 各项目的 `Interview` 字段，以及 §0A 标为 "high interview risk" 的项中提取题目

## 阶段一：去重与分类（输出后暂停）
1. 每道题整理成英文主问法。与现有题目的 `q` 和 `variants` 比对：
   - 考察点相同 → 不新建，作为 variant 并入已有 Q-ID，并补 `asked_at`
   - 考察点相近但不同 → 新建，在备注里写明区别
2. 按 taxonomy 分配 industry、role、qtype、topics、priority。题目源于简历里的说法、可能被质疑时，qtype 用 `RISK`。
3. 匹配已有故事（S-ID）；找不到合适故事的题标为"缺故事"。
4. 用表格输出：拟定 Q-ID 或并入的 Q-ID | 问题 | 分类 | 故事 | evidence | 处理方式。
5. 复盘（B）另外输出：回答得不好的地方，以及原因（缺故事 / 缺事实 / 表达问题）；新出现的事实 → 列为 `Fact_Update_Proposal` 候选，不写入简历库。

## 阶段二：确认后写入
- 新题按模板创建 `questions/Q-xxxx.md`（`status: draft`），同时创建 `answers/A-Qxxxx.md` 骨架，只填答题逻辑。完整答案由我指定后再写。
- 并入的题目只追加 `variants` 和 `asked_at`，不改其他字段。
- 复盘中出现的新事实，写入 `prep/<对应文件夹>/Fact_Update_Proposal.md`。
- 运行 `python scripts/build_index.py`，修复 ERROR，并汇报变更清单。

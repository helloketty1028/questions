# Interview Bank

面试题库。事实来源是 `C:\Users\surface\resumes`（只读），完整规则见 `CLAUDE.md`。

```
questions/Q-xxxx ──answer──► answers/A-Qxxxx ──stories──► stories/S-xxx ──facts──► resumes\...\03_Achievement_Library (PA-xx.n / X-xx)
        ▲                                                                                      │
        └──────────── prep/<JD文件夹>/  ◄── resumes\applications\<同名文件夹>（投递版简历 + 匹配分析）◄┘
```

**每次开任务**：同时选择 `resumes` 和 `Interview Bank` 两个文件夹。

**首次建库顺序**：`prompts/01` 生成故事 → `prompts/05` 分批导入旧题库（放在 `inbox/`）→ `prompts/02` 补种子题（03 的 Interview 字段 + 高风险说法）→ 补全答案 → `prompts/04` 审计。

**日常**：拿到 JD 用 `prompts/03`；面试结束后用 `prompts/02` 复盘入库；每月用 `prompts/04` 审计一次。

**索引**：`python scripts/build_index.py`，生成 `index/questions.md`、`coverage.md`、`stories.md`、`issues.md`。

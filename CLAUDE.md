# Interview Bank — 工作规则（每次任务先读本文件）

## 1. 目的
维护一个可复用的面试题库，覆盖 BNK / INT / TEL 三个行业 × ATL / TPM / SM 三类岗位。四层引用关系：
`Question`（会被问什么）→ `Answer`（按岗位怎么讲）→ `Story`（STAR：我做过什么）→ **事实 ID**（存放在简历库）。
本库**只引用事实 ID，不复制事实**。

## 2. 事实来源（只读）
读取顺序：
1. 本地 `C:\Users\surface\resumes\master\v2.0-draft\`
2. 本地读不到时：GitHub `helloketty1028/Resumes`（只读，路径相同）。注明读取的 commit，并提示可能落后于本地。
3. 两处都读不到：停止并说明，不凭记忆补写。

- 开工前列出**实际读取**的文件和版本号。
- 核心文件：`03_Achievement_Library.md`（PA-xx / PA-xx.n / X-xx、状态图标、§0A Metrics Bank、各项目的 Interview 字段）、`02_Candidate_Profile.md`（时间线、职位）、`fact-check-and-open-questions.md`。
- 针对具体 JD 时，另读 `resumes\applications\<文件夹>\` 里的**投递版简历**和 `JD_Matching_Analysis.md`。
- `archive\`、`reference\` 不作为事实来源。

## 3. 事实规则
- 个人经历只能通过事实 ID 引用。本库文件不新增事实，也不改写数字。
- 数字只能取自 03 §0A Metrics Bank，并保留原来的限定词（如 "estimated"）。
- 按 03 的状态图标使用：✅ 📄 可用；🔶 谨慎使用；❓ 只能用 `{ }` 以外的部分；⚠️ ⛔ 不用。
- 对外表述不出现内部系统名、UOB 交易量、客户名、供应商名（03 safe-wording rules）。
- 不把 "CTO" / "Chief Architect" 说成曾任职位。
- JD 的要求不等于我的经历。TEL 题默认 `evidence: transferable`，除非 03 里有直接证据。
- 发现新事实或冲突时，写入 `prep\<文件夹>\Fact_Update_Proposal.md`，由我拿回 Resume Project 处理。**不修改简历库**。

## 4. 写入边界
- 只写入 `C:\Users\surface\Interview Bank\`；简历库只读。
- 已 approved 的答案版本、已 verified 的故事，未经我确认不改。
- 批量新增或改写之前，先列出计划，等我确认后再执行。

## 5. 结构与 ID
| 目录 | 内容 | ID |
|---|---|---|
| `questions/` | 一题一个文件 | `Q-0001` |
| `answers/` | 一题一个答案文件，内含 ATL / TPM / SM 三个版本 | `A-Q0001`（与题目一一对应） |
| `stories/` | STAR 故事，只引用事实 ID | `S-001` |
| `domain-notes/` | 行业知识（不是个人事实） | — |
| `prep/<文件夹>/` | 单个 JD 的面试包，文件夹名与 `resumes\applications\` 下的同名 | — |
| `index/` | 由脚本生成，**不手改** | — |
| `inbox/<批次>/` | 待导入的旧材料，原文件只读 | — |

- ID 一经分配，不改也不复用；退役时设为 `status: retired`。文件名必须等于 ID。
- 分类代码见 `governance/taxonomy.md`；模板在 `governance/templates/`。
- frontmatter 只能用 `key: value` 和 `key: [a, b]` 两种写法（索引脚本依赖这一点）。
- 新增或修改文件后运行 `python scripts/build_index.py`，并处理 `index/issues.md` 里的 ERROR。

## 6. 固定流程（prompts/）
- `01_Build_Stories.md`：从 03 库生成或刷新故事
- `02_Add_Questions_and_Debrief.md`：新增题目；面试后复盘入库
- `03_JD_Interview_Prep.md`：针对单个 JD 生成面试包
- `04_Bank_Audit.md`：定期审计（重复题、断链、事实漂移、覆盖缺口）
- `05_Import_Legacy.md`：导入旧题库和旧答案（逐条核查事实后再入库）

## 7. 输出语言
- 答案用自然口语化英文，分析和说明用中文。
- 不确定的内容明确标出，不假装已经核实。

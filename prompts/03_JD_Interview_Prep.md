# Prompt 03 — 针对单个 JD 生成面试包

先读 `CLAUDE.md`、`governance/templates/prep.md`、`index/questions.md`、`index/stories.md`，然后按 CLAUDE.md §2 读取简历库。

**输入**：
- 申请文件夹：`resumes\applications\<文件夹名>`（读其中的 `JD.md`、**投递版简历**（docx 或 pdf 的最终版，不读 draft）和 `JD_Matching_Analysis.md`）
- 没有申请文件夹时：直接粘贴 JD 文本，并说明投的是哪一版简历
- 面试信息：<轮次 / 面试官类型 / 时长 / 已知形式>
- 题量：<默认 20 题，重点答案 8 题>

## 阶段一：分析与题单（输出后暂停）
1. 确定 Family（ATL / TPM / SM）× Lens（BNK / INT / TEL），写出依据；沿用 `JD_Matching_Analysis.md` 的判断，有不同意见时说明。
2. 岗位要点 3–5 条：这个岗位最在意的能力。
3. **简历会引发的追问**：投递版简历里的每条关键说法 → 面试官可能怎么深挖。数字、所有权、"led / owned" 之类的措辞优先。
4. **Gap 题**：`JD_Matching_Analysis.md` 里的 gap → 一定会被问的问题，以及诚实的应对口径（gap / transferable）。
5. 排序题单：已有题目用 Q-ID；新题标"新"。每题写明为什么会问、用哪个故事、答案现状（approved / draft / 无）。
6. 列出需要先补的故事或事实。

## 阶段二：确认后生成
- 在 `prep/<同名文件夹>/Interview_Prep.md` 中按模板输出。
- 重点题：已有 approved 版本的直接引用 A-ID，只补本岗位的行业角度；没有的在面试包里写本次草稿（对应岗位版本，30s + 60s + 追问应对），**不直接改动题库里的答案**。
- 写 3–5 个反问问题，要针对这家公司和这个岗位。
- 新题、新事实列入 §7，由我决定是否用 prompt 02 入库、是否回灌简历库。
- 收尾：实际读取的文件和版本、重点准备的 5 道题、仍然最薄弱的 3 个点。

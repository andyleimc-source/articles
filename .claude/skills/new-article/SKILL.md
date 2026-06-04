---
name: new-article
description: 新建一篇文章的固定目录骨架。用户输入 /new-article <slug> 或「新建文章 <slug>」时触发，在当前工作目录下生成标准结构（article.md、article-en.md、image/、prompts/）并预填 frontmatter，不读取任何已有文章。
disable-model-invocation: true
---

# 新建文章脚手架

给定一个 slug（kebab-case，如 `02-llm-wall-and-you`），在**当前工作目录**下创建固定结构。**不要**读取任何已有文章、不要扫描目录。

## 步骤

1. 取参数为 `slug`。若用户没给，问一句要什么 slug，停在这里。
2. 若 `<slug>/` 已存在，**停下报错**，不要覆盖。
3. 创建目录与占位文件：

```bash
mkdir -p "<slug>/image" "<slug>/prompts"
```

4. 写 `<slug>/article.md`（中文正文骨架）：

```markdown
<img src="cover.png">

# 标题待定

> 一句话副标题 / 钩子

正文待写。
```

5. 写 `<slug>/article-en.md`（英文骨架）：

```markdown
# Title TBD

> One-line subtitle / hook

Draft.
```

6. `image/` 与 `prompts/` 留空（出图时再填）。
7. 完成后提示：「骨架已建好。写正文前先读 `WRITING.md`；出图走 baoyu skills + 品牌色（见 `BRAND.md`）。」

## 约束
- 封面引用统一用 `cover.png`（封面单独出图后放进目录）。
- 不要顺手写 promotion.md / xhs.md —— 那是发布阶段的产物。
- 创建完不要自动开始写内容，交回给用户。

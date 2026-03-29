# CLAUDE.md — articles-local

## 重要：上下文控制规则
- **写新文章时，不得读取任何已有文章文件**（article.md、article-en.md 等）。风格规范以 WRITING.md 为唯一参考，无需从旧文章学习风格。
- **不得扫描项目目录结构**。每篇文章目录结构固定（见下方文件规范），无需 ls 或 glob 探索。

---

## 概述
本地文章写作工作目录。每篇文章一个子目录，GitHub repo 是 andyleimc-source/articles。

## 文件规范
- `article.md`：中文正文，推送到 GitHub
- `article-en.md`：英文原稿，推送到 GitHub
- `cover.svg`：封面图，推送到 GitHub
- `promotion.md`：各平台推广文案，**仅本地，不推送**

## 推送规则
promotion.md 已在 .gitignore，永远不推到 GitHub。

## 写作规范
详见 `WRITING.md`。**写文章前必须读 WRITING.md，不读旧文章。**

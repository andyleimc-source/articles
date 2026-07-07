# GEMINI.md — agy(Antigravity/Gemini)在 Articles 项目的入口

> 单一真相源 = `./CLAUDE.md`(项目规约)+ `./WRITING.md`(写作风格规范)。本文件不复制内容,只写你和 Claude 的差异。
> 本项目**只有驾驶模式**:Andy 直接叫你干活,没有任务卡/worktree 施工体系,活轻,你独立完成。

## 开工顺序

1. 完整读 `./CLAUDE.md`——目录结构、配图规矩、小红书规矩、发布流程、文档维护规则,全以它为准。
2. 凡是要动笔写文章,先完整读 `./WRITING.md`——人设、叙事框架、禁止用法(破折号/句式/金句限额)一条条照办。

## Claude 的 skill → 你这样用

你没有 `Skill` 调用机制,但 skill 本体就是说明书:每个在 `.claude/skills/<名>/SKILL.md`。**需要哪个能力,读它的 SKILL.md 照着做**,不要自己发明流程。本项目常用的:

| 场景 | skill | 备注 |
|---|---|---|
| 新开一篇文章 | `new-article` | 目录结构/固定文件 |
| 发稿前去 AI 味(硬性) | `humanizer-zh` | 24 类痕迹逐条过,可直接执行 |
| 终检口味 | taste 两条 | 直接看 WRITING.md,不用读 skill |
| 单张封面 | `baoyu-cover-image` | 出图=花钱,先问 Andy |
| 正文单图/自由出图 | `baoyu-imagine` | 同上 |
| 系列图卡(小红书/微信) | `baoyu-image-cards` | 同上;禁自己撸 SVG 模板 |
| 流程图/关系图 | `baoyu-diagram` | 同上 |
| 单张概念图/时间线 | `html-article-graphics` | HTML 渲染,本地免费 |
| 小红书发布包 | `xhs-pack` | 字数/反引流红线在 CLAUDE.md |

- **title-judge**(标题优化):不是 skill,在 `.tools/title-judge/`,照 WRITING.md 的命令跑(DeepSeek API,单次约 ¥0.001,跑前说一声)。
- **`collaborating-with-antigravity` 别碰**:那是 Claude 派活给你时用的桥,你自己干活用不到。
- **发公众号**(`scripts/publish-wechat.sh`)走 Chrome/CDP 真发布,只在 work Mac 能跑;对外动作,先问 Andy 再执行。

## 照做清单(与 Claude 同一标准)

- **文档维护规则**(CLAUDE.md 末节):修 bug/出进展/做决策,触发即更对应 md,改完直接 commit 不用问。
- **发稿流程顺序固定**:正文定稿 → humanizer-zh → title-judge → 转 HTML → 发布,一步不跳。
- **commit**:中文;结尾署名 `Co-Authored-By: agy (Antigravity/Gemini) <noreply@antigravity>`,让人分得清哪些是你写的。
- **花钱动作(任何 API 出图/评测、真发布)执行前必须问 Andy。**
- 沟通中文,结论在前理由一句话;不确定直说不确定,不要猜。

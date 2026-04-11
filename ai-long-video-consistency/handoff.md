# Handoff —— AI 长视频一致性教程（kling-studio 实战）

> **这是什么**：从上一轮对话接力过来的工作交接文档。上一轮把 `kling-studio` 工作流从 0 搭到 M4（流水线跑通 + 10s 烟测出片成功），并就本文章的选题、结构、风格达成共识。用户切换到本项目继续**写文章**。
>
> **新对话的第一件事**：读完本文档 → 读 `~/Desktop/articles/WRITING.md` → 读 `~/Desktop/articles/CLAUDE.md` → 再开始写 `article.md`。
>
> **本文档的定位**：工作笔记，不发布。`article.md`、`article-en.md`、`cover.svg`、`promotion.md` 才是交付物。

---

## TL;DR

- **主题**：如何从零搭建一套能生成高一致性 AI 长视频的工作流。核心洞察：长视频一致性问题不是 prompt 能解决的，必须交给底层模型的"主体绑定"机制。
- **实证项目**：`~/Desktop/kling-studio/` —— 围绕可灵（Kling）Omni Video + Element 主体管理搭建的一个极简 Python 工作流。当前进度 M4（流水线跑通 + 10 秒烟测成片带声音），已注册 7 个 element，已完成 1 次出片实证。
- **发布目标**：微信公众号「雷码工坊笔记」，中文，约 5000 字，深度长文。
- **读者定位**：技术开发者 + 非技术营销同行兼顾——既讲得了架构，又让不写代码的人理解为什么这么做。
- **独立成篇**：不引用旧的 `ai-video/article/` 系列 4 篇日志（那些基于即梦流水线已过时）。本文是全新开篇。
- **写作时机**：当前项目尚未完全跑完（M5、M6 未完成，音色绑定未做）。本文章需要**跟着项目进度增量更新**，最终与项目全部跑通同步完成。
- **立刻可写**：M1→M4 所有素材齐备，可以先写"问题定义"→"技术选型"→"从 0 到流水线跑通"这 4 个章节的初稿，剩余部分等项目推进再补。

---

## 一、本项目核心约定（已与用户敲定，不需要再讨论）

| 维度 | 决策 |
|---|---|
| 主题 | 如何用可灵搭建一套能生成一致性高的 AI 长视频工作流 |
| 语言 | 中文 |
| 篇幅 | **约 5000 字**，深度长文 |
| 平台 | 微信公众号「雷码工坊笔记」 |
| 读者 | **技术 + 非技术兼顾**。非技术读者能读懂"为什么"和"价值"，技术读者能按步骤复现 |
| 独立性 | **独立成篇**，不引用旧的 4 篇日志 |
| 风格 | 按 `~/Desktop/articles/WRITING.md` 的规范，**写作前必读** |
| 调性 | 专业但不堆砌术语；有观点；实战感；和用户一贯的「雷码工坊笔记」风格一致 |
| 交付物 | `article.md`（中文主文）、`cover.svg`、`promotion.md`（推广文案，仅本地）、可选 `article-en.md` |

---

## 二、核心故事脉络（建议的文章骨架）

这是给新对话的写作起点，**不是最终结构**，新对话可以调整。

```
标题建议：几个候选
  - 《怎么让 AI 视频的主角始终长一个样？——从一个一直头疼的问题说起》
  - 《AI 视频 60 秒一致性：我用可灵 Omni 摸出的一条路》
  - 《不靠 prompt 魔法，让 AI 长视频不再漂移的工程化思路》

## 开篇（500 字）
钩子：展示一个 10 秒 2 镜头的视频（smoke-test 成片），两个镜头 Boss 角色
一致到让人以为是同一个人拍的——但其实是 AI 分别生成的。抛出悬念：
"做到这一点花了 8 块钱。"

## 第一部分：一致性是 AI 长视频的头号难题（800 字）
- 15 秒以下的短视频没这个问题
- 30-60 秒才是真正的战场：人脸漂、衣服变、场景换、光线跳
- 为什么？因为目前几乎所有视频模型的 context window 是"一次生成"
- 业内常见的三种补丁方案 + 为什么都治标不治本：
  1. Prompt 里写死外形描述 → 每次重新猜
  2. 多图参考（reference images）→ 仍然是每次重解释
  3. 角色 LoRA 训练 → 门槛高、训练成本高、不跨模型
- 我之前的 ai-video/ 项目就是靠堆 prompt + scene bible + 人物参考图，结果漂移依然

## 第二部分：可灵提供的破局能力（1000 字）
- 可灵 Omni Video 2 个杀手级功能：
  1. **Omni 多镜头模式**：一次请求生成最多 6 个连贯镜头（每段 3-10s），
     镜头间的一致性由模型后端直接保证，不用拼接
  2. **Element 主体管理**：把角色/场景/道具预注册成云端"身份证"，
     拿到 element_id，以后所有视频请求只要引用这个 id，Kling 后端
     就锁死外形。跨视频、跨项目、跨月都一致
- 加上一个甜点：**sound: on 原生自带声音**——台词、音效、BGM 都有，
  不需要任何后期
- 对比图/表：老方案 vs 新方案

## 第三部分：从零搭 kling-studio（1500 字）
这是硬核实操章节。按 M1→M4 讲：

### M1 脚手架（200 字）
目录结构 / 技术栈（Python + httpx + pydantic + PyYAML + typer）/ 
为什么不用 moviepy / 依赖极简

### M2 Kling 客户端（300 字）
JWT 鉴权（30 分钟 token）/ 统一错误处理 / probe 命令一次搞定鉴权验证
代码片段：`_jwt_token()`

### M3 元素注册（500 字）—— 整篇文章的技术高潮
这是最值得展开的一章。讲清楚：
- 本地参考图 → 腾讯 COS 临时托管 → Kling 摄取 → element_id 回写 →
  COS 文件立即删除（省钱）
- "上传即删除"的契约如何用 Python context manager 保证
- 为什么要有本地 registry.json 作为真相源
- 演示：Boss 从一张肖像图 → 307840124555148 这个永久身份证

### M4 出片流水线（500 字）
Storyboard YAML → pydantic 校验 → 渲染成 Kling payload → 
Omni 多镜头 API → 轮询 → 下载 → 自动写 review.md
演示：10 秒烟测成片的完整流程

## 第四部分：实证——一次 8 块钱的烟测（600 字）
- 剧本：Boss 走进办公室看手机皱眉（5s）→ 在桌前叹气后坚定抬头（5s）
- 成片展示（附静帧 / 或嵌视频）
- 技术指标：1920×1080 / H.264 / AAC / 10.04s / 8.4MB
- 成本拆解：0.8 元/秒 × 10 秒 = 8 元
- 最重要的观察：Boss 在两个镜头中是同一个人（截帧对比）

## 第五部分：现存问题和下一步（500 字）
诚实说明当前还没解决的问题：
- **音色绑定**（方案 A：选官方预设音色，详见第四节"待办"）
- 60 秒内的跨 batch 拼接（M5 未做）
- 完整 48h 剧情片（M6 未做）
- Kling 生图时屏幕上的文字是乱的（已知局限）

## 结尾（300 字）
核心主张三段式：
1. **一致性不是 prompt 问题，是架构问题**
2. **把可复用的东西做成"身份证"**（element_id / voice_id / 任何能长期绑定的标识）
3. **让后端做后端该做的事**，不要用客户端 prompt 去模拟它
CTA：留言 / 关注公众号 / 加微信
```

---

## 三、素材与数据源（新对话要去哪读）

### 3.1 代码和产物（实证项目）

主路径：**`~/Desktop/kling-studio/`**

| 路径 | 说明 | 对文章的用处 |
|---|---|---|
| `src/kling_client.py` | Kling API 客户端（JWT、Omni Video、Element、图像生成） | 第三部分 M2 章节的代码片段 |
| `src/schemas.py` | pydantic 数据模型 | M1 章节"为什么选 pydantic" |
| `src/cos_client.py` | 腾讯 COS 上传 + 即用即删 context manager | M3 章节的"上传即删除契约" |
| `src/register_elements.py` | 元素注册 CLI | M3 章节主戏 |
| `src/bootstrap_assets.py` | 一次性生成 scene/prop 参考图并注册 | M3 章节"批量注册" |
| `src/render.py` | 把 Batch 翻译成 Kling payload（纯函数） | M4 章节 |
| `src/generate_video.py` | 主流水线 CLI | M4 章节 |
| `src/review.py` | 自动审片文档生成 | M4 章节"工程审美" |
| `assets/actors/registry.json` | Boss / Client 两个演员的 element 注册表 | 实际数据展示 |
| `assets/scenes/registry.json` | modern_office / meeting_room / office_night | 同上 |
| `assets/props/registry.json` | laptop / dashboard_screen | 同上 |
| `projects/smoke-test/storyboard.yaml` | 10s 烟测剧本 | 第四部分"一次 8 块钱的烟测"的原始剧本 |
| `projects/smoke-test/output/final.mp4` | 烟测成片 | 文章附视频 / 截帧来源 |
| `projects/smoke-test/review.md` | 烟测审片文档 | 可以直接贴出来作为"工作流自证" |
| `templates/storyboard.yaml` | 剧本模板 | "可复用工作流"的证据 |
| `CLAUDE.md` | 项目工作流说明 | 引用思路 |
| `README.md` | 项目概览 | 引用思路 |
| `PROMPT_GUIDE.md` | 可灵多镜头 prompt 写作指南 | 可以整章引用或提炼 |
| `docs/architecture.md` | 项目架构说明 | 对应文章第三部分 |

### 3.2 图片素材（可直接嵌到文章）

| 文件 | 用途 |
|---|---|
| `~/Desktop/kling-studio/assets/actors/boss/frontal.png` | Boss 参考图 |
| `~/Desktop/kling-studio/assets/actors/client/frontal.png` | Client 参考图 |
| `~/Desktop/kling-studio/assets/scenes/modern_office/frontal.png` | 白天办公室 |
| `~/Desktop/kling-studio/assets/scenes/meeting_room/frontal.png` | 会议室 |
| `~/Desktop/kling-studio/assets/scenes/office_night/frontal.png` | 夜间办公室 |
| `~/Desktop/kling-studio/assets/props/laptop/frontal.png` | 笔电 |
| `~/Desktop/kling-studio/assets/props/dashboard_screen/frontal.png` | 数据面板 |
| `~/Desktop/kling-studio/projects/smoke-test/output/final.mp4` | 10s 烟测成片（可截帧） |

**操作建议**：把要用的图片复制到本项目的 `imgs/` 目录下保持独立。公众号发布时再按需压缩。

### 3.3 可灵 API 文档（技术论据来源）

主路径：**`~/Desktop/api-docs/kling/docs/`**

| 文件 | 用途 |
|---|---|
| `apiReference_commonInfo.md` | JWT 鉴权、错误码、通用信息 |
| `apiReference_model_OmniVideo.md` | Omni Video 完整 API，含 multi_shot、sound、image_list、element_list、video_list |
| `apiReference_model_element.md` | 主体管理（创建、查询、删除） |
| `apiReference_model_customVoices.md` | 音色克隆 API |
| `apiReference_model_TTS.md` | 官方预设音色列表 |
| `productBilling_prePaidResourcePackage.md` | 价目表（重要，成本拆解用得上） |

**引用规范**：文章里如果要给准确 API 细节，从这些文档里找原文，不要凭记忆。

---

## 四、关键数据与成本（文章可直接引用）

### 4.1 已注册的 7 个 element

| 类型 | 名字 | element_id | 备注 |
|---|---|---|---|
| actor | Boss | 307840124555148 | 从旧项目迁移的角色肖像 |
| actor | Client | 307840130662211 | 同上 |
| scene | modern_office | 307840597127257 | Kling T2I 现场生成（白天 CBD 开放办公） |
| scene | meeting_room | 307840619937213 | Kling T2I 生成（会议室带壁挂屏） |
| scene | office_night | 307851285329146 | Kling T2I 生成（夜间办公室，冷蓝监视器光） |
| prop | laptop | 307840642000137 | Kling T2I 生成（1:1 银色笔电） |
| prop | dashboard_screen | 307840663434261 | Kling T2I 生成（壁挂数据面板） |

> **注意**：Boss 和 Client 这两个 element 即将因为"音色绑定"被删除重建，id 会变（见第五节）。文章定稿前确认最新 id。

### 4.2 成本数据（可灵 Video-3O 模型，std 模式，element 参考，有声）

- 单位价格：**0.8 元 / 秒**
- 烟测（10s）：**8 元**
- Shot 07 微测预估（6s）：**4.8 元**
- 完整 48h 剧本预估（55s，一次 multi-shot）：**约 44 元**
- 省钱选项：`sound: off` → 0.6 元/秒（省 25%），但会失去自带声音优势
- 无法省钱的维度：**降低分辨率不省钱**——Kling 按时长收费，不按分辨率
- 更贵的选项：`mode: pro` → 1.0 元/秒（贵 25%，画质更高）
- 失败不扣费：内容安全、任何原因失败都不扣积分（官方文档确认）

### 4.3 技术指标（烟测成片）

- 分辨率：1920 × 1080（16:9 固定）
- 视频编码：H.264
- 音频编码：AAC
- 时长：10.04 秒（接近完美命中目标 10 秒）
- 文件大小：8.4 MB
- 生成耗时：约 3-5 分钟（提交到下载完成）
- 自带内容：环境音（脚步声）+ 叹气音 + 轻微 BGM
- 跨镜头一致性：Boss 的五官、发型、服装、肤色在 2 个镜头之间**肉眼完全一致**

---

## 五、尚未做完的事（文章定稿前必须解决）

### 5.1 音色绑定（方案 A 坍塌 → MiniMax × Kling 桥接管线）

> **重大更新（2026-04-11）**：原计划的"方案 A = 选 Kling 官方预设音色"已被证伪,不得不重新设计。最终跑通的是一条**跨供应商的桥接管线**。失败和反转过程比原方案更有故事性,详细叙事材料见本文档 **第十一节**（文章可以直接取用）。

**当前状态**：桥接管线已打通,Boss 和 Client 的 Kling 克隆 voice_id 均已拿到。剩下"删重建 Boss/Client element → 绑定 voice_id"这一步 + Shot 07 微测。

**已拿到的两个 Kling 克隆 voice_id**：

| 角色 | 源音色（MiniMax 系统音色） | 克隆样本（本地 mp3，12 秒） | Kling voice_id | 本地试听 wav |
|---|---|---|---|---|
| Boss   | `English_Gentle-voiced_man` | `_minimax_test_gentle.mp3` | `871830494903013460` | `_kling_clone_trial_boss_gentle.wav` |
| Client | `English_Trustworthy_Man`    | `_minimax_test_trustworthy.mp3` | `871832297002659873` | `_kling_clone_trial_client_trust.wav` |

两条克隆均位于 `~/Desktop/kling-studio/assets/voices/`。

**实际扣费**：Kling `POST /v1/general/custom-voices` 的响应字段 `final_unit_deduction = "0.05"` —— **每条克隆 5 分钱**，两条合计 0.1 元。这是整个技术路径里最大的意外之一（原本担心克隆贵）。

**用户已做的品质确认**：
- ✅ Kling 克隆版 Boss 试听 wav：说英文、音色贴近 MiniMax 原版、清晰自然（用户原话："1.是英文 2.声音相似 3.清晰自然 都很好"）
- 🟡 Kling 克隆版 Client 试听 wav：已下载到本地，**待用户在进入 element 重建前再确认一次**

**剩余待执行动作**（顺序）：
1. 用户确认 Client 克隆试听 OK（`open assets/voices/_kling_clone_trial_client_trust.wav`）
2. `kling.delete_element(307840124555148)` 删除当前无音色的 Boss
3. `kling.delete_element(307840130662211)` 删除当前无音色的 Client
4. 复用 `register_elements._register_one` 流程重建 Boss：
   - 本地参考图不变（`assets/actors/boss/frontal.png`）
   - 把 `voice_id="871830494903013460"` 传给 `create_element`
5. 同样重建 Client，传 `voice_id="871832297002659873"`
6. 新的 element_id 写回 `assets/actors/registry.json`，并补 `voice_id` 字段
7. 同步更新 `assets/voices/registry.json`（如果采纳选项 β 本地音色库）
8. `python -m src.register_elements list --remote` 对账

**参考代码位置**：
- Kling 客户端：`src/kling_client.py` 已新增 `create_custom_voice` / `query_custom_voice_task` / `wait_custom_voice` / `delete_element` / `list_preset_voices` / `list_all_preset_voices` 六个方法
- 注册流程：`src/register_elements.py` 里的 `_register_one`——`line 70` 已有 `voice_id=getattr(entry, "voice_id", None)`，schema 需确认 `AssetEntry` 有 `voice_id` 字段（`src/schemas.py`）
- MiniMax T2A 目前是内联脚本，后续应提炼成 `src/voice_studio.py`

### 5.2 Shot 07 微测（音色绑定完成后才跑）

**背景**：48 小时剧本第 7 镜头，6 秒 OTS 过肩镜头，Boss 对 Client 说英文台词 `"I didn't bring slides. I built the actual system."`。用到 4 个 element：Boss、Client、meeting_room、laptop，**全部已注册**。

**剧本所在**：`~/Desktop/ai-video/drafts/nocoly-48h/storyboard.md` 第 306-336 行（Shot 07 完整描述）

**预估成本**：6s × 0.8 元 = **4.8 元**

**操作**：
1. 在 `kling-studio/projects/` 下新建 `nocoly-48h-shot07/`（或类似名字）
2. 写 `storyboard.yaml`（meta + 1 个 batch + 1 个 shot）
3. `python -m src.generate_video run projects/nocoly-48h-shot07 --dry-run` 校验
4. `python -m src.generate_video run projects/nocoly-48h-shot07` 出片
5. 听成片——重点听：**Boss 的台词发音是否清晰、音色是否符合预期、嘴型同步如何、Client 表情反应**

**这条数据对文章的价值**：
- 证明 element + voice_id 的组合能处理"带台词的复杂镜头"
- 证明 Kling 能念英文台词
- 实测数据：嘴型同步程度、发音准确度、语气自然度——全部写进文章的第四/五部分
- 如果不理想，就是文章里"现存问题"的诚实记录（保留批判性，不写成广告）

### 5.3 M5 多 batch 拼接（可选，看时间）

**背景**：48 小时剧本 11 个镜头共 55 秒，**超过 Omni 单次 6 shot 上限**。必须拆成 2 个 batch：
- batch 1：Shot 00-05（office_night 部分，6 个镜头，29 秒）
- batch 2：Shot 06-10（meeting_room + end_card 部分，5 个镜头，26 秒）

**待实现**：`src/stitch.py` 用 ffmpeg concat demuxer 无损拼接两段 batch，**保留音轨**。不要重编码。

**参考路径**：plan 文件在 `~/.claude/plans/compiled-dreaming-castle.md` 里有 M5 章节。

**对文章的价值**：展示"如何突破单次请求限制做更长视频"，是给技术读者的硬货。

### 5.4 M6 完整 48h 剧情片（终极验收）

等 M5 拼接做好之后，跑完整 55 秒的 nocoly-48h。**预估成本约 44 元**，是截稿前最大一笔支出。成片直接作为文章的压轴案例。

---

## 六、用户 / 品牌信息（写作必知）

- **姓名**：Andy Lei（雷明灿）
- **个人品牌**：微信公众号「雷码工坊笔记」
- **职位**：明道云 CMO / nocoly 营销负责人
- **风格定位**：专业但不失亲切；有观点；不堆砌术语；实战导向；愿意写"失败和踩坑"
- **nocoly 品牌定位**：明道云的海外子品牌，2026 核心目标是东南亚华人中大型企业 IT / 运营部门，落地模式靠本地合作伙伴（香港富士施乐等）
- **写作基调**：这是 Andy 的"工坊笔记"，不是官方稿件。写得像在跟一个同行朋友聊自己的实验过程，技术细节认真、观点鲜明、承认失败、不吹。

**一些可以贯穿全文的小主张**：
- "把 AI 能力理解为基础设施，而不是魔法"
- "工程化的价值在于'可复现'——一个人能跑通的东西，团队就能跑通"
- "给 AI 一个身份证，它就记得住你是谁"（Element 的隐喻）

---

## 七、重要的"不要"清单

文章成稿过程中要避开的坑：

- ❌ **不要**读 `~/Desktop/articles/` 下任何其他文章，按 `CLAUDE.md` 规定走
- ❌ **不要**引用旧的 `ai-video/article/` 系列 4 篇日志——本文独立成篇
- ❌ **不要**在文章里给即梦、ViMax、moviepy 做对比攻击——既然选了可灵就大大方方讲可灵，不要贬低别家
- ❌ **不要**过度营销可灵——这是雷码工坊笔记的实战复盘，不是 Kling 的软文
- ❌ **不要**省略成本数据——精确到元的成本是这篇文章的价值锚点之一
- ❌ **不要**省略"失败和局限"——屏幕文字乱、mode 默认、单次 6 shot 上限、时长上限，都要写
- ❌ **不要**把代码塞进文章——只放关键片段（大约 3-5 段），完整代码引导读者去 GitHub / 私信
- ❌ **不要**在正文里用表情符号（`~/Desktop/articles/WRITING.md` 应该有规范，以它为准）
- ❌ **不要**先写英文再翻译中文——直接写中文，英文稿后做（如果要做的话）

---

## 八、新对话的启动清单（Copy 以下给新对话）

```
你好，我要继续写 /Users/andy/Desktop/articles/ai-long-video-consistency/article.md 这篇文章。

请按顺序做这些事：

1. 读 /Users/andy/Desktop/articles/CLAUDE.md（仓库级规则）
2. 读 /Users/andy/Desktop/articles/WRITING.md（写作风格指南）
3. 读 /Users/andy/Desktop/articles/ai-long-video-consistency/handoff.md（本项目的完整交接）
4. 按 handoff.md 里的建议大纲，先写第一部分+第二部分的初稿到 article.md
   （这两部分不依赖未完成的技术工作，可以立刻动笔）

写作时：
- 不要读其他已有文章（仓库规则明确禁止）
- 不要扫描项目目录（仓库规则明确禁止）
- 严格按 WRITING.md 的风格规范
- 草稿不要贪多，先写 1500 字看效果
- 写完后回来问我要不要调整再继续下一部分
```

---

## 九、技术决策与原则（从原对话抽取，避免新对话重复讨论）

原对话里已经达成共识的事，直接当作既定事实：

1. **可灵 Omni Video 的多镜头模式**是长视频一致性的决定性能力
2. **Element 主体管理**是跨视频一致性的决定性能力
3. **`sound: on`** 让整个"后期配音 / BGM"环节消失
4. **`kling-v3-omni` + `std` 模式 + `sound:on`** 是当前性价比最优组合
5. **本地 `registry.json` 是真相源**，Kling 服务端状态要定期对账（`list --remote`）
6. **COS 上传即删除**是本项目的强制契约
7. **一个 batch ≤ 6 shot ≤ 60s** 是 Omni Video 的硬约束
8. **描述字段 ≤ 100 字符** 是 Kling Element 创建的硬约束（文章里写时引用这个踩坑点）
9. **新项目围绕可灵从零搭建**，不在旧的 ai-video/ 上打补丁
10. **旧的 ai-video/drafts/nocoly-partner-drama/ 已删除**，不再引用
11. **Kling 有两套互不相通的 voice_id 命名空间**（2026-04-11 踩坑发现）：
    - `/v1/general/presets-voices` 返回的"官方预设音色"（形如 `829826792415842333`，全是字符串化的大数字）→ **可以**作为 `element_voice_id` 绑定到 element
    - `/v1/audio/tts` 文档里用的"TTS 音色"（形如 `oversea_male1` / `uk_man2`）→ **不能**作为 `element_voice_id`，POST 元素创建时会返回 `HTTP 400 code=1201 "Invalid voice id"`
    - 这意味着：element 的语音只能从 **"大数字 ID"** 空间里取，而这个空间非常小（只有 5 个中文预设音色）。想要英文音色 = **必须走自定义克隆**（`POST /v1/general/custom-voices`），没有第三条路

---

## 十、一行总结

**上一轮做完了 kling-studio 的 M1→M4（脚手架→客户端→元素注册→单 batch 出片流水线），花 8 元出了一条 10 秒的一致性烟测视频。接下来的工作分两条线：一条是继续把 kling-studio 跑到 M6（音色→Shot 07→M5→M6 完整片），一条是把这套经验写成 5000 字的公众号长文。两条线互相喂素材。**

写得好的话，这篇文章本身就是读者可以照着跑一遍的工程手册。

---

## 附：环境参考

- **项目根**：`~/Desktop/kling-studio/`
- **venv**：`~/Desktop/kling-studio/.venv/`（写代码前 `source .venv/bin/activate`）
- **环境变量**：`~/Desktop/kling-studio/.env`（含 KLING_ACCESS_KEY_ID / KLING_SECRET_ACCESS_KEY / COS_*）
- **Kling 账号**：上海万企明道软件有限公司（Andy Lei 的工作账号）
- **API 文档源**：`~/Desktop/api-docs/kling/docs/`
- **旧项目**（不动）：`~/Desktop/ai-video/`
- **plans 文件**：`~/.claude/plans/compiled-dreaming-castle.md`（原始规划文档，含 M1-M6 全景）

祝写作顺利。

---

## 十一、音色绑定的曲折故事（文章可直接取用的原始素材）

> **给写作者**：这一节记录 2026-04-11 发生的音色绑定反转过程。它本身就是一段完整的剧情——"以为的路走不通 → 被迫另辟蹊径 → 撞上意外的便宜 → 反而更有工程美感"。这条故事线价值两点：(1) 展示 AI 工具链组合的真实工程代价，(2) 让文章不是"一路顺风的说明书"，而是"一段真实的探索过程"。建议在文章第五部分"现存问题"里**单独开一章 600-800 字**，或者作为第三部分"从零搭 kling-studio"之后的**外传彩蛋**。
>
> 下面所有数据点、API 响应码、扣费金额都是真实的，可直接引用。

### 11.1 故事概览（一句话版）

原计划从 Kling 官方预设音色池里挑两个英文男声绑定给 Boss 和 Client。实际执行时发现 Kling 官方预设池**只有 5 个音色全是中文**，而文档里另一处出现的"英文音色 ID"（`oversea_male1` 等）被 Kling 接口硬拒 `Invalid voice id`。不得不回去重新搭管线：用 **MiniMax 海螺语音**合成一段 12 秒的英文音频样本，上传到**腾讯 COS** 拿到临时 URL，再调 **Kling 的 `POST /v1/general/custom-voices`** 把它克隆成 Kling 自己的自定义音色，最后才能绑给 element。意外之喜是——**Kling 克隆每条只扣 0.05 元**，比原本担心的贵 100 倍的定价便宜到可以忽略。

### 11.2 时间线（实际发生顺序）

| 步 | 动作 | 结果 |
|---|---|---|
| 1 | 按 handoff 第四节第 1 步，在 `kling_client.py` 加 `list_preset_voices()` 方法封装 `GET /v1/general/presets-voices` | 代码通过 |
| 2 | 跑 `list_all_preset_voices()` 拉全量预设音色 | 只返回 **5 条**：钓系女友 / 温柔女声 / 播报男声 / 盐系少年 / 撒娇女友 —— **全部中文** |
| 3 | 确认这 5 条是 Kling "可以绑到 element 的预设音色"池的全部内容（翻页到头） | 英文路径没有任何候选 |
| 4 | 想起 `apiReference_model_TTS.md` 里出现过 `voice_id: "oversea_male1"` + `voice_language: "en"`，以为是同一个音色池 | 假设先行 |
| 5 | WebSearch 找到 fal.ai 的 Kling TTS 镜像 API 文档，拿到完整 TTS voice_id 枚举 | 发现 6 个英文音色：`oversea_male1` / `reader_en_m-v1` / `commercial_lady_en_f-v1` / `uk_boy1` / `uk_man2` / `uk_oldman3` |
| 6 | 同一条测试脚本里并发测：Kling 中文预设 `829826792415842333` + TTS 枚举 `oversea_male1` 各创建一个 element | 中文预设 **✅ 接受**；`oversea_male1` **❌ 被拒**：`HTTP 400 code=1201 "Invalid voice id: oversea_male1"` |
| 7 | 推论：**Kling 有两套 voice_id 命名空间**。TTS 的命名化 id（`oversea_male1`）只能用于 `/v1/audio/tts`，不能作为 `element_voice_id`。想给 element 装英文音，唯一的路是自定义克隆 | 结构性结论 |
| 8 | 跟用户同步发现，并抛出一个关键假设："Kling voice_id 只是音色模板，语种跟 prompt 文本走。用中文音色 + 英文台词会不会直接得到英文发音？" | 这个假设后来没测，因为第 9 步直接给出了更好的答案 |
| 9 | 用户问："有哪些网站能生成声音 + 有 API？我可以用来做 Kling 克隆的源。"整理对比 ElevenLabs / MiniMax / PlayHT / OpenAI TTS / Google / Azure 等 | 推荐 MiniMax 作为主选：亚洲人说英文的底子好、API 便宜、有 Voice Design |
| 10 | 用户给 MiniMax API key → 扫 `~/Desktop/api-docs/minimax/docs/`，发现 `English_Trustworthy_Man` / `English_Diligent_Man` / `English_Gentle-voiced_man` 等 **16 个英文系统音色直接可用**，根本不需要走 Voice Design | 省一道复杂度 |
| 11 | 跑 `POST /v1/t2a_v2` 合成一段 12 秒的英文台词（"I didn't bring slides..."）→ `English_Trustworthy_Man` → 11.988 秒 mp3 / 193 KB / 0.07 元 | 连通性通过 |
| 12 | 同一脚本并行生成 `English_Diligent_Man` 和 `English_Gentle-voiced_man` 两条作为候选对比 | 三个样本横向对比 |
| 13 | 用户听完后拍板：**Boss = gentle，Client = trustworthy**（和"Trustworthy 适合 Boss"的原始直觉相反，用户选了 gentle 给 Boss） | 决策 |
| 14 | 探价：把 gentle.mp3 上传到腾讯 COS 拿临时 URL，调 `POST /v1/general/custom-voices` 做 Kling 克隆，轮询到成功读 `final_unit_deduction` | 扣费 **0.05 元**，10 秒内完成 |
| 15 | 下载 Kling 克隆版的 trial wav 给用户听，检验三点：①说的是英文还是中文 ②音色是否保留 ③清晰度 | 用户确认："1.是英文 2.声音相似 3.清晰自然" |
| 16 | 同样流程再跑 Client 的 trustworthy 克隆 | 又一条 0.05 元，拿到第二个 voice_id |

### 11.3 最终拿到的两个 Kling voice_id（都是 custom cloned）

- **Boss** → `871830494903013460`（源：MiniMax `English_Gentle-voiced_man`）
- **Client** → `871832297002659873`（源：MiniMax `English_Trustworthy_Man`）

两条 Kling 克隆 API 响应的 `owned_by` 字段都是 `871235376517124150`——这是 Kling 账号自身的 ID，而不是 `"kling"` 字符串，这一点确认了它们是"属于我的自定义音色"，而不是预设池的条目。这个细节可以用在文章里说明 **"Kling 把自定义音色和预设音色做了来源标签区分"**。

### 11.4 成本全账（截至音色绑定阶段）

| 项 | 次数 | 单价 | 小计 |
|---|---|---|---|
| MiniMax T2A 合成样本（Boss 候选 × 1） | 1 | ~0.07 元 | 0.07 |
| MiniMax T2A 合成样本（Client/Boss 备选 × 2） | 2 | ~0.07 元 | 0.14 |
| Kling 克隆（Boss） | 1 | 0.05 元 | 0.05 |
| Kling 克隆（Client） | 1 | 0.05 元 | 0.05 |
| **音色绑定阶段总支出** | | | **约 0.31 元** |

加上 M1→M4 烟测的 8 元，**全项目累计花费约 8.3 元**。

### 11.5 技术洞见（可以作为文章金句的素材）

- **金句候选 1**：*"以为是一道题，其实是两张表。"* —— Kling 的 `element_voice_id` 字段和 `/v1/audio/tts` 的 `voice_id` 字段看起来是同一个类型，但它们属于**两张互不相通的表**。文档没有明说，所以第一次尝试 `oversea_male1` 的人会 100% 被 `Invalid voice id` 绊倒。
- **金句候选 2**：*"一条假设走不通，不要硬撞。换一家供应商做桥，往往更便宜。"* —— 原本以为 Kling 预设池不够用就要退回自己录音；实际解法是让 **MiniMax 合成 → Kling 克隆**，两家供应商组合，反而只花了 0.3 元。
- **金句候选 3**：*"最贵的不是 API 费用，是以为它贵的恐惧。"* —— 克隆之前我担心每条 50-100 元，结果是 0.05 元。敢不敢先跑一次比单价本身重要。
- **工程价值观**：两个独立服务拼成的管线（MiniMax T2A → COS → Kling custom-voices → element_voice_id）看上去比"单家搞定"丑，但它**强制我们把流程拆成可验证的阶段**——每一步都能独立测试、独立回滚、独立替换。写文章时可以强调这个"丑但可维护"的美感。
- **偶然收获**：MiniMax 提供了一个看起来就是为这个场景准备的 `POST /v1/voice_design` 接口——用自然语言描述音色（"40 岁新加坡华人科技创始人，讲英文，声音沉稳"），9.9 元直接生成一个新音色。**这次用不上因为系统音色够用**，但下次如果要做更多角色就有现成工具。

### 11.6 适合在文章里做的对比图 / 截帧

1. **命令行截图**：`python -m src.register_elements list --remote` 的输出，显示 7 个 element 注册状态对账通过（在 element 重建之前留一张，element 重建之后再留一张，对比 Boss/Client 从 `307840124555148 → 新 id` 的变化）
2. **代码片段**：`kling_client.py` 的 `create_custom_voice` 方法（不超过 20 行），作为文章里"音色绑定如何 API 化"的示例
3. **响应 JSON 片段**：Kling 克隆任务 `data.task_result.voices[0]` 这一段，特别框出 `final_unit_deduction: "0.05"` —— 让"五分钱"这个数字有视觉证据
4. **本地文件对比**：`_minimax_test_gentle.mp3` vs `_kling_clone_trial_boss_gentle.wav` 的波形图截图（用 Audacity 开一下就行），展示两者的音色相似性
5. **架构图**：一张很简单的流水线图 `本地描述 → MiniMax T2A → 本地 mp3 → 腾讯 COS → Kling custom-voices → Kling voice_id → Kling element`，作为"桥接管线"这一节的开头

### 11.7 素材清单（给文章拍图截帧用）

`~/Desktop/kling-studio/assets/voices/` 目录下现存的文件（都是这次探索过程里真实生成的）：

```
_minimax_test_trustworthy.mp3       # MiniMax English_Trustworthy_Man 合成，12s，Client 源音色
_minimax_test_diligent.mp3          # MiniMax English_Diligent_Man 合成，12.6s，备选未采用
_minimax_test_gentle.mp3            # MiniMax English_Gentle-voiced_man 合成，12s，Boss 源音色
_kling_clone_trial_boss_gentle.wav  # Kling 克隆成功后返回的试听 wav（Boss）
_kling_clone_trial_client_trust.wav # Kling 克隆成功后返回的试听 wav（Client）
```

这些本地 mp3/wav 文件可以在文章里作为超链或二维码引用（"扫码听样本 vs 克隆版对比"这种互动点子）。

### 11.8 写作建议

- 不要把这一节写成干巴巴的 API 技术文档。它是一段探索故事，情绪是"以为很顺 → 撞墙 → 灵机一动 → 撞到彩蛋"。保留情绪起伏。
- 可以把**假设 → 测试 → 反驳**这三段循环作为结构骨架，让技术读者感受到"工程的本质是证伪"。
- `Invalid voice id` 这个错误码是整篇文章的一个**情绪支点**——可以把它作为"看起来简单实则踩坑"的代表，让非技术读者也能共情"API 文档没说清楚的地方往往是最贵的时间"。
- 别回避"方案 A 崩了"这个失败。失败本身就是这篇文章区别于广告软文的关键差异点。

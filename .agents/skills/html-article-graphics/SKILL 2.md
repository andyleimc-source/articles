---
name: html-article-graphics
description: 文章 HTML 自制概念图标准流程（雷码工坊 Notion-flat 风）。当文章需要单张结构图/时间线/对照图/迁移图/引用卡/人物脉络图时使用——手写 HTML + headless Chrome 截图，不走生图模型。触发词：概念图、示意图、时间线、对照图、HTML 配图、结构图。
---

# HTML 文章配图标准（雷码工坊）

> 2026-07-02 定稿（《从「少即是多」到「值得信任」》一文实战沉淀）。
> 定位：**单张**信息结构图用本 skill；**系列多张统一版式卡片**（小红书 9 宫格等）仍必须走 `baoyu-image-cards`；**封面 / 纯视觉隐喻图**走 Seedream 5.0（baoyu-imagine）。

## 什么时候用 HTML（而不是生图模型）

文字密集、结构精确的图 = HTML。生图模型出这类图必错字，HTML 100% 可控、免费、可复现改字。

适用类型：时间线 / 人物脉络（可嵌真实照片头像）、概念迁移图（A→B→C）、新旧对照表（旧划掉→新高亮）、大字引用卡、流程/层级示意。

## 硬性规格

1. **竖版 900×1200（3:4），禁止横版**——读者在手机上看，横版缩到全宽后字太小（2026-07-02 老雷实测拍板）
2. **单一字体家族，整图不许混**：`font-family:"PingFang SC","Hiragino Sans GB",sans-serif`，中文、英文、数字全走这一套。**禁止** Georgia / Songti SC / 任何衬线体混排（2026-07-02 老雷反馈：同一批图字体不一致）。层级靠字重（400/600/700/800）和字号做，不靠换字体
3. **字号下限（900px 宽画布）**：主标题 ≥40px，节点名/卡片题 ≥26px，正文/注释 ≥18px，来源行可 14px
4. **品牌色 token（禁止其他色）**：
   ```css
   --paper:#FAF7F0;  /* 背景，一律米白 */
   --ink:#0E1116;    /* 标题/主线条，禁纯黑 */
   --green:#1AB87C;  /* 强调/高亮/现在时态，点状使用 */
   --graphite:#3A4151; /* 正文 */
   --mist:#9CB4CC;   /* 箭头/薄边框/次要 */
   --brick:#6E6259;  /* 来源行/辅助 */
   ```
   关键规则：**结构由墨黑撑起，亮点由磷绿点燃**——磷绿只做信号点（高亮带、竖条、徽章、现在卡），不做大面积填充
5. **水印**：按 CLAUDE.md 默认加「雷码工坊笔记」右下角小字；老雷对某篇明确说不要时整篇不加
6. **反模板（taste 原则）**：禁紫渐变、居中三等分卡+图标、通栏 hero。用编辑排版：左对齐大字、非对称、留白、细分隔线、`↓`/`↳` 做流向

## 惯用组件（已验证好看）

- **绿描边 pill 标签**（图左上角小分类：`溯 源`/`三次迁移`）
- **人物节点**：圆头像（`background-image` + `background-size/position` 对准脸，别用 object-fit）+ 名字 + 灰色小身份 + 一句贡献；纵向串在一条 2.5px mist 竖线上，主角节点换磷绿描边
- **现在卡**：磷绿 2.5-3px 边框 + 右上 `现 在` 磷绿徽章 + `box-shadow:7px 7px 0 rgba(26,184,124,.14)`
- **旧→新对照行**：旧词石墨色 `<s>` 划掉，`↳`，新词大号加粗 + 磷绿荧光带 `background:linear-gradient(transparent 64%, rgba(26,184,124,.32) 64%)`
- **真实照片素材**：Wikimedia Commons 下载（curl 带 UA），进图前肉眼核对；来源行写在图底部 brick 色小字

## 产出流程

1. 源码存 `<article-dir>/image/html/<name>.html`，body 定宽 `width:900px;height:1200px;overflow:hidden`
2. 渲染（2x 采样再压回 1200，字更利）：
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
     --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
     --window-size=900,1200 --screenshot="$PWD/01-name.png" "file://$PWD/html/name.html"
   sips --resampleHeightWidthMax 1200 01-name.png
   ```
3. 产物命名 `01-xxx.png` 按文中出现顺序编号，放 `image/`
4. **每张渲染完必须 Read 肉眼核对**：字有没有截断/溢出、头像有没有圈错位置、字体是否统一
5. 登记 `image_describe.md`（内容 / 与论点关系 / 来源）

## 插入正文

- `![](image/01-xxx.png)` + 空行 + `<p align="center"><em>图注</em></p>`（图注贴图、小字、砖灰由 `scripts/md-to-wechat-html.py` 自动处理，不用手调）
- 概念图不一定要图注；照片必须带来源图注

## Checklist（出图前过一遍）

- [ ] 竖版 900×1200
- [ ] 全图一个字体家族（无 Georgia/Songti）
- [ ] 只用 6 个品牌色 token
- [ ] 主标题 ≥40px、正文 ≥18px
- [ ] 磷绿只做点状信号
- [ ] 渲染后逐张肉眼核对
- [ ] 水印按当篇要求

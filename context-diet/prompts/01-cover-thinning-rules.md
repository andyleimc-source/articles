# 封面图 Prompt — context-diet

**用途**：`cover.png`，16:9，文章顶部封面
**模型**：Seedream 5.0（`doubao-seedream-5-0-260128`）— 目前唯一能稳定写对中文短句的
**风格锚点**：Notion 扁平插画风 + 雷码工坊品牌色（见 `BRAND.md`）
**调用方式**：skill `baoyu-cover-image`（**禁止自己撸 SVG + rsvg 合成**）

---

## 概念

一摞厚厚的规则文档，上面四分之三的纸张淡出成雾蓝色半透明轮廓，底部剩下薄薄几张墨黑实心的纸，纸上有磷绿的小标记。视觉上一眼读出「大部分被删掉了，留下的是硬货」。

备选概念（若主稿不理想）：两个方向相反的磷绿箭头在一份文档上对撞 → 表达「两条规则在打架」。

---

## 主 Prompt（英文，供 Seedream）

```
Flat Notion-style editorial illustration, 16:9 horizontal.

A tall stack of paper documents on a warm off-white background. The upper
three quarters of the stack are dissolving into pale misty-blue translucent
outlines, gently fading away like they are being erased. The bottom quarter
remains solid ink-black paper with crisp edges, a few small phosphor-green
marks on those remaining sheets indicating what was kept.

Style: flat vector illustration, soft pastel palette, hand-drawn slightly
irregular outlines, simple geometric shapes, generous white space, subtle
paper grain texture, warm and friendly, editorial magazine feel.

Color palette (strict): background warm off-white #FAF7F0, main outlines and
solid paper ink-black #0E1116, accent and marks phosphor-green #1AB87C,
secondary labels graphite #3A4151, faded translucent sheets misty-blue #9CB4CC,
shadows brick-grey #6E6259.

Text in image: the Chinese characters 「删掉一半」 in ink-black, placed in the
upper left area, clean sans-serif, large but not dominating. Small watermark
「雷码工坊笔记」 in the bottom-right corner, graphite #3A4151 at about 65%
opacity, roughly 7% of image width, no icon, no border, small margin from edges.

Chinese glyphs must render correctly, no garbled characters, no fake-looking
CJK, kerning correct.

Avoid: photorealism, 3D render, cyber neon, purple gradients, blue tech
gradients, orange or coral tones, pure black #000, marketing hero style,
busy composition.
```

---

## 字数自查（Seedream 安全区）

| 项 | 内容 | 字数 | 限制 |
|---|---|---:|---|
| 主标题 | 删掉一半 | 4 | 单行 ≤10 ✓ |
| 水印 | 雷码工坊笔记 | 6 | 固定 ✓ |
| **合计** | | **10** | 整图 ≤40 ✓ |

无代码块、无长句、无英文 ALWAYS/NEVER 列表 ✓

---

## 出图后必做

1. 肉眼逐张核对中文字形，有错字就重抽（Seedream 也会偶发）
2. 水印没渲染对 → 回退 ImageMagick 后处理叠加
3. `sips --resampleHeightWidthMax 1200 cover.png` 压到长边 ≤1200px、≤1MB，否则公众号剪贴板粘贴会静默失败
4. 正文顶部用 `<img src="cover.png">`，公众号封面需手动上传

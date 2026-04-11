# Claude Code 培训 PPT 设计规范

> 来源：Claude Code 培训课件 · 2026 版 PPT 设计风格文档
> 最后更新：2026-04-06

---

## 一、设计哲学

**关键词：克制、精准、专业**
- 不堆砌装饰，用色极简
- 留白充足，信息层次清晰
- 每页一个核心信息，不超过 3 个内容模块
- 深色主题为主，适合投影和屏幕演示

---

## 二、色彩系统

### 主色板

| 色名 | 色值 | 用途 |
|------|------|------|
| **主紫** `a` | `#7c85fa` | 标题强调、编号、重点边框 |
| **次紫** | `#a5b4fc` | 次级强调、辅助元素 |
| **橙** `w` | `#f08c4a` | 警告、点缀、对比 |
| **蓝** `b` | `#5aa0f5` | 信息、链接、说明 |
| **青** `g` | `#3fc99e` | 成功、积极、开始 |
| **红** `r` | `#f06060` | 危险、删除、禁止 |
| **灰** `m` | `#5a6578` | 次要文字、辅助信息 |
| **白** `h` | `#eef1f6` | 主要文字、标题 |
| **深夜黑蓝** | `#0f1117` | 页面背景（主） |
| **卡灰** | `rgba(255,255,255,0.025)` | 卡片背景 |

### CSS 变量速查

```css
.a  { color: #7c85fa; }   /* 主紫 */
.w  { color: #f08c4a; }   /* 橙 */
.b  { color: #5aa0f5; }   /* 蓝 */
.g  { color: #3fc99e; }   /* 青 */
.r  { color: #f06060; }   /* 红 */
.m  { color: #5a6578; }   /* 灰 */
.h  { color: #eef1f6; }   /* 白文字 */
```

---

## 三、字体系统

### 字体栈

```css
font-family: "苹方", "PingFang SC", "SF Pro Text",
             "Helvetica Neue", Arial, sans-serif;
```

### 字号层级

| 元素 | 字号 | 字重 | 示例 |
|------|------|------|------|
| 页面主标题 h1 | `3.1em` | 900 | Claude **Code** |
| 副标题 h2 | `1.85em` | 700 | 核心概念 |
| 正文 p / li | `1.05em` | 400 | 说明文字 |
| 编号数字 .bn | `2.1em` | 900 | **01** |
| 步骤编号 .sn | `1.75em` | 900 | **①** |
| 代码 code | `0.88em` | 400 | `claude` |
| 徽章 .badge | `0.6em` | 700 | MUST KNOW |
| 标签 .ls | `0.63em` | 700 | # 安装命令 |

### 行高规则
- 标题：`1.0 ~ 1.15`
- 正文：`1.65`
- 代码块：`1.4`

---

## 四、组件库

### 1. 顶栏 `.topbar`
每页顶部 3px 渐变细条，区分章节。
```css
.topbar {
  position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #7c85fa, #5aa0f5 50%, #f08c4a);
}
```
**用法：** 每页顶部放一个 `<div class="topbar" style="background:..."></div>`

---

### 2. 徽章 `.badge`
标签式小标牌，用于标注页面类型。
```css
.badge {
  display: inline-block;
  font-size: 0.6em; font-weight: 700;
  letter-spacing: 0.1em; text-transform: uppercase;
  padding: 0.3em 0.85em; border-radius: 9999px;
  border: 1px solid; margin-bottom: 0.9em;
}
```
**配色变体：**
- `.bp` 主紫蓝调
- `.bo` 橙调（Why 类）
- `.bg` 青绿调（Go/Installation 类）
- `.bb` 蓝调（Tools/Compare 类）
- `.br` 红调（警告/注意类）

---

### 3. 卡片 `.card`
信息聚合容器。
```css
.card {
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 8px;
  padding: 0.65em 1em; margin-bottom: 0.6em;
}
```
**左边框变体（最常用）：**
- `.ca` → `border-left: 3px solid #7c85fa;`（主紫）
- `.cw` → `border-left: 3px solid #f08c4a;`（橙）
- `.cb` → `border-left: 3px solid #5aa0f5;`（蓝）
- `.cg` → `border-left: 3px solid #3fc99e;`（青）

**顶边变体：**
- `.card-top-a` → `border-top: 3px solid #7c85fa;`（四格布局）

---

### 4. 大编号 `.bn`
醒目数字，用于编号列表。
```css
.bn {
  font-size: 2.1em; font-weight: 900;
  line-height: 1; color: #7c85fa;
  font-family: "SF Pro Display", Arial, sans-serif;
}
```
**配色变体：**
- `.bn` 默认主紫
- `.bnw` 橙色
- `.bnb` 蓝色
- `.bng` 青色

---

### 5. 步骤块 `.step`
左侧大编号 + 右侧内容。
```html
<div class="step">
  <div class="sn">01</div>
  <div class="sb">
    <p class="t">步骤标题</p>
    <p>说明文字</p>
  </div>
</div>
```

---

### 6. 代码块 `pre + code`
```css
code {
  font-family: "SF Mono", Menlo, monospace;
  font-size: 0.88em; color: #5aa0f5;
  background: rgba(90,160,245,0.08);
  padding: 0.12em 0.35em; border-radius: 4px;
}
pre {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-left: 3px solid #7c85fa;
  border-radius: 6px; padding: 0.4em 0.8em;
  margin: 0.3em 0; text-align: left;
}
pre code { background: none; border: none; padding: 0; color: #dde4ee; }
```

---

### 7. 网格系统

**两栏 `.g2`** — 适合 2/4 项并列：
```css
.g2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0.7em; }
```

**四栏 `.g4`** — 适合 4 项并列：
```css
.g4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.6em; }
```

---

### 8. 分栏布局 `.cols`
左 + 中 + 右三块并排：
```css
.cols { display: flex; gap: 1.8em; align-items: flex-start; }
.cols > * { flex: 1; }
.cols .cen-col { flex: 0 0 auto; align-self: center; text-align: center; }
```

---

## 五、页面布局模板

### 模板 A：标题 + 内容
```
[顶栏渐变条 - 3px]
[徽章 badge]
[h2 大标题]
[内容区 - 卡片/网格/步骤列表]
```

### 模板 B：居中金句/章节页
```
[顶栏渐变条]
[背景光晕装饰 div - 可选]
[div.cen 垂直水平居中]
  h1 超大标题
  p 副标题/说明
```

### 模板 C：对比页
```
[cols 三栏布局]
  左：传统方式（删除线灰色）
  中：箭头 + 标注
  右：AI 方式（彩色高亮）
```

---

## 六、翻页交互（纯 JS，无依赖）

```javascript
var cur = 1, total = 16;
function go(n) {
  var s = document.getElementById('s'+cur);
  cur = (cur - 1 + n + total) % total + 1;
  var ns = document.getElementById('s'+cur);
  if (s) s.classList.remove('active');
  if (ns) ns.classList.add('active');
  document.getElementById('cur').textContent = cur;
}
document.addEventListener('keydown', function(e) {
  if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); go(1); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); go(-1); }
});
```

---

## 七、顶栏渐变配色参考

| 章节类型 | 渐变色 |
|----------|--------|
| 封面/综合 | `#7c85fa` → `#5aa0f5` → `#f08c4a` |
| Why（为什么）| `#f08c4a` → `#7c85fa` |
| Compare（对比）| `#7c85fa` → `#5aa0f5` |
| Phase 1 环境 | `#3fc99e` → `#5aa0f5` |
| Installation | `#3fc99e` → `#7c85fa` |
| 警告/注意 | `#f06060` → `#f08c4a` |
| Go（开始）| `#3fc99e` → `#7c85fa` |
| 金句 | `#f08c4a` → `#fcd34d` |

---

## 八、文件信息

- **文件**：`Claude Code培训-乔布斯风PPT.html`
- **尺寸**：响应式（100vw × 100vh）
- **依赖**：零外部依赖（纯 HTML/CSS/JS）
- **字体**：苹方（系统内置）
- **翻页**：键盘 ← → / 空格；右下角按钮
- **适用**：macOS / Windows / Linux

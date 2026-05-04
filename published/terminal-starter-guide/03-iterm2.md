# 03 · iTerm2 配置 / iTerm2 Setup

> iTerm2 是 macOS 上最流行的终端模拟器，功能远超系统自带的 Terminal.app。  
> iTerm2 is the most popular terminal emulator for macOS, far more powerful than the built-in Terminal.app.

---

## 安装 / Installation

**方法一：官网下载 / Download from website**  
前往 [iterm2.com](https://iterm2.com) 下载安装包。

**方法二：Homebrew（推荐）/ Via Homebrew (recommended)**

```bash
brew install --cask iterm2
```

---

## 推荐字体 / Recommended Font

普通等宽字体在使用 Oh My Zsh 等主题时无法显示特殊图标，推荐安装 **Nerd Font**：  
Standard monospace fonts can't render special icons used by themes. Install a **Nerd Font**:

```bash
brew install --cask font-meslo-lg-nerd-font
```

安装后在 iTerm2 中设置：  
After installing, set in iTerm2:

`Preferences → Profiles → Text → Font` → 选择 **MesloLGS Nerd Font**，字号 14–16

---

## 推荐主题 / Color Themes

### Dracula（最流行）

1. 前往 [draculatheme.com/iterm](https://draculatheme.com/iterm) 下载 `.itermcolors` 文件
2. `Preferences → Profiles → Colors → Color Presets → Import`
3. 导入后选择 Dracula

### Solarized Dark（经典护眼）

`Preferences → Profiles → Colors → Color Presets → Solarized Dark`（内置，直接选择）

---

## 常用快捷键 / Keyboard Shortcuts

### 分屏 / Split Panes

| 快捷键 | 操作 |
|---|---|
| `Cmd + D` | 水平分屏（左右）|
| `Cmd + Shift + D` | 垂直分屏（上下）|
| `Cmd + [ / ]` | 在分屏间切换 |
| `Cmd + W` | 关闭当前分屏/标签页 |

### 标签页 / Tabs

| 快捷键 | 操作 |
|---|---|
| `Cmd + T` | 新建标签页 |
| `Cmd + 数字` | 切换到第 N 个标签页 |
| `Cmd + ←/→` | 左右切换标签页 |

### 编辑 / Editing

| 快捷键 | 操作 |
|---|---|
| `Ctrl + A` | 跳到行首 |
| `Ctrl + E` | 跳到行尾 |
| `Ctrl + U` | 清除当前行 |
| `Ctrl + W` | 删除前一个单词 |
| `Ctrl + R` | 反向搜索历史（配合 fzf 更强大）|
| `Cmd + F` | 在当前窗口内搜索文本 |

---

## 热键窗口 / Hotkey Window

设置一个全局快捷键，在任何应用中快速唤起/隐藏终端：  
Set a global shortcut to summon/hide the terminal from anywhere:

1. `Preferences → Keys → Hotkey`
2. 勾选 **Show/hide all windows with a system-wide hotkey**
3. 设置快捷键，推荐 `Option + Space` 或 `Cmd + `` ` ``

---

## 实用设置 / Useful Settings

### 选中即复制 / Copy on Select

`Preferences → General → Selection → ✅ Copy to pasteboard on selection`

选中文字后自动复制到剪贴板，无需 Cmd+C。

### 无限滚动 / Unlimited Scrollback

`Preferences → Profiles → Terminal → ✅ Unlimited scrollback`

防止长输出被截断。

### 静音 / Silence Bell

`Preferences → Profiles → Terminal → ✅ Silence bell`

关闭恼人的提示音。

### Shell Integration

在终端执行以下命令，启用 iTerm2 与 Shell 的深度集成（支持命令耗时、标记行等功能）：  
Run the following to enable deep shell integration (command duration, mark lines, etc.):

```bash
curl -L https://iterm2.com/shell_integration/install_shell_integration.sh | bash
```

---

## Profiles（多配置） / Profiles

可以为不同场景创建不同的 Profile，比如：  
Create different profiles for different scenarios:

- **Default**：日常开发，深色主题
- **Presentation**：大字体、高对比度，适合演示
- **SSH**：特定颜色区分远程连接

`Preferences → Profiles → +（新建）`

---

## Oh My Zsh（可选增强）/ Oh My Zsh (Optional)

Oh My Zsh 是 zsh 的配置框架，提供主题和插件：  
Oh My Zsh is a configuration framework for zsh with themes and plugins:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

热门主题：`agnoster`、`powerlevel10k`（需要 Nerd Font）

---

[← 上一章：常用命令](./02-commands.md) · [下一章：z 目录跳转 →](./04-z.md)

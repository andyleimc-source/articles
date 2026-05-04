# 05 · fzf 模糊搜索 / Fuzzy Finding with fzf

> fzf 是一个通用的命令行模糊搜索工具，安装后 `Ctrl+R` 搜索历史命令的体验将发生质的改变。  
> fzf is a general-purpose fuzzy finder. After installing it, your `Ctrl+R` history search experience will be transformed.

---

## 是什么 / What is fzf?

**fzf（fuzzy finder）** 可以接收任何列表输入，让你用模糊关键词快速筛选，结果实时预览。  
**fzf** takes any list as input and lets you interactively filter it with fuzzy keywords in real time.

没装 fzf 时的 `Ctrl+R`：只能逐条向前翻历史。  
Without fzf, `Ctrl+R` only steps backwards through history one by one.

装了 fzf 后的 `Ctrl+R`：弹出全量历史列表，输入关键词实时模糊筛选，上下箭头选择，回车执行。  
With fzf, `Ctrl+R` shows your full history with live fuzzy filtering — type anything, select, and execute.

---

## 安装 / Installation

```bash
# 1. 安装 fzf
brew install fzf

# 2. 安装 Shell 集成（关键！启用 Ctrl+R 等快捷键）
$(brew --prefix)/opt/fzf/install
```

安装脚本会询问三个问题，全部选 `y`：  
The install script asks three questions — answer `y` to all:

```
Do you want to enable fuzzy auto-completion? ([y]/n) y
Do you want to enable key bindings? ([y]/n) y
Do you want to update your shell configuration files? ([y]/n) y
```

重新加载配置：

```bash
source ~/.zshrc
```

---

## 三大快捷键 / Three Key Bindings

### `Ctrl+R` — 模糊搜索命令历史

这是最常用的功能。按下 `Ctrl+R`，输入任意关键词，即可从全量历史中模糊匹配命令。  
The most-used feature. Press `Ctrl+R`, type any keyword, fuzzy-match from your full history.

```
# 示例：搜索含 "docker run" 的历史命令
Ctrl+R  →  输入 "dkr"  →  自动匹配 docker run 相关命令
```

操作 / Controls:
- `↑↓` 或 `Ctrl+N/P`：移动选择
- `Enter`：执行选中命令
- `Ctrl+C` 或 `Esc`：取消

### `Ctrl+T` — 模糊搜索文件并插入路径

在命令行输入到一半时按 `Ctrl+T`，弹出文件选择器，选中文件后路径自动插入光标位置。  
While typing a command, press `Ctrl+T` to open a file picker — the selected path is inserted at the cursor.

```bash
# 示例：cat 后按 Ctrl+T 选择文件
cat [Ctrl+T]  →  选择 config.json  →  变成 cat ./src/config.json
```

### `Alt+C` — 模糊选择目录并跳入

按 `Alt+C`（macOS 上可能是 `Option+C`），弹出子目录列表，选择后直接 `cd` 进入。  
Press `Alt+C` to open a directory picker and `cd` into the selected folder.

---

## 基本用法 / Basic Usage

fzf 可以接收任何管道输入：  
fzf can receive any piped input:

```bash
# 从文件列表中选择
ls | fzf

# 从 git 分支中选择
git branch | fzf

# 从进程列表中 kill
ps aux | fzf | awk '{print $2}' | xargs kill

# 交互式选择并打开文件
code $(fzf)
```

---

## 预览窗口 / Preview Window

```bash
# 选择文件时预览内容
fzf --preview 'cat {}'

# 预览代码（带语法高亮，需安装 bat）
fzf --preview 'bat --color=always {}'

# 预览目录结构（需安装 tree）
fzf --preview 'tree -C {} | head -50'
```

安装 `bat`（带语法高亮的 cat）：

```bash
brew install bat
```

---

## 与 zoxide 联动 / Integration with zoxide

安装 zoxide 后，`zi` 命令会调用 fzf 实现交互式目录跳转：  
With zoxide installed, `zi` uses fzf for interactive directory jumping:

```bash
zi           # 显示所有历史目录，fzf 交互式选择，回车跳入
zi project   # 过滤包含 "project" 的目录，fzf 选择
```

这是两个工具结合的最佳使用方式之一。  
This is one of the best use cases for combining these two tools.

---

## 常用配置 / Useful Config

在 `~/.zshrc` 中添加：  
Add to `~/.zshrc`:

```bash
# 设置默认预览命令
export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border'

# Ctrl+T 使用 bat 预览（需安装 bat）
export FZF_CTRL_T_OPTS="--preview 'bat --color=always {}'"

# Ctrl+R 显示完整命令（不截断）
export FZF_CTRL_R_OPTS='--with-nth=1.. --exact'
```

---

## 快速参考 / Quick Reference

| 快捷键 / Shortcut | 功能 |
|---|---|
| `Ctrl+R` | 模糊搜索命令历史 |
| `Ctrl+T` | 模糊搜索文件，插入路径 |
| `Alt+C` | 模糊选择目录并跳入 |
| `zi` | 结合 zoxide，交互式目录跳转 |

---

[← 上一章：z 目录跳转](./04-z.md) · [下一章：Git & GitHub →](./06-git-github.md)

# 06 · Git & GitHub

> Git 是本地版本控制工具，GitHub 是托管 Git 仓库的云平台。  
> Git is a local version control tool; GitHub is a cloud platform for hosting Git repositories.

---

## Git vs GitHub

| | **Git** | **GitHub** |
|---|---|---|
| 是什么 | 版本控制系统（软件）| 代码托管平台（网站）|
| 运行在 | 你的本地机器 | 云端服务器 |
| 用途 | 记录代码历史、管理分支 | 远程备份、协作、开源分享 |
| 类比 | 本地的"存档系统" | 存档上传到的"网盘" |

---

## 安装与配置 / Install & Configure

```bash
# 安装（macOS 通常自带，或用 brew 更新）
brew install git

# 配置你的身份（提交记录中会显示）
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# 查看配置
git config --list
```

---

## 核心概念 / Core Concepts

| 概念 | 说明 |
|---|---|
| **Repository（仓库）** | 存储代码和历史记录的目录，通常含 `.git/` 文件夹 |
| **Commit（提交）** | 一次代码快照，附带说明信息 |
| **Branch（分支）** | 独立的开发线，互不影响 |
| **Remote（远程）** | 托管在 GitHub 等平台的仓库副本 |
| **Staging Area（暂存区）** | 介于工作区和提交之间的缓冲区 |

### 三个区域 / Three Zones

```
工作区 (Working)  →  暂存区 (Staging)  →  仓库 (Repository)
     git add                  git commit
```

---

## 本地工作流 / Local Workflow

### 初始化仓库

```bash
mkdir my-project && cd my-project
git init
# 输出：Initialized empty Git repository in .../my-project/.git/
```

### 查看状态

```bash
git status          # 查看哪些文件有变动
git diff            # 查看未暂存的具体改动
git diff --staged   # 查看已暂存的改动
```

### 暂存与提交

```bash
git add index.html         # 暂存单个文件
git add .                  # 暂存所有变动
git add -p                 # 交互式选择要暂存的部分

git commit -m "添加首页结构"    # 提交并附上说明
git commit -am "修复 bug"       # 暂存已追踪文件并提交（合并步骤）
```

### 查看历史

```bash
git log                     # 完整历史
git log --oneline           # 每条提交一行（简洁）
git log --oneline --graph   # 带分支图
git show abc1234            # 查看某次提交的详情
```

---

## 连接 GitHub / Connect to GitHub

### 方法一：SSH（推荐）/ SSH (Recommended)

```bash
# 1. 生成 SSH 密钥
ssh-keygen -t ed25519 -C "you@example.com"
# 一路回车使用默认路径和空密码

# 2. 复制公钥内容
cat ~/.ssh/id_ed25519.pub
# 复制输出的内容

# 3. 添加到 GitHub
# 打开 GitHub → Settings → SSH and GPG keys → New SSH key
# 粘贴公钥内容并保存

# 4. 测试连接
ssh -T git@github.com
# 输出：Hi username! You've successfully authenticated...
```

### 方法二：GitHub CLI（最简单）/ GitHub CLI (Easiest)

```bash
brew install gh
gh auth login
# 按提示选择 GitHub.com → SSH → 完成浏览器授权
```

---

## 推送到 GitHub / Push to GitHub

### 创建远程仓库并推送（GitHub CLI 最快）

```bash
# 在当前目录，一步创建 GitHub 仓库并推送
gh repo create my-project --public --source=. --remote=origin --push
```

### 手动方式 / Manual

```bash
# 1. 在 GitHub 网站创建空仓库，拿到仓库 URL

# 2. 关联远程仓库
git remote add origin git@github.com:username/my-project.git

# 3. 首次推送
git push -u origin main
# -u 设置上游，之后可以直接用 git push

# 4. 后续推送
git push
```

---

## 拉取与克隆 / Pull & Clone

```bash
# 拉取远程最新内容（与本地合并）
git pull

# 克隆已有仓库到本地
git clone git@github.com:username/repo.git
git clone https://github.com/username/repo.git
```

---

## 分支 / Branches

```bash
git branch                    # 列出本地所有分支
git branch -a                 # 包含远程分支

git checkout -b feature/login # 创建并切换到新分支
git switch -c feature/login   # 同上（新语法，推荐）

git switch main               # 切回 main 分支
git merge feature/login       # 将 feature 分支合并到当前分支

git branch -d feature/login   # 删除已合并的分支
```

---

## 常见场景 / Common Scenarios

### 撤销未暂存的修改

```bash
git restore file.txt          # 撤销 file.txt 的修改
git restore .                 # 撤销所有未暂存的修改
```

### 撤销暂存

```bash
git restore --staged file.txt  # 从暂存区移出（保留修改）
```

### 修改最近一次提交信息

```bash
git commit --amend -m "新的提交信息"
# ⚠️ 只在未推送前使用
```

### 查看某行代码是谁写的

```bash
git blame file.txt            # 每行前显示提交者和时间
```

### 查看两个提交之间的差异

```bash
git diff abc1234 def5678
git diff main feature/login
```

---

## 常用命令速查 / Quick Reference

| 命令 | 用途 |
|---|---|
| `git init` | 初始化仓库 |
| `git status` | 查看状态 |
| `git add .` | 暂存所有变动 |
| `git commit -m "msg"` | 提交 |
| `git log --oneline` | 简洁历史 |
| `git push` | 推送到远程 |
| `git pull` | 拉取远程更新 |
| `git clone <url>` | 克隆仓库 |
| `git switch -c <branch>` | 创建新分支 |
| `git merge <branch>` | 合并分支 |
| `git restore <file>` | 撤销修改 |

---

[← 上一章：fzf 模糊搜索](./05-fzf.md) · [← 返回目录](./README.md)

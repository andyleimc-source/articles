# 02 · 常用终端命令 / Common Terminal Commands

---

## 导航 / Navigation

### `pwd` — 显示当前路径 / Print Working Directory

```bash
pwd
# /Users/andy/Documents/project
```

### `ls` — 列出文件 / List files

```bash
ls              # 列出当前目录文件
ls -l           # 详细列表（权限、大小、时间）
ls -la          # 包含隐藏文件（以 . 开头）
ls -lh          # 文件大小用人类可读格式（KB/MB）
ls ~/Downloads  # 列出指定目录
```

### `cd` — 切换目录 / Change Directory

```bash
cd ~/Documents        # 进入 Documents
cd ..                 # 返回上一级
cd -                  # 返回上次所在目录（很常用！）
cd                    # 直接回到主目录
```

---

## 文件操作 / File Operations

### `mkdir` — 创建目录 / Make Directory

```bash
mkdir my-project
mkdir -p a/b/c    # 递归创建多层目录
```

### `touch` — 创建空文件 / Create empty file

```bash
touch index.html
touch a.txt b.txt c.txt   # 同时创建多个
```

### `cp` — 复制 / Copy

```bash
cp file.txt backup.txt          # 复制文件
cp -r folder/ folder-backup/    # 递归复制目录
```

### `mv` — 移动/重命名 / Move or Rename

```bash
mv old.txt new.txt              # 重命名
mv file.txt ~/Desktop/          # 移动到桌面
mv folder/ ~/Documents/         # 移动目录
```

### `rm` — 删除 / Remove

```bash
rm file.txt           # 删除文件
rm -r folder/         # 递归删除目录
rm -rf folder/        # 强制递归删除（⚠️ 不可恢复，谨慎使用）
```

> ⚠️ `rm` 删除后无法从回收站恢复，请确认后再执行。  
> ⚠️ Files deleted with `rm` cannot be recovered from Trash.

---

## 查看内容 / Viewing File Content

### `cat` — 输出文件内容 / Concatenate and print

```bash
cat README.md
cat file1.txt file2.txt   # 连续输出多个文件
```

### `less` — 分页查看（大文件推荐）/ Paged viewer

```bash
less large-file.log
# 操作：空格翻页，q 退出，/ 搜索，n 下一个搜索结果
```

### `head` / `tail` — 查看开头/结尾

```bash
head -20 file.txt     # 前 20 行
tail -20 file.txt     # 后 20 行
tail -f app.log       # 实时跟踪文件末尾（查看日志神器）
```

### `grep` — 搜索文本 / Search text

```bash
grep "error" app.log          # 搜索包含 error 的行
grep -i "error" app.log       # 忽略大小写
grep -r "TODO" ./src/         # 递归搜索目录
grep -n "error" app.log       # 显示行号
grep -v "debug" app.log       # 排除包含 debug 的行
```

---

## 系统信息 / System Info

### `ps` / `top` — 查看进程 / Process list

```bash
ps aux                    # 所有进程详情
ps aux | grep python      # 搜索特定进程
top                       # 实时进程监控（q 退出）
```

### `kill` — 结束进程 / Kill process

```bash
kill 1234         # 发送 TERM 信号（优雅退出）
kill -9 1234      # 强制杀死进程
```

### `df` / `du` — 磁盘空间 / Disk usage

```bash
df -h             # 各分区可用空间
du -sh folder/    # 查看目录占用大小
du -sh *          # 当前目录各文件/目录大小
```

---

## 网络 / Network

### `curl` — 发送 HTTP 请求 / HTTP requests

```bash
curl https://example.com                    # GET 请求
curl -O https://example.com/file.zip       # 下载文件
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com
```

### `ping` — 测试网络连通性 / Test connectivity

```bash
ping google.com       # Ctrl+C 停止
ping -c 4 8.8.8.8     # 只发 4 个包
```

### `ssh` — 远程登录 / Remote login

```bash
ssh user@hostname
ssh -i ~/.ssh/id_rsa user@192.168.1.100
```

---

## 效率命令 / Productivity

### `history` — 命令历史

```bash
history           # 列出历史命令
history | grep git  # 搜索含 git 的历史
!!                # 重复上一条命令
!ssh              # 重复最近一条以 ssh 开头的命令
```

### `alias` — 创建命令别名 / Command aliases

```bash
# 临时别名（当前 session 有效）
alias ll="ls -la"
alias gs="git status"

# 永久生效：写入 ~/.zshrc
echo 'alias ll="ls -la"' >> ~/.zshrc
source ~/.zshrc   # 重新加载配置
```

### `which` — 查找命令路径 / Locate command

```bash
which python3     # /usr/bin/python3
which git         # /usr/bin/git
```

### `man` — 查看手册 / Manual pages

```bash
man ls            # 查看 ls 的完整文档
man grep
# 操作：空格翻页，/ 搜索，q 退出
```

### `clear` / `Ctrl+L` — 清屏 / Clear screen

```bash
clear
# 或按 Ctrl+L（更快）
```

### `Ctrl+C` — 终止当前命令 / Interrupt

当命令卡住或想中断时按 `Ctrl+C`。  
Press `Ctrl+C` to interrupt any running command.

---

## 快速参考 / Quick Reference

| 命令 | 用途 |
|---|---|
| `pwd` | 当前路径 |
| `ls -la` | 列出所有文件含详情 |
| `cd -` | 返回上次目录 |
| `mkdir -p` | 递归创建目录 |
| `mv` | 移动/重命名 |
| `rm -rf` | 强制删除（慎用） |
| `tail -f` | 实时查看日志 |
| `grep -r` | 递归搜索文本 |
| `Ctrl+C` | 中断命令 |
| `Ctrl+L` | 清屏 |

---

[← 上一章：基本概念](./01-concepts.md) · [下一章：iTerm2 配置 →](./03-iterm2.md)

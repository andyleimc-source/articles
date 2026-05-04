# 01 · 基本概念 / Core Concepts

---

## Terminal vs Shell vs Console

这三个词经常混用，但其实各有所指：  
These three terms are often used interchangeably, but they mean different things:

| 术语 / Term | 含义 / Meaning |
|---|---|
| **Terminal（终端）** | 显示输入输出的窗口程序，如 iTerm2、Terminal.app |
| **Shell** | 解释并执行你输入命令的程序，如 `bash`、`zsh` |
| **Console（控制台）** | 历史概念，指物理终端设备；现代语境下与 Terminal 同义 |

**类比 / Analogy:**  
Terminal 是浏览器窗口，Shell 是浏览器引擎。你看到的是 Terminal，真正"理解"命令的是 Shell。  
Terminal is the browser window; Shell is the browser engine.

### macOS 默认使用 zsh

macOS Catalina（2019）起默认 Shell 切换为 **zsh**，之前是 `bash`。  
Since macOS Catalina (2019), the default shell is **zsh** (previously `bash`).

```bash
# 查看当前 Shell / Check current shell
echo $SHELL
# 输出：/bin/zsh
```

---

## PATH 环境变量

`PATH` 告诉系统去哪里寻找可执行程序。  
`PATH` tells the system where to look for executable programs.

```bash
# 查看 PATH / View PATH
echo $PATH
# 输出示例：/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# 查看某个命令的实际位置 / Find where a command lives
which python3
# 输出：/usr/bin/python3
```

多个路径用 `:` 分隔，系统从左到右依次查找。  
Multiple paths are separated by `:`, searched left to right.

**添加自定义路径 / Add custom path** (编辑 `~/.zshrc`):
```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

## 主目录与路径 / Home Directory & Paths

| 符号 / Symbol | 含义 / Meaning |
|---|---|
| `~` | 当前用户主目录，等同于 `/Users/你的用户名` |
| `.` | 当前目录 |
| `..` | 上一级目录 |
| `/` | 根目录（整个文件系统的起点） |

**绝对路径 vs 相对路径 / Absolute vs Relative paths:**

```bash
# 绝对路径：从根目录开始，始终指向同一位置
/Users/andy/Documents/project

# 相对路径：相对于当前所在目录
./project          # 当前目录下的 project
../other-project   # 上一级目录下的 other-project
```

---

## stdin / stdout / stderr

每个命令默认有三条数据流：  
Every command has three default data streams:

| 流 / Stream | 数字 / FD | 说明 / Description |
|---|---|---|
| **stdin** | 0 | 标准输入（键盘输入） |
| **stdout** | 1 | 标准输出（正常结果） |
| **stderr** | 2 | 标准错误（错误信息） |

---

## 管道与重定向 / Pipes & Redirection

### 管道 `|`

把前一个命令的输出作为后一个命令的输入：  
Pass the output of one command as input to another:

```bash
# 列出文件，然后过滤包含 .md 的行
ls | grep ".md"

# 查看进程列表，搜索 python
ps aux | grep python
```

### 重定向 `>` `>>`

```bash
# > 覆盖写入文件（文件不存在则创建）
echo "hello" > output.txt

# >> 追加写入文件
echo "world" >> output.txt

# 2> 将错误输出重定向到文件
command 2> error.log

# &> 将所有输出重定向到文件
command &> all.log
```

---

## 文件权限 / File Permissions

```bash
ls -l
# -rwxr-xr-- 1 andy staff 1234 Apr 7 10:00 script.sh
```

权限字符串解读 / Permission string breakdown:

```
- rwx r-x r--
│ │   │   └── 其他用户 (others): 只读
│ │   └────── 同组用户 (group): 读+执行
│ └────────── 文件所有者 (owner): 读+写+执行
└──────────── 文件类型：- 普通文件，d 目录，l 链接
```

| 字母 / Letter | 权限 / Permission | 数字 / Number |
|---|---|---|
| `r` | 读 read | 4 |
| `w` | 写 write | 2 |
| `x` | 执行 execute | 1 |

```bash
# 给脚本添加执行权限 / Add execute permission
chmod +x script.sh
chmod 755 script.sh   # rwxr-xr-x

# 查看文件权限
ls -la
```

---

[← 返回目录](./README.md) · [下一章：常用命令 →](./02-commands.md)

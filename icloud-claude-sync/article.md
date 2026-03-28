# 把 Claude Code 配置存进 iCloud，两台电脑秒同步

**我找到了一个最简单的方法，让家里和公司的 Claude Code 配置完全一致。**

---

### 起因：换台电脑什么都得重来

我有两台 Mac，一台在家，一台在公司。每次切换设备，Claude Code 都像一个失忆的助手——插件没了，白名单规则没了，CLAUDE.md 里那些精心写好的指令全部消失。每次都要从头配置，每次都会漏掉什么。

我试过用 GitHub 同步配置文件，搭了一个私有仓库，写了 `.gitignore`，设定了推送规则。这套方案能用，但太笨重：每次改完配置要手动 commit、push，在另一台电脑还要 pull。更麻烦的是，有些文件不适合放进 git，有些状态文件每天都在变，.gitignore 越写越长。

后来我意识到，我需要的不是 git，而是**文件同步**。我已经有 iCloud 了。

---

### 方案：一个软链接解决一切

Claude Code 的用户数据目录默认在 `~/.claude`，所有配置、插件、记忆文件都在这里。

解决思路很简单：
1. 把这个目录**迁移到 `~/Documents/claude-config`**
2. 在原位置创建一个**符号链接**指向新目录
3. iCloud 会自动同步 Documents 文件夹

Claude Code 毫无感知——它读写 `~/.claude` 的行为完全不变，但数据实际存储在 iCloud 同步的目录里。

```
~/.claude  →  ~/Documents/claude-config  →  ☁️ iCloud  →  公司电脑的 ~/Documents/claude-config
```

---

### 需要具备的条件

- 两台 Mac，登录同一个 Apple ID
- iCloud Drive 已开启，且 **Documents 文件夹已勾选同步**（系统设置 → Apple ID → iCloud → iCloud Drive → 同步文档和桌面）
- 两台电脑都安装了 Claude Code

不需要 GitHub，不需要任何第三方工具，不需要手动操作。

---

### 迁移步骤（家里电脑，一次性操作）

**第一步：迁移数据目录**

```bash
mv ~/.claude ~/Documents/claude-config
```

**第二步：创建符号链接**

```bash
ln -s ~/Documents/claude-config ~/.claude
```

**第三步：验证**

```bash
ls -la ~/.claude
# 应该显示：~/.claude -> /Users/你的用户名/Documents/claude-config
```

完成。从这一刻起，所有写入 `~/.claude` 的数据都实际存储在 iCloud 同步目录里。

---

### 公司电脑的操作（一次性）

等 iCloud 把 `claude-config` 目录同步到公司电脑后：

```bash
# 如果公司电脑有旧的 ~/.claude，先备份
mv ~/.claude ~/.claude-backup

# 创建同样的符号链接
ln -s ~/Documents/claude-config ~/.claude
```

完成。两台电脑从此共享同一份配置。

---

### 迁移前后对比

| | 迁移前 | 迁移后 |
|---|---|---|
| 换电脑后的状态 | 插件、设置全部消失，重新配置 | 完全一致，开机即用 |
| 配置同步方式 | 手动 git commit/push/pull | 自动，保存即同步 |
| 需要额外工具 | GitHub 仓库、.gitignore 维护 | 无，iCloud 原生支持 |
| 同步延迟 | 取决于手动操作时机 | 通常几秒到几分钟 |
| Claude Code 感知 | — | 零，行为完全不变 |

---

### 什么文件会同步

`~/Documents/claude-config` 里的内容全部同步，包括：

- `CLAUDE.md` — 全局 AI 指令（最重要，这是你教 Claude 怎么工作的文件）
- `settings.json` — 模型选择、权限模式、启用的插件
- `settings.local.json` — 命令白名单（哪些操作不需要确认）
- `plugins/` — 已安装的插件及其配置
- `projects/` — 各项目的 AI 记忆文件

---

### 注意事项

**iCloud 同步有延迟。** 在一台电脑上改完配置，另一台不会立刻生效，通常需要几秒到几分钟，取决于网络状况。不要在两台电脑上同时修改同一个配置文件，偶发的冲突 iCloud 会创建副本，需要手动合并。

**会话状态不同步是正常的。** `sessions/`、`file-history/`、`telemetry/` 这些目录里存的是运行时状态，体积大、变化频繁，iCloud 会同步它们，但你不需要关心。两台电脑的对话历史是独立的，这是预期行为。

**符号链接要在两台电脑上分别创建。** iCloud 同步的是 `claude-config` 目录本身，不是 `~/.claude` 这个链接。每台新电脑都要手动执行一次 `ln -s` 命令。

---

### 适合哪些人

- 有多台 Mac，希望 AI 工作环境保持一致的开发者
- 深度使用 Claude Code，在 CLAUDE.md 里积累了大量自定义指令的人
- 不想维护 git 仓库来管理工具配置的人
- 已经在用 iCloud 同步文件的 Apple 生态用户

如果你只有一台电脑，这个方案没有意义。如果你用的是 Linux 或 Windows，需要把 iCloud 替换成 Dropbox 或 OneDrive，原理完全一样。

---

### 为什么我喜欢这个方案

我在 Claude Code 里积累了相当多的自定义配置：全局的 CLAUDE.md 写了项目文档规范，settings.local.json 里有十几条命令白名单，插件也装了七八个。这些东西花了我不少时间才调到顺手的状态。

用了这个方案之后，到公司开机，一切都在。CLAUDE.md 的规则在，插件在，白名单在，Claude 认识我。这是一种很具体的、能感受到的效率提升——不是快了多少秒，而是少了那种"又要重新设置一遍"的疲惫感。

符号链接是个老技术，iCloud 也不是什么新东西。但把这两个东西组合起来用在 AI 工具配置上，确实好用。

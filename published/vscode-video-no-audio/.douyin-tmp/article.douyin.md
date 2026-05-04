# VS Code 播放视频没有声音？一篇讲清楚

前两天在 VS Code 里预览可灵生成的视频，发现**有画面没声音**，喇叭图标直接是灰的。同一个文件丢到 Antigravity 里，声音正常。

折腾了一圈，终于搞清楚了。记录一下，省得你再踩坑。

---

### 原因

VS Code 基于 Electron（Chromium 内核），但微软因为 **AAC 音频编解码器的专利授权费用**，在 VS Code 的构建中**故意去掉了 AAC 解码支持**。

绝大多数 MP4 视频的音频轨都是 AAC 编码。VS Code 能解码 H.264 视频，但遇到 AAC 音频直接忽略——所以你看到视频在播，喇叭却是灰的。

这不是 bug，是微软法务部门的决定。GitHub issue [#167685](https://github.com/microsoft/vscode/issues/167685) 从 2022 年挂到现在，56+ 票，没修。

---

### 解决方案

**装一个扩展就行。**

扩展名：**Video Preview (Player)**
ID：`BatchNepal.vscode-video-preview`

它的原理是调用你系统里安装的 `ffmpeg` 来提取音频并播放，绕过了 VS Code 内置的编解码限制。

安装步骤：

1. 确保系统有 ffmpeg（`brew install ffmpeg`）
2. VS Code 扩展商店搜 `BatchNepal.vscode-video-preview`，安装
3. 设置为 mp4 默认打开方式：

```json
"workbench.editorAssociations": {
    "*.mp4": "videoPreview.video"
}
```

装完之后，不管视频是可灵、Seedance、还是随便什么工具生成的，AAC 音频都能正常播放。

---

### 不要尝试的方法

| 方法 | 为什么不行 |
|------|-----------|
| 替换 VS Code 内置的 `libffmpeg.dylib` | Electron 官方版本与 VS Code 自定义构建不兼容，会导致 VS Code 启动闪退 |
| 修改 `~/.vscode/argv.json` 加 `autoplay-policy` | 与音频编解码无关，改了也没用 |
| 修改 VS Code 设置 `mediaPreview.video.autoplay` | 只控制自动播放行为，不影响编解码能力 |
| 用 nwjs-ffmpeg-prebuilt 替换 | Chromium 版本不匹配，同样会闪退 |

---

### 补充：项目级方案

如果你的项目有视频生成流水线（比如调 API 生成视频后下载），可以在下载后自动把音频从 AAC 转成 MP3：

```bash
ffmpeg -i input.mp4 -c:v copy -c:a libmp3lame -q:a 2 output.mp4
```

视频不重新编码，只转音频，几乎秒完成。这样即使没装扩展，VS Code 原生预览也能播放声音。

---

> **老雷（Andy）**，明道云 & Nocoly CMO，SaaS 行业从业十余年。骨子里是个技术迷，乔布斯的信徒，相信好的产品能改变世界。深度关注 AI、商业与科技趋势，目前在深度使用和实践 Claude Code，专注探索 AI 如何重塑产品形态和商业逻辑。不聊概念，只聊真实发生的事。

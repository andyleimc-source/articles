# VS Code Video Preview Has No Audio? Here's Why and How to Fix It

I was previewing a Kling-generated video in VS Code the other day. Video played fine — but no audio. The speaker icon was completely grayed out. Same file played with sound in every other player.

After some digging, I found the root cause. Documenting it here so you don't have to go through the same rabbit hole.

---

### Why It Happens

VS Code is built on Electron (Chromium), but Microsoft's legal team **deliberately removed AAC audio decoding** from VS Code's build due to patent licensing fees.

Most MP4 files use AAC audio. VS Code can decode H.264 video just fine, but when it hits the AAC audio track, it simply ignores it — hence the grayed-out speaker icon.

This isn't a bug. It's a legal decision. GitHub issue [#167685](https://github.com/microsoft/vscode/issues/167685) has been open since 2022 with 56+ upvotes. No fix in sight.

---

### The Fix

**Install one extension.**

Name: **Video Preview (Player)**
ID: `BatchNepal.vscode-video-preview`

It uses your system-installed `ffmpeg` to extract and play audio, bypassing VS Code's built-in codec limitation.

Setup:

1. Make sure you have ffmpeg (`brew install ffmpeg` on macOS)
2. Install `BatchNepal.vscode-video-preview` from the extension marketplace
3. Set it as the default for mp4 files:

```json
"workbench.editorAssociations": {
    "*.mp4": "videoPreview.video"
}
```

Works with any video source — Kling, Seedance, whatever. AAC audio plays fine.

---

### Things That Don't Work

| Approach | Why It Fails |
|----------|-------------|
| Replacing VS Code's bundled `libffmpeg.dylib` | Electron's version is incompatible with VS Code's custom build — causes crash on startup |
| Adding `autoplay-policy` to `~/.vscode/argv.json` | Unrelated to codec support, has no effect on audio decoding |
| Setting `mediaPreview.video.autoplay: false` | Only controls autoplay behavior, doesn't add codec support |
| Using nwjs-ffmpeg-prebuilt | Chromium version mismatch, also causes crashes |

---

### Bonus: Pipeline-Level Fix

If your project generates videos via API (e.g., Kling, Seedance), you can auto-convert audio from AAC to MP3 after download:

```bash
ffmpeg -i input.mp4 -c:v copy -c:a libmp3lame -q:a 2 output.mp4
```

Video stream stays untouched, only audio is re-encoded. Takes under a second. This way VS Code's built-in preview also works — no extension needed.

---

> **Andy** — SaaS veteran (10+ years) obsessed with products and technology. Daily Claude user redefining how work gets done with AI. Sharing practical AI techniques and real productivity gains — no buzzwords, just what actually works.

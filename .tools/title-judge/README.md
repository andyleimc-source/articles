# title-judge — promptfoo 标题生成 + 自评打分

## 用法

```bash
export DEEPSEEK_API_KEY=sk-xxx
cd .tools/title-judge
# 1. 把要测的文章 article.md 内容塞进 build_config.py 的 sources 字典
python3 build_config.py
# 2. 跑评分
promptfoo eval --no-cache
# 3. 看 web 报表
promptfoo view
```

## 文件
- `prompt.txt` — 含爆款 DNA few-shot 的 system prompt。**注意：不要用 `---` 分隔段，会被 promptfoo 当作多 prompt 切开。**
- `promptfooconfig.yaml` — 文章内联，由 `build_config.py` 生成
- `build_config.py` — 从 `published/*/article.md` 抽内容塞进 config

## 已知坑
- promptfoo 把 .txt 里的 `---` 当 prompt 分隔符（→ 9 个结果而不是 3 个）。用 `═══` 之类替代
- vars 里 `file://` 不展开成文件内容（至少 0.121 不行），必须内联

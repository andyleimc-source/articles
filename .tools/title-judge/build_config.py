#!/usr/bin/env python3
"""从 published/*/article.md 抽 1500 字塞进 promptfooconfig.yaml"""
import yaml, pathlib, re

SOURCES = {
    "enterprise-ai-landing-jobs（Jobs 模式 · 企业 AI 落地）": "../../enterprise-ai-landing-jobs/article.md",
    "introduce-superpowers（已知爆款 11686 阅读 · 基线对照）": "../../published/introduce-superpowers/article.md",
    "pensieve-mcp-screen-memory（中等 3339 阅读 · 验证能否超越）": "../../published/pensieve-mcp-screen-memory/article.md",
}

def clean(p):
    raw = pathlib.Path(p).read_text(encoding='utf-8')
    lines = []
    for ln in raw.splitlines():
        if re.match(r'^\s*#\s', ln): continue
        if ln.strip().startswith('<!--'): continue
        if ln.strip().startswith('<img'): continue
        if re.match(r'^!\[', ln.strip()): continue
        if ln.strip() == '---': continue
        lines.append(ln)
    return '\n'.join(lines).strip()[:1500]

tests = [{"description": d, "vars": {"article": clean(f)}} for d, f in SOURCES.items()]
config = {
    "description": "Andy 公众号标题生成 + 自评打分",
    "prompts": ["file://prompt.txt"],
    "providers": [{
        "id": "openai:chat:deepseek-v4-flash",
        "config": {
            "apiBaseUrl": "https://api.deepseek.com/v1",
            "apiKeyEnvar": "DEEPSEEK_API_KEY",
            "temperature": 0.8,
            "max_tokens": 4000,
        }
    }],
    "tests": tests,
}
out = pathlib.Path(__file__).parent / "promptfooconfig.yaml"
with out.open("w", encoding="utf-8") as f:
    yaml.safe_dump(config, f, allow_unicode=True, sort_keys=False, width=10000)
print(f"✅ wrote {out} ({out.stat().st_size} bytes, {len(tests)} tests)")

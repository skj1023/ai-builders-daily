# AI Builders Daily

Kami-style daily briefing page for Lance.

- Data source: public central feeds from [`zarazhangrui/follow-builders`](https://github.com/zarazhangrui/follow-builders)
- No X/Twitter or podcast API key is required in the current mode
- Long-term display: latest homepage + `data/digests.json` recent 60-day archive + per-day archive JSON under `data/archive/`

## Update locally

```bash
python scripts/update_daily.py
```

Then commit and push. GitHub Pages serves the static files from `main`.

## Delivery note

自 2026-09-08 起停止定时推送日报；历史内容保留。页面仍可由数据流程更新，归档与最新内容继续按页面数据逻辑生成。
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

## Automation

A Hermes cron job runs every morning in Asia/Shanghai, updates the digest from follow-builders feeds, commits, pushes, and verifies the Pages URL.

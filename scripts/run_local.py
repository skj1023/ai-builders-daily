#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run update_daily.py logic from local JSON files (bypass urllib SSL issue)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from update_daily import build_digest, load_existing, zh_date, DATA, ARCHIVE
from datetime import datetime, timezone, timedelta

now_cn = datetime.now(timezone.utc) + timedelta(hours=8)
date_key = zh_date(now_cn)

feeds = {}
for name in ["x", "blogs", "podcasts"]:
    host = Path(__file__).resolve().parents[1]
    path = host / f"tmp_{name}.json"
    feeds[name] = json.loads(path.read_text("utf-8"))

digest = build_digest(feeds["x"], feeds["blogs"], feeds["podcasts"], date_key)

archive_path = ARCHIVE / f"{date_key}.json"
archive_path.write_text(json.dumps(digest, ensure_ascii=False, indent=2), "utf-8")
(DATA / "latest.json").write_text(json.dumps(digest, ensure_ascii=False, indent=2), "utf-8")

existing = [d for d in load_existing() if d.get("date") != date_key]
digests = [digest] + existing
digests.sort(key=lambda d: d.get("date", ""), reverse=True)
digests = digests[:60]
(DATA / "digests.json").write_text(json.dumps(digests, ensure_ascii=False, indent=2), "utf-8")

print(json.dumps({
    "status": "ok",
    "date": date_key,
    "builders": digest["stats"]["builders"],
    "tweets": digest["stats"]["tweets"],
    "blogs": digest["stats"]["blogs"],
    "podcasts": digest["stats"]["podcasts"],
    "archive": str(archive_path),
}, ensure_ascii=False, indent=2))

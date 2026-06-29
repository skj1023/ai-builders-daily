#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI Builders Daily updater.

Consumes the public follow-builders central feeds. No X/Twitter, YouTube, or
podcast transcript API key is required. The script writes:
- data/archive/YYYY-MM-DD.json
- data/digests.json
- data/latest.json

The webpage renders from these JSON files, so the long-term logic is:
latest-first homepage + date-grouped archive + source-specific sections.
"""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ARCHIVE = DATA / "archive"

FEEDS = {
    "x": "https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-x.json",
    "blogs": "https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-blogs.json",
    "podcasts": "https://raw.githubusercontent.com/zarazhangrui/follow-builders/main/feed-podcasts.json",
}

TAG_RULES = [
    ("产品", r"product|launch|ship|release|v0|claude|chatgpt|codex|agentforce"),
    ("Agent", r"agent|agents|tool|tools|workflow|automation|autonomous"),
    ("工程", r"code|coding|engineer|infra|system|logs|deploy|compute|gpu|cloud"),
    ("组织", r"team|role|roles|pmf|hiring|founder|company|startup|builder"),
    ("研究", r"paper|eval|benchmark|safety|model|training|scaling|alignment"),
    ("市场", r"pricing|funding|revenue|customers|procurement|market|sales"),
]


def fetch_json(url: str) -> dict[str, Any]:
    req = Request(url, headers={"User-Agent": "AI-Builders-Daily/1.0"})
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def clean_text(text: str, limit: int = 280) -> str:
    text = html.unescape(text or "")
    text = re.sub(r"https://t\.co/\S+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def first_sentence(text: str, limit: int = 220) -> str:
    text = clean_text(text, limit=1000)
    m = re.search(r"(.{40,}?)(?:[。.!?]\s|$)", text)
    out = (m.group(1) if m else text)[:limit].strip()
    return out + ("…" if len(text) > len(out) and not out.endswith("…") else "")


def engagement(tweet: dict[str, Any]) -> int:
    return int(tweet.get("likes") or 0) + 3 * int(tweet.get("retweets") or 0) + int(tweet.get("replies") or 0)


def tags_for(text: str) -> list[str]:
    low = (text or "").lower()
    tags: list[str] = []
    for tag, pattern in TAG_RULES:
        if re.search(pattern, low):
            tags.append(tag)
    return tags[:3] or ["观察"]


def zh_date(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")


def display_date(date_key: str) -> str:
    d = datetime.strptime(date_key, "%Y-%m-%d")
    weekday = "一二三四五六日"[d.weekday()]
    return f"{d.month}月{d.day}日 · 周{weekday}"


def build_digest(feed_x: dict[str, Any], feed_blogs: dict[str, Any], feed_podcasts: dict[str, Any], date_key: str) -> dict[str, Any]:
    builders_raw = feed_x.get("x") or []
    blogs_raw = feed_blogs.get("blogs") or []
    podcasts_raw = feed_podcasts.get("podcasts") or []

    all_tweets: list[tuple[int, dict[str, Any], dict[str, Any]]] = []
    builders: list[dict[str, Any]] = []
    tag_counts: dict[str, int] = {}

    for b in builders_raw:
        tweets = sorted(b.get("tweets") or [], key=engagement, reverse=True)
        if not tweets:
            continue
        items = []
        merged = " ".join(t.get("text", "") for t in tweets)
        for t in tweets[:3]:
            t_tags = tags_for(t.get("text", ""))
            for tag in t_tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            all_tweets.append((engagement(t), b, t))
            items.append({
                "id": t.get("id"),
                "url": t.get("url"),
                "createdAt": t.get("createdAt"),
                "text": clean_text(t.get("text", ""), 320),
                "summary": first_sentence(t.get("text", ""), 180),
                "engagement": engagement(t),
                "tags": t_tags,
            })
        builders.append({
            "name": b.get("name"),
            "handle": b.get("handle"),
            "bio": clean_text(b.get("bio", ""), 120),
            "summary": first_sentence(merged, 220),
            "tags": tags_for(merged),
            "tweets": items,
        })

    all_tweets.sort(key=lambda x: x[0], reverse=True)

    toplines = []
    for score, b, t in all_tweets[:5]:
        topic = first_sentence(t.get("text", ""), 160)
        toplines.append({
            "title": f"{b.get('name')} 的高热度观点",
            "source": f"{b.get('name')} on X",
            "url": t.get("url"),
            "summary": topic,
            "tags": tags_for(t.get("text", "")),
            "score": score,
        })

    blogs = []
    for post in blogs_raw[:6]:
        content = post.get("description") or post.get("content") or ""
        blogs.append({
            "name": post.get("name"),
            "title": html.unescape(post.get("title") or "Untitled"),
            "url": post.get("url"),
            "author": post.get("author") or "",
            "publishedAt": post.get("publishedAt"),
            "summary": first_sentence(content, 260),
            "tags": tags_for((post.get("title") or "") + " " + content),
        })

    podcasts = []
    for ep in podcasts_raw[:4]:
        transcript = ep.get("transcript") or ""
        podcasts.append({
            "name": ep.get("name"),
            "title": html.unescape(ep.get("title") or "Untitled"),
            "url": ep.get("url"),
            "publishedAt": ep.get("publishedAt"),
            "summary": first_sentence(transcript, 260),
            "tags": tags_for((ep.get("title") or "") + " " + transcript[:1200]),
        })

    total_tweets = sum(len(b.get("tweets") or []) for b in builders_raw)
    dominant_tags = sorted(tag_counts.items(), key=lambda kv: kv[1], reverse=True)[:5]
    tag_line = "、".join(t for t, _ in dominant_tags) or "AI builders"
    headline = f"今天的信息流集中在 {tag_line}：{len(builders)} 位 builder、{len(blogs)} 篇官方博客、{len(podcasts)} 期播客进入观察。"

    return {
        "date": date_key,
        "displayDate": display_date(date_key),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceGeneratedAt": {
            "x": feed_x.get("generatedAt"),
            "blogs": feed_blogs.get("generatedAt"),
            "podcasts": feed_podcasts.get("generatedAt"),
        },
        "source": "follow-builders public central feed",
        "sourceRepo": "https://github.com/zarazhangrui/follow-builders",
        "headline": headline,
        "editorNote": "这是一份每日 Builder Briefing：优先收集真正在做产品、模型、基础设施和研究的人，而不是泛化资讯搬运。",
        "stats": {
            "builders": len(builders),
            "tweets": total_tweets,
            "blogs": len(blogs),
            "podcasts": len(podcasts),
            "topTags": [{"name": k, "count": v} for k, v in dominant_tags],
        },
        "toplines": toplines,
        "builders": builders,
        "blogs": blogs,
        "podcasts": podcasts,
        "errors": (feed_x.get("errors") or []) + (feed_blogs.get("errors") or []) + (feed_podcasts.get("errors") or []),
    }


def load_existing() -> list[dict[str, Any]]:
    path = DATA / "digests.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text("utf-8"))
        if isinstance(data, list):
            return data
    except Exception:
        pass
    return []


def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    ARCHIVE.mkdir(parents=True, exist_ok=True)

    now_cn = datetime.now(timezone.utc) + timedelta(hours=8)
    date_key = zh_date(now_cn)
    if len(sys.argv) > 1 and re.match(r"^\d{4}-\d{2}-\d{2}$", sys.argv[1]):
        date_key = sys.argv[1]

    feeds = {name: fetch_json(url) for name, url in FEEDS.items()}
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# subreddit_selector.py
from __future__ import annotations
import json, time, math
from dataclasses import dataclass
from typing import List, Dict, Tuple
from pathlib import Path

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import praw

@dataclass
class SubInfo:
    name: str
    title: str
    public_description: str
    subscribers: int
    active_user_count: int | None
    over18: bool
    lang: str | None
    recent_activity_score: float
    sim: float
    score: float

# FAST activity probe (optional, tiny API usage)
def _recent_activity_score(sr) -> float:
    try:
        hot_n = sum(1 for _ in sr.hot(limit=3))  # small + quick
        return hot_n / 3.0
    except Exception:
        return 0.0

def _describe(sr) -> str:
    title = (getattr(sr, "title", "") or "").strip()
    desc  = (getattr(sr, "public_description", "") or "").strip()
    return f"{sr.display_name_prefixed} — {title}. {desc}"

def _blend(sim: float, subs: int, act: float, lang_ok: bool,
           min_subs: int, prefer_active: bool) -> float:
    subs_term = math.log10(max(subs, 10)) / 6.0  # ~0..1 for 10..1M
    act_term  = min(max(act, 0.0), 1.5) / 1.5
    w_sim, w_sub = 0.64, 0.22
    w_act = 0.12 if prefer_active else 0.04
    w_lang = 0.02
    if subs < min_subs and sim < 0.52:
        return 0.0
    return w_sim*sim + w_sub*subs_term + w_act*act_term + w_lang*(1.0 if lang_ok else 0.6)

def find_subreddits_for_topics(
    reddit: praw.Reddit,
    topics: List[str],
    max_per_topic: int = 5,
    min_subscribers: int = 10_000,
    prefer_active: bool = True,
    language_hint: str | None = "en",
    cache_path: str | None = None,
) -> Dict[str, List[str]]:
    # ---- per-topic cache (safe) ----
    topics = [t.strip() for t in topics if t and t.strip()]
    if not topics:
        return {}

    cached: Dict[str, List[str]] = {}
    if cache_path and Path(cache_path).exists():
        try:
            data = json.loads(Path(cache_path).read_text(encoding="utf-8"))
            if isinstance(data, dict):
                cached = {k: v for k, v in data.items() if isinstance(v, list)}
        except Exception:
            cached = {}

    results: Dict[str, List[str]] = {t: cached.get(t, []) for t in topics if cached.get(t)}
    to_compute = [t for t in topics if not results.get(t)]
    if not to_compute:
        return results

    # ---- model ----
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", cache_folder="./models")
    topic_emb = model.encode(to_compute, normalize_embeddings=True)

    # ---- compute missing topics ----
    for i, topic in enumerate(tqdm(to_compute, desc="Selecting subreddits")):
        # 1) subreddit search (names/descriptions)
        candidates = list(reddit.subreddits.search(topic, limit=20))

        # 2) fallback via posts → collect subreddits from matching posts
        if not candidates:
            posts = list(reddit.subreddit("all").search(topic, limit=50))
            candidates = [p.subreddit for p in posts]

        cand_texts, cand_objs = [], []
        for sr in candidates:
            try:
                cand_texts.append(_describe(sr))
                cand_objs.append(sr)
            except Exception:
                continue

        if not cand_texts:
            results[topic] = []
            continue

        emb = model.encode(cand_texts, normalize_embeddings=True)
        sim = cosine_similarity([topic_emb[i]], emb)[0]

        scored: List[Tuple[float, SubInfo]] = []
        for s, sr in zip(sim, cand_objs):
            try:
                subs = int(getattr(sr, "subscribers", 0) or 0)
                active = getattr(sr, "accounts_active", None)
                lang = getattr(sr, "lang", None)
                # keep polite but fast
                time.sleep(0.0)
                activity = _recent_activity_score(sr)
                lang_ok = True
                if language_hint and isinstance(lang, str):
                    lang_ok = (language_hint.lower() in (lang or "").lower()) or (lang is None)

                final = _blend(float(s), subs, activity, lang_ok, min_subscribers, prefer_active)
                scored.append((
                    final,
                    SubInfo(
                        name=sr.display_name,
                        title=(getattr(sr, "title", "") or ""),
                        public_description=(getattr(sr, "public_description", "") or ""),
                        subscribers=subs,
                        active_user_count=active if isinstance(active, int) else None,
                        over18=bool(getattr(sr, "over18", False)),
                        lang=lang if isinstance(lang, str) else None,
                        recent_activity_score=activity,
                        sim=float(s),
                        score=final,
                    )
                ))
            except Exception:
                continue

        scored.sort(key=lambda x: x[0], reverse=True)

        picked, seen = [], set()
        for sc, si in scored:
            if sc <= 0:
                continue
            key = si.name.lower()
            if any(key.startswith(x) or x.startswith(key) for x in seen):
                continue
            seen.add(key)
            picked.append(si.name)
            if len(picked) >= max_per_topic:
                break

        results[topic] = picked

    # ---- write merged cache & return ----
    if cache_path:
        try:
            Path(cache_path).parent.mkdir(parents=True, exist_ok=True)
            Path(cache_path).write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception:
            pass

    return results
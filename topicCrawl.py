import os, sys, subprocess, itertools
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv
import praw

# our selector module (keep file name: subreddit_selector.py)
from subredditSelector import find_subreddits_for_topics

# ---- setup ----
load_dotenv()  # load .env from repo root if present
SCRIPT_PATH = "redditCrawler.py"  # adjust path if your legacy script lives elsewhere

def get_reddit() -> praw.Reddit:
    return praw.Reddit(
        client_id=os.environ.get("REDDIT_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
        user_agent=os.environ.get("REDDIT_USER_AGENT", "topic-crawl/0.1"),
        username=os.environ.get("REDDIT_USERNAME"),
        password=os.environ.get("REDDIT_PASSWORD"),
    )

def prompt_topics() -> List[str]:
    print("what topic to crawl?")
    print("(enter a topic and press Enter; blank line to finish)")
    topics = []
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            break
        topics.append(line)
    return topics

def resolve_subreddits(topics: List[str], reddit: praw.Reddit) -> List[str]:
    topic2subs = find_subreddits_for_topics(
        reddit=reddit,
        topics=topics,
        max_per_topic=5,
        min_subscribers=10_000,
        prefer_active=True,
        language_hint="en",
        cache_path="out/topic2subs.json",   # set to None to bypass cache
    ) or {}

    merged = list(dict.fromkeys(
        itertools.chain.from_iterable(v for v in topic2subs.values() if isinstance(v, (list, tuple)))
    ))

    print("\n[selector] Topics -> subreddits")
    for t, subs in topic2subs.items():
        print(f" {t} -> {subs}")
    print(f"[selector] total unique subreddits: {len(merged)}\n")
    return merged

def call_existing_script_for_subreddits(sr_list: List[str]) -> int:
    """
    Call legacy crawler ONCE with all subreddits:
      python redditCrawler.py --subreddit sub1 sub2 sub3
    """
    if not Path(SCRIPT_PATH).exists():
        print(f"[warn] {SCRIPT_PATH} not found; cannot spawn legacy crawler.")
        return 1
    argv = [sys.executable, SCRIPT_PATH, "--subreddit", *sr_list]
    print(f"[spawn] {' '.join(argv)}")
    proc = subprocess.run(argv)
    return proc.returncode

def try_import_crawl_func() -> Optional[callable]:
    """
    If someday your legacy module exposes a crawl function, you can wire it here.
    For now, always return None to use the subprocess path.
    """
    return None

def main():
    reddit = get_reddit()
    topics = prompt_topics()
    if not topics:
        print("No topics entered. Exiting.")
        sys.exit(0)

    subreddits = resolve_subreddits(topics, reddit)
    if not subreddits:
        print("No subreddits found for the given topics.")
        sys.exit(0)

    crawl_fn = try_import_crawl_func()
    if crawl_fn:
        print("[info] Using imported crawler function (single process).")
        crawl_fn(subreddits)  # hypothetical signature
    else:
        print("[info] Launching legacy crawler once with --subreddit list.")
        rc = call_existing_script_for_subreddits(subreddits)
        if rc != 0:
            print(f"[warn] crawler exited with code {rc}")

if __name__ == "__main__":
    main()

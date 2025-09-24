import os, praw
from subredditSelector import find_subreddits_for_topics
from dotenv import load_dotenv
load_dotenv()

r = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent="topic-crawl/test",
    username=os.environ.get("REDDIT_USERNAME"),
    password=os.environ.get("REDDIT_PASSWORD"),
)

print(find_subreddits_for_topics(r, ["Hellbomb"], max_per_topic=5, cache_path=None))

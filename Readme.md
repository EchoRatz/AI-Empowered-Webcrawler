# AI-Empowered Webcrawler

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI-Empowered-Webcrawler.git
cd AI-Empowered-Webcrawler
```

2. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up Reddit API credentials

Create a .env file with:
```bash
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
REDDIT_USER_AGENT=your_user_agent
```

🚀 Usage

Run with run.sh:
```bash
./run.sh
```
Or run manually:
```bash
python redditCrawler.py --config config.yaml
```

⚙️ Config File (config.yaml)
```bash
Example:

subreddits:
  - ArtificialIntelligence
  - MachineLearning
  - privacy

query: ""          # "" => new feed, or set to a keyword
since: "2025-01-01T00:00:00Z"
until: "2025-09-11T00:00:00Z"

fetch_comments: true
comment_depth: "all"

out_dir: "out"
format: "csv"          # csv or json
rotate_every_n_posts: 2000
```

📊 Data Pipeline

Crawler (redditCrawler.py) → Fetch raw posts/comments into out/posts.partXXX.csv

Cleaner (cleaner.py) → Normalize fields, drop duplicates, standardize timestamps

Preprocessor (preprocess.py) → Generate text_clean, word counts, and final posts_preprocessed.csv

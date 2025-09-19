# 🕸️ AI-Empowered Webcrawler for Reddit

This project is a **Reddit Sentiment & Trend Analysis pipeline**.  
It crawls Reddit posts via the official **Reddit API (PRAW)**, cleans and preprocesses the data, and prepares it for downstream sentiment and trend analysis.

---

## 📌 Features
- ✅ Crawl multiple subreddits with a single config file
- ✅ Time-window filtering (`since`, `until`)
- ✅ Configurable depth for comments
- ✅ Rotating writer (splits large datasets into multiple `.csv` or `.json` files)
- ✅ Cleaning & preprocessing modules:
  - Remove duplicates
  - Normalize timestamps
  - Clean text (URLs, emojis, punctuation)
  - Handle `NaN` values
- ✅ Ready for **Hive/Spark ingestion** or other analytics tools

---

## 📂 Project Structure
AI-Empowered-Webcrawler/
│── redditCrawler.py # Main crawler (PRAW API)
│── cleaner.py # Cleaning module
│── preprocess.py # Preprocessing module
│── config.yaml # Config file for crawler
│── requirements.txt # Python dependencies
│── run.sh # Bootstrap script (venv + run crawler)
│── out/ # Output folder (CSV/JSON files)

yaml
Copy code

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI-Empowered-Webcrawler.git
cd AI-Empowered-Webcrawler


2. Create virtual environment
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate


3. Install dependencies
bash
Copy code
pip install -r requirements.txt


4. Set up Reddit API credentials
Create a .env file with:

ini
Copy code
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
REDDIT_USER_AGENT=your_user_agent


🚀 Usage
Run with run.sh
bash
Copy code
./run.sh
Run manually
bash
Copy code
python redditCrawler.py --config config.yaml


⚙️ Config File (config.yaml)
Example:

yaml
Copy code
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


📊 Data Pipeline
Crawler (redditCrawler.py) → Fetch raw posts/comments into out/posts.partXXX.csv

Cleaner (cleaner.py) → Normalize fields, drop duplicates, standardize timestamps

Preprocessor (preprocess.py) → Generate text_clean, word counts, and final posts_preprocessed.csv
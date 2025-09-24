<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="left">

# REDDITCRAWLER

<em>Unlock Social Insights, Accelerate Innovation</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/EchoRatz/Redditcrawler?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/EchoRatz/Redditcrawler?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/EchoRatz/Redditcrawler?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/scikit--learn-F7931E.svg?style=flat&logo=scikit-learn&logoColor=white" alt="scikit-learn">
<img src="https://img.shields.io/badge/SentenceTransformers-0A0A0A.svg?style=flat&logo=HuggingFace&logoColor=white" alt="SentenceTransformers">
<img src="https://img.shields.io/badge/praw-FF4500.svg?style=flat&logo=reddit&logoColor=white" alt="praw">

</div>
<br>

---

## 📄 Table of Contents

- [Overview](#-overview)
- [Getting Started](#-getting-started)
  - [Prerequisites](#-prerequisites)
  - [Installation](#-installation)
  - [Usage](#-usage)
- [Features](#-features)
- [Project Structure](#-project-structure)
    - [Project Index](#-project-index)

---

## ✨ Overview

**Redditcrawler** is a Python-based tool for scalable crawling, processing, and analyzing Reddit content.  
It supports classic **subreddit-based crawling** as well as a new **topic-driven subreddit discovery** workflow powered by NLP.

**Why Redditcrawler?**

This project simplifies large-scale social media data harvesting and analysis. The core features include:

- **🧰 Flexible Data Collection:** Supports user-defined queries, timeframes, and depth-controlled comment extraction.  
- **🌐 Topic-Driven Subreddit Discovery:** Uses semantic similarity and activity metrics to find relevant communities.  
- **🧹 Data Cleaning & Preprocessing:** Normalize, filter, deduplicate, and enrich data.  
- **🤖 NLP Integration:** Sentiment analysis and embeddings for deeper insights.  
- **📊 Scalable & Modular:** Ready for large-scale social media research and ML workflows.

---

## 📌 Features

|      | Component       | Details                                                                                     |
| :--- | :-------------- | :------------------------------------------------------------------------------------------ |
| ⚙️  | **Architecture**  | <ul><li>Modular scripts for collection, processing, and analysis</li><li>Classic config-based crawler + topic-driven mode</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Uses configuration files for parameters</li><li>Clear directory layout with separation of concerns</li></ul> |
| 📄 | **Documentation** | <ul><li>README with setup instructions</li><li>Configurable via `config.yaml` and `.env`</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Sentence-BERT embeddings (`sentence-transformers`)</li><li>Reddit API via `praw`</li><li>Pandas + scikit-learn for preprocessing</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate modules for crawling, preprocessing, and sentiment</li><li>Configurable via YAML</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes `test_selector.py` for subreddit discovery</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Efficient batching and cached embeddings</li><li>Optional lightweight activity checks</li></ul> |
| 🛡️ | **Security**      | <ul><li>Secrets loaded from `.env` file</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Managed via `requirement.txt`</li></ul> |

---

## 📁 Project Structure

```sh
└── Redditcrawler/
    ├── README.md
    ├── cleaner.py
    ├── config.yaml
    ├── models/
    │   └── models--sentence-transformers--all-MiniLM-L6-v2
    ├── preprocess.py
    ├── redditCrawler.py
    ├── requirement.txt
    ├── run.sh
    ├── sentiment.py
    ├── subredditSelector.py
    ├── test_selector.py
    └── topicCrawl.py
```
---

📑 Project Index
<details open> <summary><b><code>REDDITCRAWLER/</code></b></summary> <blockquote> <div class='directory-path' style='padding: 8px 0; color: #666;'> <code><b>⦿ __root__</b></code> <table style='width: 100%; border-collapse: collapse;'> <thead> <tr style='background-color: #f8f9fa;'> <th style='width: 30%; text-align: left; padding: 8px;'>File Name</th> <th style='text-align: left; padding: 8px;'>Summary</th> </tr> </thead> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>redditCrawler.py</b></td> <td style='padding: 8px;'>Main crawler — fetches posts/comments from specified subreddits via `config.yaml` or `--subreddit` CLI flag.</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>topicCrawl.py</b></td> <td style='padding: 8px;'>Topic-driven entrypoint — prompts for a topic, discovers subreddits via NLP, asks for confirmation, and launches the crawler.</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>subreddit_selector.py</b></td> <td style='padding: 8px;'>Finds relevant subreddits by analyzing user-defined topics with semantic similarity, popularity, and activity metrics.</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>preprocess.py</b></td> <td style='padding: 8px;'>Prepares crawled CSVs — cleaning, deduplication, timestamp normalization — for analysis or ML pipelines.</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>cleaner.py</b></td> <td style='padding: 8px;'>Provides additional cleaning and filtering for Reddit datasets.</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>sentiment.py</b></td> <td style='padding: 8px;'>Runs sentiment analysis (positive/neutral/negative) on crawled posts.</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>config.yaml</b></td> <td style='padding: 8px;'>Config file for classic crawling: subreddits, queries, timeframes, and output paths.</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>requirement.txt</b></td> <td style='padding: 8px;'>List of Python dependencies for pip installation.</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>run.sh</b></td> <td style='padding: 8px;'>Helper shell script to launch the crawler in config mode (Linux/Mac).</td> </tr> <tr style='border-bottom: 1px solid #eee;'> <td style='padding: 8px;'><b>test_selector.py</b></td> <td style='padding: 8px;'>Small test harness for subreddit discovery using a topic string.</td> </tr> </table> </blockquote> </details>

---

🚀 Getting Started

📋 Prerequisites

Python 3.10+

Reddit API credentials (client ID, secret, username, password, user agent)

pip for dependency installation

⚙️ Installation
1. Clone the repository:
```
git clone https://github.com/EchoRatz/Redditcrawler
```
2. Navigate to the project directory:
```
cd Redditcrawler
```
3. Create and activate a virtual environment:
```
python -m venv .venv
```
```
.\.venv\Scripts\activate   # Windows
# or
source .venv/bin/activate  # Linux/Mac
```
4. Install dependencies:
```
pip install -r requirement.txt
```

Create a .env file:
```
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
REDDIT_USER_AGENT=redditCrawler by u/your_username
```
💻 Usage
Classic mode (from config.yaml):
```
python redditCrawler.py --config config.yaml
```
Topic-driven mode (prompt + NLP):
```
python topicCrawl.py
```
<div align="left"><a href="#top">⬆ Return</a></div> 

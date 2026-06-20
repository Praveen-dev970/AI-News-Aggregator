# AI News Aggregator

An automated, LLM-powered pipeline that aggregates, processes, ranks, and delivers personalized AI news digests to your inbox.

---

## Problem Statement
AI professionals face constant information overload from high-velocity research, blog posts, and video releases. Manually filtering, digesting, and sorting this content based on individual relevance and technical depth is highly inefficient, resulting in either missed breakthroughs or wasted time.

## Tech Stack
*   **Core Logic**: Python 3.12+ (managed with `uv`)
*   **Inference Engine**: Groq API (utilizing `openai/gpt-oss-120b` for fast structured JSON outputs)
*   **Database & ORM**: PostgreSQL & SQLAlchemy
*   **Data Parsing**: Beautiful Soup 4, Docling, Feedparser, and YouTube Transcript API
*   **Infrastructure**: Docker & Docker Compose
*   **Validation**: Pydantic v2

## Input & Output
*   **Input**: 
    *   AI blog RSS feeds (e.g. OpenAI)
    *   Markdown pages & research articles (e.g. Anthropic)
    *   YouTube channel transcripts
    *   Stated user interest profiles, experience level, and preferences
*   **Output**: 
    *   Structured, deduplicated database entries for articles
    *   Relevance-ranked content scores (0.0 - 10.0) based on user alignment
    *   A personalized daily markdown-formatted HTML email summary with top-N ranked digests and custom greetings

## Our Solution
An orchestrated pipeline divided into five key stages:
1.  **Scraping**: Fetches articles and transcripts via RSS feeds, BeautifulSoup/Docling web-scrapers, and YouTube API.
2.  **Digesting**: Employs [DigestAgent](file:///home/krishna/internship%20projects/ai-news-aggregator/app/agent/digest_agent.py) to distill raw content into a concise, technical 2-3 sentence summary.
3.  **Ranking**: Employs [CuratorAgent](file:///home/krishna/internship%20projects/ai-news-aggregator/app/agent/curator_agent.py) to score and order digests based on matching metrics with the user's specific profile interests.
4.  **Email Preparation**: Employs [EmailAgent](file:///home/krishna/internship%20projects/ai-news-aggregator/app/agent/email_agent.py) to draft a friendly, themed overview introducing the top-ranked updates.
5.  **Delivery**: Sends the final compiled HTML report to the configured recipient email.

---

## Setup Guide

### 1. Configure the Environment
Clone the repository and copy the environment template:
```bash
cp app/example.env .env
```
Fill in the `.env` file with your credentials:
*   `GROQ_API_KEY`: Your Groq platform API key.
*   `GROQ_MODEL`: Model name (defaults to `openai/gpt-oss-120b`).
*   `MY_EMAIL`: Sender email address.
*   `APP_PASSWORD`: SMTP app password for sending emails.

### 2. Start PostgreSQL
Launch the database container:
```bash
docker compose -f docker/docker-compose.yml up -d
```

### 3. Install Dependencies
Sync project dependencies using `uv`:
```bash
uv sync
```

### 4. Create Tables
Initialize the database schemas:
```bash
uv run app/database/create_tables.py
```

### 5. Run the Pipeline
Run the daily run command (accepts optional parameters `[hours]` and `[top_n]`):
```bash
# Default: last 24 hours, top 10 articles
uv run main.py 168 10
```

# 🧠 AI News Aggregator

An AI-powered news intelligence platform that automatically collects, summarizes, ranks, stores, and delivers the latest Artificial Intelligence news through a modern Streamlit dashboard and personalized email digests.

---

## 🚀 Overview

#Problem Statement
AI professionals often struggle to keep up with the rapid pace of new research papers, product launches, company announcements, and technical blog posts. Reading multiple sources every day is time-consuming and inefficient.

AI News Aggregator automates this process by collecting news from multiple AI sources, generating concise AI-powered summaries, ranking articles based on user interests, storing everything in PostgreSQL, and delivering a personalized email digest along with an interactive web dashboard.

---

# ✨ Features

## 🤖 AI-Powered Pipeline

* Automated AI news aggregation
* LLM-generated article summaries
* Personalized article ranking
* HTML email digest generation
* PostgreSQL data storage
* Modern Streamlit dashboard

---

## 🌐 Supported Sources

* OpenAI Blog
* Anthropic Blog
* YouTube AI Channels

---

## 📊 Interactive Dashboard

The project includes a professional Streamlit dashboard with:

* 📈 Live dashboard metrics
* 📰 Latest AI news
* 🤖 AI-generated summaries
* 📧 Email digest preview
* 🗄 PostgreSQL data viewer
* 🚀 One-click pipeline execution
* 🌙 Modern dark UI

---

# 🛠 Tech Stack

| Category           | Technology                          |
| ------------------ | ----------------------------------- |
| Language           | Python 3.12+                        |
| UI                 | Streamlit                           |
| LLM                | Groq API (OpenAI Compatible)        |
| Database           | PostgreSQL                          |
| ORM                | SQLAlchemy                          |
| Parsing            | BeautifulSoup4, Feedparser, Docling |
| Video Processing   | YouTube Transcript API              |
| Validation         | Pydantic v2                         |
| Dependency Manager | uv                                  |
| Infrastructure     | Docker & Docker Compose             |

---

# 📂 Project Workflow

```text
OpenAI Blog
        │
Anthropic Blog
        │
YouTube Channels
        │
        ▼
───────────────
 Scrapers
───────────────
        │
        ▼
Digest Agent
(AI Summary)
        │
        ▼
Curator Agent
(Relevance Ranking)
        │
        ▼
PostgreSQL
        │
        ├─────────────┐
        ▼             ▼
Email Agent     Streamlit Dashboard
        │             │
        ▼             ▼
 Personalized     Interactive UI
 Email Digest
```

---

# 📥 Inputs

* OpenAI RSS feeds
* Anthropic articles
* YouTube transcripts
* User profile preferences

---

# 📤 Outputs

* AI-generated summaries
* Ranked AI articles
* PostgreSQL database records
* HTML email digest
* Interactive Streamlit dashboard

---

# ⚙️ Pipeline Architecture

The system consists of five stages.

### 1. Scraping

Collects content from:

* OpenAI
* Anthropic
* YouTube

---

### 2. AI Summarization

The **Digest Agent** generates concise technical summaries for every article using Groq LLM.

---

### 3. AI Ranking

The **Curator Agent** scores every article based on user interests and relevance.

---

### 4. Email Generation

The **Email Agent** prepares a personalized HTML digest.

---

### 5. Dashboard

A Streamlit dashboard displays:

* Live metrics
* Latest AI articles
* AI summaries
* Email preview
* PostgreSQL data

---

# 🗃 Database Tables

The application stores processed information inside PostgreSQL.

| Table              | Description                   |
| ------------------ | ----------------------------- |
| openai_articles    | OpenAI blog articles          |
| anthropic_articles | Anthropic blog articles       |
| youtube_videos     | AI YouTube videos             |
| digests            | AI-generated digest summaries |

---

# 📸 Dashboard Preview

Current dashboard includes:

* Dashboard Metrics
* Latest AI News
* AI Summary Panel
* Email Digest Preview
* PostgreSQL Data Viewer
* Run Pipeline Button

*(Add screenshots here after deployment.)*

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository_url>
cd AI_NEWS_AGGREGATOR
```

---

## 2. Configure Environment

Copy the environment template.

```bash
cp app/.env.example .env
```

Configure the following variables.

```env
MODEL_API_KEY=
MODEL_BASE_URL=
MODEL_NAME=

POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

MY_EMAIL=
APP_PASSWORD=
```

---

## 3. Start PostgreSQL

```bash
docker compose -f docker/docker-compose.yml up -d
```

---

## 4. Install Dependencies

```bash
uv sync
```

---

## 5. Create Database Tables

```bash
uv run app/database/create_tables.py
```

---

## 6. Run Pipeline

```bash
uv run main.py
```

The pipeline will:

* Collect AI news
* Generate summaries
* Rank articles
* Store data in PostgreSQL
* Send email digest

---

## 7. Launch Streamlit Dashboard

```bash
streamlit run app_ui.py
```

Open your browser:

```text
http://localhost:8501
```

---

# 📁 Project Structure

```text
AI_NEWS_AGGREGATOR
│
├── app/
│   ├── agent/
│   ├── database/
│   ├── profiles/
│   ├── scrapers/
│   ├── services/
│   ├── config.py
│   ├── daily_runner.py
│   └── runner.py
│
├── docker/
│
├── .env
├── app_ui.py
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

# 🎯 Current Features

* ✅ OpenAI Scraper
* ✅ Anthropic Scraper
* ✅ YouTube Scraper
* ✅ Groq LLM Integration
* ✅ AI Article Summarization
* ✅ Personalized Ranking
* ✅ PostgreSQL Storage
* ✅ Email Digest
* ✅ Streamlit Dashboard
* ✅ Dashboard Metrics
* ✅ AI Summary Panel
* ✅ Email Preview
* ✅ PostgreSQL Viewer

---

# 🚀 Upcoming Features

* 📊 Interactive Plotly Analytics
* 🔍 Search & Filters
* 📈 Trends Dashboard
* 📰 Professional News Cards
* 📤 Export CSV / PDF
* 🤖 AI Insights
* 💬 RAG-powered AI Chat
* 🌐 Docker Deployment
* ☁ Cloud Deployment
* 🔐 User Authentication

---

# 👨‍💻 Author

**Praveen Yeggada**

AI & Machine Learning Engineer | Python Developer | Generative AI Enthusiast

---

# 📄 License

This project is intended for educational and portfolio purposes.

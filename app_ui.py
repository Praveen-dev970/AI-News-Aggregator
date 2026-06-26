import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import subprocess
import os
from dotenv import load_dotenv
load_dotenv()

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI News Aggregator",
    page_icon="🧠",
    layout="wide"
)

# ==========================================
# DARK THEME CSS
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.news-card {
    background: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    border: 1px solid #333;
}

.metric-card {
    background: #1E1E1E;
    padding: 15px;
    border-radius: 15px;
    text-align:center;
}

.summary-box {
    background:#151515;
    padding:20px;
    border-radius:15px;
    border-left:5px solid #00C896;
}

.digest-box {
    background:#121212;
    padding:20px;
    border-radius:15px;
    border:1px solid #444;
}

h1,h2,h3 {
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

# ==========================================
# LOAD DATA
# ==========================================

def load_articles():

    conn = get_connection()

    query = """
    SELECT *
    FROM openai_articles
    ORDER BY created_at DESC
    LIMIT 20
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def load_digest():

    conn = get_connection()

    query = """
    SELECT *
    FROM digests
    ORDER BY created_at DESC
    LIMIT 1;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🧠 AI News Aggregator")

if st.sidebar.button("🚀 Run Pipeline"):

    with st.spinner("Running AI pipeline..."):

        try:

            subprocess.run(
        ["uv", "run", "python", "main.py"],
        check=True
    )

            st.sidebar.success("Pipeline completed!")

        except Exception as e:
            st.sidebar.error(str(e))

st.sidebar.markdown("---")

st.sidebar.info("""
Features

✅ Latest AI News

✅ AI Summaries

✅ PostgreSQL Data

✅ Email Digest

✅ Analytics Dashboard
""")

# ==========================================
# HEADER
# ==========================================

st.title("🧠 AI News Intelligence Dashboard")

st.caption(
    f"Last Updated: {datetime.now().strftime('%d %b %Y %I:%M %p')}"
)

# ==========================================
# DATA
# ==========================================

try:
    articles_df = load_articles()

    st.write("Rows:", len(articles_df))
    st.dataframe(articles_df.head())

except Exception as e:
    st.error(f"Articles Error: {e}")
    articles_df = pd.DataFrame()

try:

    digest_df = load_digest()

except:

    digest_df = pd.DataFrame()


#========
def load_article_counts():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM openai_articles")
    openai_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM anthropic_articles")
    anthropic_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM youtube_videos")
    youtube_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM digests")
    digest_count = cur.fetchone()[0]

    conn.close()

    return {
        "openai": openai_count,
        "anthropic": anthropic_count,
        "youtube": youtube_count,
        "digests": digest_count,
        "total": openai_count + anthropic_count + youtube_count
    }
# ==========================================
# METRICS
# ==========================================

stats = load_article_counts()

st.subheader("📊 Dashboard Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Articles", stats["total"])

with col2:
    st.metric("OpenAI Articles", stats["openai"])

with col3:
    st.metric("YouTube Videos", stats["youtube"])

with col4:
    st.metric("Digests", stats["digests"])

st.divider()
# ==========================================
# NEWS CARDS
# ==========================================

left, right = st.columns([2, 1])

with left:

    st.subheader("📰 Latest AI News")

    if not articles_df.empty:

        for _, article in articles_df.head(10).iterrows():

            title = article.get("title", "No Title")
            source = article.get("source", "Unknown")
            summary = article.get("summary", "")
            url = article.get("url", "#")

            st.markdown(
                f"""
                <div class="news-card">
                    <h4>{title}</h4>
                    <p><b>Source:</b> {source}</p>
                    <p>{summary[:250]}...</p>
                    <a href="{url}" target="_blank">
                    Read More →
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.warning("No articles found.")

# ==========================================
# AI SUMMARY PANEL
# ==========================================

with right:

    st.subheader("🤖 AI Summary")

    if not digest_df.empty:

        summary = digest_df.iloc[0]["summary"]

        st.markdown(
            f"""
            <div class="summary-box">
            {summary}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.info("No digest generated yet.")

st.divider()

# ==========================================
# EMAIL DIGEST PREVIEW
# ==========================================

st.subheader("📧 Email Digest Preview")

if not digest_df.empty:

    digest_text = digest_df.iloc[0]["summary"]

    st.markdown(
        f"""
        <div class="digest-box">
        {digest_text}
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.warning("No email digest found.")

st.divider()

# ==========================================
# RAW DATABASE VIEW
# ==========================================

st.subheader("🗄 PostgreSQL Data")

if not articles_df.empty:

    st.dataframe(
        articles_df,
        use_container_width=True
    )

else:

    st.info("No records available.")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Powered by Groq • PostgreSQL • Streamlit • AI News Aggregator"
)
import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns

st.set_page_config(page_title="Trader Behavior vs Sentiment", layout="wide")

st.title("📊 Trader Performance vs Market Sentiment")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    trades = pd.read_csv("historical_data.csv")
    sent = pd.read_csv("fear_greed_index.csv")

    # Clean columns
    trades.columns = trades.columns.str.strip().str.lower().str.replace(" ", "_")
    sent.columns = sent.columns.str.strip().str.lower()

    # Convert timestamp
    trades['timestamp'] = pd.to_datetime(trades['timestamp'], unit='ms')
    trades['date'] = trades['timestamp'].dt.date

    sent['date'] = pd.to_datetime(sent['date']).dt.date

    # Standardize sentiment
    sent['classification'] = sent['classification'].replace({
        'Extreme Fear': 'Fear',
        'Extreme Greed': 'Greed'
    })

    # Merge
    df = trades.merge(sent[['date', 'classification']], on='date', how='left')

    # Identify PnL column
    pnl_col = 'closedpnl' if 'closedpnl' in df.columns else 'pnl'

    # Feature Engineering
    df['daily_pnl'] = df.groupby(['account', 'date'])[pnl_col].transform('sum')
    df['win'] = df[pnl_col] > 0
    df['trade_size'] = abs(df['size'])
    df['is_long'] = df['side'].apply(lambda x: 1 if str(x).lower() == 'buy' else 0)
    df['trades_per_day'] = df.groupby(['account', 'date'])['account'].transform('count')

    return df


df = load_data()

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['classification'].dropna().unique(),
    default=df['classification'].dropna().unique()
)

df_filtered = df[df['classification'].isin(sentiment_filter)]

# =========================
# METRICS
# =========================
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Daily PnL", round(df_filtered['daily_pnl'].mean(), 2))
col2.metric("Win Rate", round(df_filtered['win'].mean() * 100, 2))
col3.metric("Avg Trades/Day", round(df_filtered['trades_per_day'].mean(), 2))

# =========================
# PnL DISTRIBUTION
# =========================
st.subheader("📈 PnL Distribution by Sentiment")

fig1, ax1 = plt.subplots()
sns.boxplot(x='classification', y='daily_pnl', data=df_filtered, ax=ax1)
st.pyplot(fig1)

# =========================
# WIN RATE
# =========================
st.subheader("✅ Win Rate by Sentiment")

win_data = df_filtered.groupby('classification')['win'].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(x='classification', y='win', data=win_data, ax=ax2)
st.pyplot(fig2)

# =========================
# BEHAVIOR ANALYSIS
# =========================
st.subheader("⚙️ Trader Behavior")

behavior = df_filtered.groupby('classification').agg({
    'leverage': 'mean',
    'trade_size': 'mean',
    'trades_per_day': 'mean'
}).reset_index()

st.dataframe(behavior)

# =========================
# SEGMENTATION
# =========================
st.subheader("👥 Trader Segmentation")

median_lev = df_filtered['leverage'].median()

df_filtered['leverage_segment'] = df_filtered['leverage'].apply(
    lambda x: 'High' if x > median_lev else 'Low'
)

segment_perf = df_filtered.groupby(
    ['leverage_segment', 'classification']
)['daily_pnl'].mean().reset_index()

fig3, ax3 = plt.subplots()
sns.barplot(
    x='classification',
    y='daily_pnl',
    hue='leverage_segment',
    data=segment_perf,
    ax=ax3
)

st.pyplot(fig3)

# =========================
# LONG / SHORT RATIO
# =========================
st.subheader("🔄 Long vs Short Ratio")

long_short = df_filtered.groupby('classification')['is_long'].mean().reset_index()

fig4, ax4 = plt.subplots()
sns.barplot(x='classification', y='is_long', data=long_short, ax=ax4)
st.pyplot(fig4)

# =========================
# INSIGHTS
# =========================
st.subheader("🧠 Key Insights")

st.markdown("""
- Traders tend to take higher leverage during **Greed** periods  
- Win rates generally drop during **Fear** periods  
- Frequent trading increases during volatile sentiment  
""")

# =========================
# STRATEGY
# =========================
st.subheader("💡 Strategy Recommendations")

st.markdown("""
**1. Reduce leverage during Fear periods**  
→ Helps avoid losses in volatile markets  

**2. Avoid overtrading during Greed**  
→ Focus on high-quality trades instead  
""")

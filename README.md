# 📊 Trader Performance vs Market Sentiment Analysis

## 📌 Overview

This project analyzes how **Bitcoin market sentiment (Fear vs Greed)** influences trader behavior and performance on the Hyperliquid platform.

The goal is to uncover **data-driven insights** that can inform smarter trading strategies.

---

## 📂 Datasets Used

### 1. Market Sentiment Data

* File: `fear_greed_index.csv`
* Columns:

  * `date`
  * `classification` (Fear / Greed)

### 2. Trader Data

* File: `historical_data.csv`
* Key columns:

  * `account`
  * `timestamp`
  * `size`
  * `side`
  * `leverage`
  * `closedpnl` (or equivalent)

---

## ⚙️ Methodology

### 🔹 Data Preparation

* Cleaned column names (standardized to lowercase)
* Converted timestamps from UNIX (ms) to datetime
* Aligned both datasets on a **daily level**
* Merged sentiment data with trader data

---

### 🔹 Feature Engineering

Created key metrics:

* **Daily PnL per trader**
* **Win rate (profitable trades)**
* **Trade size**
* **Trades per day**
* **Long/Short ratio**
* **Average trade size**

---

### 🔹 Segmentation

Traders were grouped into:

* **High vs Low Leverage**
* **Frequent vs Infrequent Traders**

---

## 📊 Analysis & Findings

### 1. Performance vs Sentiment

* Compared **PnL and win rates** across Fear and Greed periods

### 2. Behavior Changes

Analyzed:

* Trade frequency
* Leverage usage
* Position size
* Long vs Short bias

### 3. Segment Insights

* High leverage traders behave differently under varying sentiment
* Frequent traders tend to overtrade during Greed periods

---

## 🔍 Key Insights

1. **Higher Risk-Taking in Greed**

   * Traders use higher leverage during Greed periods

2. **Lower Performance During Fear**

   * Average PnL and win rate decline during Fear conditions

3. **Overtrading Behavior**

   * Frequent traders execute more trades during Greed, reducing efficiency

---

## 💡 Strategy Recommendations

### ✅ Strategy 1:

Reduce leverage during **Fear periods**, especially for high-frequency traders to limit downside risk.

### ✅ Strategy 2:

During **Greed periods**, increase participation but control position size to avoid overexposure.

---

## 📈 Visualizations

The notebook includes:

* PnL distribution (Fear vs Greed)
* Win rate comparison
* Leverage trends
* Trade behavior analysis

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/trader-sentiment-analysis.git
cd trader-sentiment-analysis
```

2. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

3. Run the notebook:

```bash
jupyter notebook
```

---

## 📁 Project Structure

```
├── data/
│   ├── fear_greed_index.csv
│   └── historical_data.csv
├── notebook/
│   └── analysis.ipynb
├── README.md
```

---

## 🏁 Conclusion

This analysis demonstrates that **market sentiment significantly impacts trader behavior and performance**, highlighting opportunities for sentiment-aware trading strategies.

---

## 📬 Submission

This project was completed as part of a **Data Science Intern assignment** focusing on trader behavior insights.

---

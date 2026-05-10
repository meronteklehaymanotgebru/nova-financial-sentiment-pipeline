# 📈 Predicting Price Moves with News Sentiment
> **Nova Financial Solutions** | Data Analytics & Predictive Modeling Pipeline  
> *Separating signal from noise in financial news to forecast stock market movements*

## 📋 Project Overview
This project builds a rigorous, reproducible analytical pipeline that quantifies the relationship between financial news sentiment and daily stock price returns. By combining Natural Language Processing (NLP) for headline sentiment scoring with quantitative technical indicators, we aim to identify actionable patterns that investment teams can use for predictive forecasting and risk management.

### 🎯 Business Objective
Financial markets generate thousands of headlines daily. Most are noise; some drive measurable price action. Nova Financial Solutions requires a data-driven methodology to:
- Extract and score sentiment from financial news headlines
- Compute standard technical indicators (SMA, EMA, RSI, MACD)
- Statistically correlate sentiment shifts with daily stock returns
- Deliver clear, publication-quality visualizations and strategy recommendations

---

## 🏗️ Project Architecture
nova-financial-sentiment-pipeline/
├── .github/workflows/       # CI/CD pipelines (linting, testing)
├── data/raw/                # Raw datasets (news + OHLCV stock data)
├── notebooks/               # Jupyter analysis notebooks
│   ├── 01_eda_financial_news.ipynb
│   └── 02_technical_indicators.ipynb
├── reports/                 # Generated visualizations & interim report
├── scripts/                 # Standalone Python utilities
├── src/                     # Modular source code
│   └── indicators.py        # Pure-pandas technical indicator functions
├── tests/                   # Unit tests for core logic
├── .gitignore
├── requirements.txt
└── README.md 

---

## ⚙️ Quick Start

### 1. Clone & Navigate
```bash
git clone https://github.com/<your-username>/nova-financial-sentiment-pipeline.git
cd nova-financial-sentiment-pipeline

```
---
## Environment Setup
# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Upgrade pip & install dependencies
pip install --upgrade pip
pip install -r requirements.txt

## Run Analysis
# Launch Jupyter Lab
jupyter lab notebooks/

# Or run EDA script directly
python scripts/eda_news_data.py


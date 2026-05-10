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

📊 Data Description
📰 Financial News Dataset

    File: data/raw/raw_analyst_ratings.csv (1,407,328 rows)
    Timeframe: April 2011 – June 2020
    Columns: headline, url, publisher, date (UTC), stock (ticker)
    Preprocessing: Dropped auto-generated index, parsed UTC timestamps, mapped legacy FB → META, extracted headline length & word counts.

📈 Historical Stock Prices

    Files: AAPL.csv, GOOG.csv, AMZN.csv, NVDA.csv, META.csv
    Source: Yahoo Finance (yfinance)
    Columns: Date, Close, High, Low, Open, Volume (split-adjusted)
    Frequency: Daily trading days (weekends/holidays excluded)

🔍 Analysis Pipeline
Phase
	
Task
	
Tools & Methods
	
Output
1. EDA
	
Explore news structure, publisher activity, publication trends, TF-IDF keyword extraction
	
pandas, seaborn, scikit-learn
	
4 publication-quality plots, cleaned CSV
2. Technical Indicators
	
Compute SMA, EMA, RSI, MACD; visualize against price action
	
Pure pandas rolling/ewm operations
	
Indicator overlays, RSI/MACD panels
3. Sentiment & Correlation
	
Score headlines (TextBlob/VADER), align to trading days, compute Pearson correlation
	
nltk, textblob, scipy.stats
	
Scatter plots, category-based return bars, correlation coefficient
🛠️ Tools & Technologies

    Core: Python 3.12, pandas, numpy, scipy
    NLP: nltk (VADER), textblob, scikit-learn (TF-IDF)
    Visualization: matplotlib, seaborn
    Data I/O: yfinance (fallback), native pandas CSV readers
    Quality & CI: pytest, flake8, black, GitHub Actions
    Environment: venv, requirements.txt, Makefile (optional)

✅ Deliverables & Status
Requirement
	
Status
	
Location
GitHub repo + task-1 branch
	
✅ Complete
	
git branch
CI/CD workflow (.github/workflows/unittests.yml)
	
✅ Active
	
Auto-runs on push/PR
Task 1: EDA notebook + ≥3 visualizations
	
✅ Complete
	
notebooks/01_eda_financial_news.ipynb
Task 2: Technical indicators notebook
	
✅ In Progress
	
notebooks/02_technical_indicators.ipynb
Interim Report (≤3 pages)
	
✅ Drafted
	
reports/interim_report.md
≥3 descriptive commits/day
	
✅ Maintained
	
git log
🧪 Testing & CI/CD
The repository uses GitHub Actions to enforce code quality and reproducibility:

    Linting: flake8 checks for syntax/style violations
    Formatting: black ensures PEP8 compliance
    Testing: pytest runs unit tests on src/indicators.py
    Coverage: pytest-cov tracks line coverage (artifact saved)


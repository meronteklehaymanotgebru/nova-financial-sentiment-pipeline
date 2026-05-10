# Interim Report: Predicting Price Moves with News Sentiment
**Author:** Meron Gebru | **Team:** Nova Financial Solutions | **Date:** May 10, 2026

## Executive Summary
We successfully established a reproducible data pipeline, completed exploratory analysis on 1.4M financial headlines, and computed technical indicators for five major equities (AAPL, GOOG, AMZN, NVDA, META). Early findings reveal structured publishing patterns, clear technical indicator signals, and a baseline for sentiment-return correlation analysis.

## Data Loading & Cleaning
- **News Dataset**: Loaded `raw_analyst_ratings.csv` (1,407,328 rows, 5 columns). Removed auto-generated index, parsed UTC timestamps to dates, and mapped legacy ticker `FB` → `META`.
- **Stock Data**: Imported OHLCV CSVs from Yahoo Finance format. Verified headers, handled split-adjusted prices, and computed daily percentage returns.
- **Data Quality**: ~2.1% of news dates were malformed; dropped safely. Stock files contained zero missing values after sorting.

## Key EDA Findings
1. **Headline Patterns**: Average length 73.1 characters (11.4 words). Distribution is right-skewed, indicating concise financial reporting.
2. **Publisher Activity**: 1,034 unique sources. Top publisher: Paul Quintaro. Volume spikes align with market open (8–10 AM UTC) and earnings seasons.
3. **Stock Coverage**: NVDA (3,146), GOOG (1,199), AAPL (441), AMZN (278), META/FB (mapped). Coverage disparity reflects market focus vs. dataset sampling.
4. **TF-IDF Themes**: Top keywords include `"price target"`, `"earnings beat"`, `"surges"`, `"drops"`, indicating event-driven headline framing.

*(Attach: `headline_length_dist.png`, `news_volume_timeline.png`, `top_publishers.png`)*

## Initial Technical Analysis
- Implemented pure-pandas SMA, EMA, RSI, and MACD to avoid external C-dependency conflicts.
- **SMA/EMA**: 20/50-day crosses clearly identify trend shifts (e.g., AAPL 2023 uptrend).
- **RSI**: Oscillates between 30–70, with overbought/oversold signals preceding short-term reversals.
- **MACD**: Histogram divergence aligns with momentum shifts before price confirmation.
*(Attach: `AAPL_price_sma.png`, `AAPL_rsi_macd.png`)*

## Challenges & Next Steps
- **Ticker Mapping**: Resolved `FB` → `META` mismatch. Future work: automate ticker normalization using a mapping table.
- **Date Alignment**: Handled weekend/holiday gaps by merging news dates only with active trading days. Next: test lagged sentiment (T-1) for predictive modeling.
- **Sentiment Scale**: VADER outperformed TextBlob on financial jargon due to domain-specific lexicon. Will finalize correlation analysis and draft investment strategy recommendations for final submission.
#!/usr/bin/env python3
"""EDA for Financial News Dataset - Task 1"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# === CONFIG ===
FILE_PATH = Path("data/raw/raw_analyst_ratings.csv")  # The news file
OUTPUT_DIR = Path("reports")
OUTPUT_DIR.mkdir(exist_ok=True)

print(f"📁 Loading data from: {FILE_PATH}")

# === 1. LOAD & CLEAN ===
df = pd.read_csv(FILE_PATH, index_col=0)  # Drop Unnamed: 0
print(f"✅ Loaded {len(df):,} rows, {len(df.columns)} columns")
print(f"📋 Columns: {df.columns.tolist()}")

# Parse dates
df['date_parsed'] = pd.to_datetime(df['date'], errors='coerce', utc=True)
print(f"📅 Date range: {df['date_parsed'].min()} to {df['date_parsed'].max()}")

# Check stock symbols
print(f"\n🏷️  Unique stocks: {df['stock'].nunique()}")
print(f"📊 Top 10 tickers:\n{df['stock'].value_counts().head(10)}")

# === 2. DESCRIPTIVE STATS - HEADLINES ===
df['headline_length_chars'] = df['headline'].str.len()
df['headline_length_words'] = df['headline'].str.split().str.len()

print(f"\n📏 Headline Stats:")
print(f"   Avg length (chars): {df['headline_length_chars'].mean():.1f}")
print(f"   Avg length (words): {df['headline_length_words'].mean():.1f}")
print(f"   Min/Max: {df['headline_length_chars'].min()} - {df['headline_length_chars'].max()} chars")

# === 3. VISUALIZATIONS ===
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# 3a. Headline length distribution
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(df['headline_length_chars'], bins=40, edgecolor='black', color='skyblue')
axes[0].axvline(df['headline_length_chars'].mean(), color='red', linestyle='--', label='Mean')
axes[0].set_title('Headline Length (Characters)')
axes[0].set_xlabel('Characters')
axes[0].set_ylabel('Frequency')
axes[0].legend()

axes[1].hist(df['headline_length_words'], bins=30, edgecolor='black', color='lightgreen')
axes[1].axvline(df['headline_length_words'].mean(), color='red', linestyle='--', label='Mean')
axes[1].set_title('Headline Length (Words)')
axes[1].set_xlabel('Words')
axes[1].set_ylabel('Frequency')
axes[1].legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'headline_length_dist.png', dpi=300, bbox_inches='tight')
print(f"✅ Saved: reports/headline_length_dist.png")
plt.show()

# 3b. Publisher analysis
plt.figure(figsize=(10, 8))
top_publishers = df['publisher'].value_counts().head(15)
top_publishers.plot(kind='barh', color='steelblue', edgecolor='black')
plt.title('Top 15 Publishers by Article Count')
plt.xlabel('Number of Articles')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'top_publishers.png', dpi=300, bbox_inches='tight')
print(f"✅ Saved: reports/top_publishers.png")
plt.show()

# 3c. News volume over time (daily)
df_clean = df.dropna(subset=['date_parsed'])
daily_counts = df_clean.groupby(df_clean['date_parsed'].dt.date).size()

plt.figure(figsize=(14, 5))
daily_counts.plot(linewidth=0.5, color='darkblue')
plt.title('Daily News Publication Volume')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'news_volume_timeline.png', dpi=300, bbox_inches='tight')
print(f"✅ Saved: reports/news_volume_timeline.png")
plt.show()

# 3d. Articles per stock
plt.figure(figsize=(10, 6))
stock_counts = df['stock'].value_counts().head(20)
stock_counts.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Top 20 Stocks by News Coverage')
plt.xlabel('Stock Ticker')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'stock_coverage.png', dpi=300, bbox_inches='tight')
print(f"✅ Saved: reports/stock_coverage.png")
plt.show()

# === 4. SAMPLE HEADLINES PER STOCK ===
print(f"\n🔍 Sample headlines for your stock files (AAPL, GOOG, AMZN, NVDA, META):")
for ticker in ['AAPL', 'GOOG', 'AMZN', 'NVDA', 'META']:
    mask = df['stock'].str.upper() == ticker
    if mask.any():
        samples = df.loc[mask, 'headline'].head(3).tolist()
        print(f"\n{ticker} ({mask.sum()} articles):")
        for i, h in enumerate(samples, 1):
            print(f"   {i}. {h[:100]}...")
    else:
        print(f"\n{ticker}: ❌ No articles found (check ticker format)")

# === 5. SAVE CLEANED DATA ===
df_clean = df.drop(columns=['date']).rename(columns={'date_parsed': 'date'})
df_clean.to_csv(OUTPUT_DIR / 'news_data_cleaned.csv', index=False)
print(f"\n✅ Saved cleaned data: reports/news_data_cleaned.csv")

# === 6. QUICK SUMMARY FOR REPORT ===
summary = {
    'total_articles': len(df),
    'unique_stocks': df['stock'].nunique(),
    'unique_publishers': df['publisher'].nunique(),
    'date_range': f"{df['date_parsed'].min().date()} to {df['date_parsed'].max().date()}",
    'avg_headline_words': round(df['headline_length_words'].mean(), 1),
    'top_stock': df['stock'].value_counts().idxmax(),
    'top_publisher': df['publisher'].value_counts().idxmax()
}

print(f"\n📋 EDA Summary for Interim Report:")
for k, v in summary.items():
    print(f"   • {k}: {v}")
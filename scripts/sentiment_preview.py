import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load a small sample for quick preview
df = pd.read_csv("reports/news_cleaned.csv").head(5000)
df["sentiment"] = df["headline"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

plt.figure(figsize=(8,4))
df["sentiment"].hist(bins=50, color="teal", edgecolor="black")
plt.axvline(0, color="red", linestyle="--")
plt.title("Preview: Sentiment Distribution (5k Headlines)")
plt.savefig("reports/sentiment_preview.png", dpi=200)
print("✅ Saved sentiment preview. Ready for Task 3 correlation.")
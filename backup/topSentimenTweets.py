import pandas as pd


df = pd.read_csv("tweets_with_sentiment.csv")


top_positive = df.sort_values(by="Polarity", ascending=False).head(10)
top_negative = df.sort_values(by="Polarity").head(10)


top_positive.to_csv("top_positive_tweets.csv", index=False)
top_negative.to_csv("top_negative_tweets.csv", index=False)

print("Top positive and negative tweets saved to CSV files.")

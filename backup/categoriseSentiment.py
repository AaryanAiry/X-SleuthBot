import pandas as pd


df = pd.read_csv("tweets_with_sentiment.csv")


def classify_sentiment(polarity):
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"


df['sentiment_label'] = df['polarity'].apply(classify_sentiment)


df.to_csv("tweets_with_sentiment_labeled.csv", index=False)

import pandas as pd
from textblob import TextBlob


df = pd.read_csv("tweets.csv")


def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return pd.Series([polarity, subjectivity])


df[['Polarity', 'Subjectivity']] = df['text'].apply(get_sentiment)


def classify_sentiment(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['Polarity'].apply(classify_sentiment)

# Save results
df.to_csv("tweets_with_sentiment.csv", index=False)
print("Sentiment analysis complete. Results saved to tweets_with_sentiment.csv")
import pandas as pd

df = pd.read_csv("tweets_with_sentiment.csv")
print(df.columns)

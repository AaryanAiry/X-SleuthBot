import pandas as pd


df = pd.read_csv("tweets_with_sentiment.csv")


print(df['Sentiment'].value_counts())


import matplotlib.pyplot as plt


df['Sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.tight_layout()
plt.show()

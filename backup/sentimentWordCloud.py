import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import string


df = pd.read_csv('tweets_with_sentiment.csv')


def clean_text(text):
    text = re.sub(r'http\S+|www.\S+', '', text)          # remove URLs
    text = re.sub(r'@\w+|#\w+', '', text)                # remove mentions and hashtags
    text = re.sub(r'\d+', '', text)                      # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    text = text.lower()                                  # lowercase
    return text


df['clean_text'] = df['text'].astype(str).apply(clean_text)


all_text = ' '.join(df['clean_text'])


wordcloud = WordCloud(width=1000, height=500, background_color='white',
                      max_words=200, colormap='viridis').generate(all_text)


plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("WordCloud of All Tweets")
plt.tight_layout()
plt.savefig('all_tweets_wordcloud.png')
plt.show()

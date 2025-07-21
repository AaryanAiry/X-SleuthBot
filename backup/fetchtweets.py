import tweepy
import csv
import os

from dotenv import load_dotenv



load_dotenv()


BEARER_TOKEN = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = "superman movie is:verified has:images has:links -is:retweet lang:en"
response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["id", "author_id", "created_at", "text"],
    expansions=["author_id"],
    user_fields=["username"]
)


users = {user.id: user.username for user in response.includes["users"]}


existing_ids = set()
if os.path.exists("tweets.csv"):
    with open("tweets.csv", mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_ids.add(row['id'])


with open("tweets.csv", mode='a', newline='', encoding='utf-8') as file:
    fieldnames = ['id', 'created_at', 'author_id', 'username', 'text', 'url']
    writer = csv.DictWriter(file, fieldnames=fieldnames)


    if os.stat("tweets.csv").st_size == 0:
        writer.writeheader()

    for tweet in response.data:
        if str(tweet.id) not in existing_ids:
            username = users.get(tweet.author_id, "unknown")
            tweet_url = f"https://twitter.com/{username}/status/{tweet.id}"
            writer.writerow({
                'id': tweet.id,
                'created_at': tweet.created_at,
                'author_id': tweet.author_id,
                'username': username,
                'text': tweet.text,
                'url': tweet_url
            })

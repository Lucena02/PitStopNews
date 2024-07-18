from app import app
import tweepy
from app.keys import *
import csv
import datetime
import os
# Your credentials


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)



@app.route('/')
def home():
    return "Hello, Flask!"



@app.route('/cnn/')
def index():
    # Specify the Twitter handle of the user
    username = 'CNN'

    # Number of tweets to fetch
    tweet_count = 10

    # Fetch tweets
    tweets = api.user_timeline(screen_name=username, count=tweet_count, tweet_mode='extended')

    # Store tweets in a list
    tweet_list = []

    for tweet in tweets:
        tweet_list.append({
            'user': tweet.user.screen_name,
            'text': tweet.full_text,
            'created_at': tweet.created_at
        })

    return render_template('index.html', tweets=tweet_list)


@app.route('/teste/')
def indexx():
    return get_tweets("CNN")



def get_tweets(username: str):
    """
    Pulls 3,200 (maximum allowed) most recent tweets for specified username and saves to tweets_<username>.csv
    """

    client = tweepy.Client(TWITTER_BEARER_TOKEN)
    user_id = client.get_user(username=username).data.id
    responses = tweepy.Paginator(client.get_users_tweets, user_id, max_results=100, limit=100)
    tweets_list = [["link", "username" "tweet"]]
    currentime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    counter = 0
    for response in responses:
        counter += 1
        print(f"==> processing {counter * 100} to {(counter + 1) * 100} of {username}'s tweets")
        try:
            for tweet in response.data:  # see any individual tweet by id at: twitter.com/anyuser/status/TWEET_ID_HERE
                tweets_list.append([f"https://twitter.com/anyuser/status/{tweet.id}", username, tweet.text])
        except Exception as e:
            print(e)

    with open(f"tweets_{username}_{currentime}.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tweets_list)

    print("Done!")


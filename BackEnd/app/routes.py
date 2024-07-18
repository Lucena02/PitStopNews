from app import app
import tweepy
from keys import *

# Your credentials


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

@app.route('/')
def home():
    return "Hello, Flask!"

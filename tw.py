from config import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import pandas as pd
from pprint import pprint
from datetime import datetime
import pytz
import numpy as np
import time
import tweepy

df = pd.read_csv('twitter-data/trump.csv') # old tweets
cols = list(df.columns)

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) # auth

api = tweepy.API(auth)

def get_tweets(df, cols, api):
    old = df.iloc[0].to_list()[1] # first old tweet
    timeline = api.user_timeline('realDonaldTrump', count=1000, since_id=old) # get new tweets

    new_tweets = []

    for t in list(timeline)[::-1]:
        t = t._json
        date, tweet_id = t['created_at'], t['id'] # date, id
        dt = datetime.strptime(date,'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
        date = dt.strftime('%Y-%m-%d %H:%M:%S')
        new_tweets.append((date, tweet_id))

    if new_tweets: # write new tweets
        # for tweet in new_tweets:
        #     print(tweet)
        new_df = pd.DataFrame(np.array(new_tweets), columns=cols).iloc[::-1] # new tweets df
        df = new_df.append(df, ignore_index=True) # add new tweets above old ones

        df.to_csv('twitter-data/trump.csv', index=False)

if __name__ == '__main__':
    while True:
        get_tweets(df, cols, api)
        time.sleep(60)

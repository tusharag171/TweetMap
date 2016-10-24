#! /usr/bin/python

# This file pushes data into Elasticsearch Instance

from twython import Twython
from datetime import datetime
import config as Config
import time
from elasticsearch import Elasticsearch
from elasticsearch import *

es = Elasticsearch([Config.ES])
#es = Elasticsearch(["127.0.0.1:9200"])

TWITTER_APP_KEY = Config.TWITTER_APP_KEY
TWITTER_APP_KEY_SECRET = Config.TWITTER_APP_KEY_SECRET
TWITTER_ACCESS_TOKEN = Config.TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = Config.TWITTER_ACCESS_TOKEN_SECRET

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

def get_tweets(keyword):
    search = t.search(q=keyword,count=100)
    tweets = []
    tweets = search['statuses']
    for tweet in tweets:
	#print "TWEET"
        if tweet['user']['location'] is not None:
            doc = {
                'text': tweet['text'],
                'location': tweet['user']['location'],
                'timestamp': datetime.now()
            }
            res = es.index(index="test-index",doc_type='tweet', body=doc)
            #print(res['created'])



def twittmap():
    try:
        while True:
            get_tweets('java')
            get_tweets('love')
            get_tweets('worlds')
            get_tweets('ruby')
            get_tweets('tata')
            get_tweets('columbia')
            get_tweets('food')
            get_tweets('diwali')
            get_tweets('movie')
            get_tweets('music')
    except:
        return

print "Fetching Tweets from Twitter...(Ctrl+C to stop)"
twittmap()

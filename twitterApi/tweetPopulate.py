#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 08:40:59 2018

@author: hritik
"""

from pymongo import MongoClient,errors
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler,API,Stream
import datetime
import pprint
client = MongoClient('localhost',27017)
db = client.TwitterStream
db.tweets.create_index("id",unique=True, dropDups=True)
collection = db.tweets

# Add the keywords you want to track. They can be cashtags, hashtags, or words.

# Optional - Only grab tweets of specific language
language = ['en']
#key_Words = ['#MeToo','#Durgapuja','#India','#Bollywood','#NetFlix']

consumer_key = "7iELV7aYkxYoUsD5mG8p8GPqR"
consumer_secret = "HxaGueioOE6FmjJvZjzTru5XgqnN55Oo6Ok7xX7Hr17u75UUWG"
access_token = "2940370883-qD6fYwHRKJhgtKkeXH5E5meXSc2w36khw1pMdRJ"
access_token_secret = "GqrRT9IKayLb8mdQQdjm5Mxn9kJbpwt3kuTeGJtKYdh3h"


class MyStreamListener(StreamListener):

    def on_data(self, data):
        try:
            t = json.loads(data)
            tweet_id = collection.count()+1
            if 'id' in t.keys():
                user_id = t['id']
            else:
                user_id = 0
               # The Tweet ID from Twitter in string format
            User_name = t['user']['name']  # The username of the Tweet author
            Screen_name = t['user']['screen_name'] # The Screen name of the Tweet Author

            tweet_date = t['created_at']  # The timestamp of when the Tweet was created
            if 'retweet_status' in t.keys():
                retweet_count = t['retweet_status']['retweet_count']
            else:
                retweet_count = 0
            if(len(t['entities']['user_mentions']) != 0):
                User_mentions = t['entities']['user_mentions'][0]['name']  # The number of followers the Tweet author has
            else:
                User_mentions = "Nil"

            tweet_text = t['text']  # The entire body of the Tweet
            Url_text = t['source']
            if 'followers' in t['user'].keys():
                followers = t['user']['followers']
            else:
                followers = 0

            if 'favorites' in t['user'].keys():
                favorites = t['user']['favorites']
            else:
                favorites = 0

            if 'friends' in t['user'].keys():
                friends = t['user']['friends']
            else:
                friends = 0
            tweet_date = datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S +0000 %Y')

            tweet = { 'id':tweet_id,'user_id':user_id,'User_name':User_name, 'Screen_name':Screen_name, 'followers':followers,'favorites':favorites,'friends':friends,'tweet_date':tweet_date,'retweet_count':retweet_count,'User_mentions':User_mentions,'tweet_text':tweet_text,'Url_text':Url_text}
            collection.save(tweet)
            pprint.pprint(tweet)
            if collection.count() > 100:
                return False
        except KeyboardInterrupt:
            sys.exit()
        return True

# Prints the reason for an error to your console
    def on_error(self, status):
        print (status.text)

class StreamTweets():
    def stream(self,key_Words):
        l = MyStreamListener()
        auth = OAuthHandler(consumer_key, consumer_secret,'https://127.0.0.1/')
        auth.set_access_token(access_token, access_token_secret)
        api = API(auth)
        stream = Stream(auth=api.auth,listener = l,async=True)
        stream.filter(track=key_Words, languages=language)

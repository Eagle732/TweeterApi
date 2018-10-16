#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 08:40:59 2018

@author: hritik
"""

from pymongo import MongoClient,errors
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
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

consumer_key = "LsVriZLSKbmjuvtOL1hsXjGmA"
consumer_secret = "5X3pWMKVfbYize4Fy9S61cquiEiUe2nB9g6qAX6eQnBPuhUHzk"
access_token = "2940370883-ts4J9aXF5fQDJ5dYKcUbIDRrD20nmmdYuzzuGdt"
access_token_secret = "eKJx3qsLNR9Y1kGPNeqeOgyB4ifYiMn1oiKHJbEY6G9BG"


class StdOutListener(StreamListener):

    def on_data(self, data):

        # Load the Tweet into the variable "t"
        t = json.loads(data)
        tweet_id = collection.count()+1  # The Tweet ID from Twitter in string format
        User_name = t['user']['name']  # The username of the Tweet author
        Screen_name = t['user']['screen_name']

        tweet_date = t['created_at']  # The timestamp of when the Tweet was created
        retweet_count = t['retweet_count']
        if(len(t['entities']['user_mentions'])!= 0):
            User_mentions = t['entities']['user_mentions'][0]['name']  # The number of followers the Tweet author has
        else:
            User_mentions = "Nil"
        tweet_text = t['text']  # The entire body of the Tweet
        Url_text = t['user']['url']
        tweet_length = len(tweet_text)
        tweet_date = datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S +0000 %Y')

        tweet = { 'id':tweet_id,'User_name':User_name, 'Screen_name':Screen_name, 'tweet_length':tweet_length,'tweet_date':tweet_date,'retweet_count':retweet_count,'User_mentions':User_mentions,'tweet_text':tweet_text,'Url_text':Url_text}
        collection.save(tweet)
        pprint.pprint(tweet)
        if tweet_id > 50:
            return False
        return True

# Prints the reason for an error to your console
    def on_error(self, status):
        print (status)

class StreamTweets():
    def stream(self,key_Words):
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l,async=True)
        stream.filter(track=key_Words, languages=language)

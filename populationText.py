import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','intern.settings')

import django
django.setup()


# FAKE POP SCRIPT

from random import randint

from twitterApi.models import Tweets ,KeyWords
from faker import Faker

fakegen = Faker()
tweets = ['User name','Screen_name','len','tweet_date','retweet_count','User_mentions','tweet_text','Url_text']
KeyWords = ['words']

def Tweet_gen(N=5):
    for entry in range(N):
        User_name = fakegen.name()
        Screen_name = fakegen.name()
        len = randint(1,100)
        tweet_date = fakegen.date()
        retweet_count = randint(1,19)
        User_mentions = fakegen.name()
        tweet_text = fakegen.text()
        Url_text = fakegen.url()

        tweets = Tweets.objects.get_or_create(User_name=User_name,Screen_name=Screen_name,tweet_length=len,tweet_date=tweet_date,
                                        retweet_count=retweet_count,User_mentions=User_mentions,
                                        tweet_text=tweet_text,Url_text=Url_text)[0]

if __name__ == '__main__':
    Tweet_gen(15)
    print("Population Complete !")

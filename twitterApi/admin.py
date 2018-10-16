from django.contrib import admin
from .models import KeyWords, Tweets

from . import models
# Register your models here.
class TweetsAdmin(admin.ModelAdmin):
    fields = ['User_name','Screen_name','tweet_length','tweet_date','retweet_count','User_mentions','tweet_text','Url_text']
    list_display = ['User_name','Screen_name','tweet_length','tweet_date','retweet_count','User_mentions','tweet_text','Url_text']
    search_fields = ['Screen_name','tweet_length','tweet_date','retweet_count','User_mentions']
    list_editable = ['Screen_name','tweet_length','tweet_date','retweet_count','User_mentions','tweet_text','Url_text']
    list_filter = ['Screen_name','tweet_length','tweet_date','retweet_count','User_mentions',]

admin.site.register(KeyWords)
admin.site.register(Tweets,TweetsAdmin)
# admin.site.register(Song)

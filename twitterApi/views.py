from django.shortcuts import render,get_object_or_404
import re
import csv
from . import formKeyWords,filterForm
import pymongo
from . import tweetPopulate
from .models import Tweets,Filtered_Tweets
from .tables import TweetTables
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .filteringAlgo import filtering

def index(request):
	form = formKeyWords.TweetKeyWords()
	# Tweets.objects.all().delete()
	# conn = pymongo.MongoClient('localhost',27017).TwitterStream.tweets.drop()
	return render(request,'twitterApi/index.html',{'form':form})

def dowload_tweets(request):
	print(request)
	return HttpResponse("")



def fil_tweets(request):
	filter_tweets = filterForm.tweetFilter()
	TweetObject = Tweets.objects.all()
	if request.method == "POST":
		filt = filterForm.tweetFilter(request.POST)
		if filt.is_valid():
			TweetObject = filtering(filt)
			val = TweetObject.all().values()
			i = 1
			for objects in val:
				Filtered_Tweets(Id = i,user_id=obj['user_id'],favorites=obj['favorites'],friends=obj['friends'],followers=obj['followers'],User_name=obj['User_name'],Screen_name=obj['Screen_name'],
					tweet_date=obj['tweet_date'],retweet_count=obj['retweet_count'],User_mentions=obj['User_mentions'],tweet_text=obj['tweet_text'],Url_text=obj['Url_text']).save()
			i+=1
			to_import = list(Filtered_Tweets.objects.all().values())
			if len(to_import)>0:
				keys = 	to_import[0].keys()
				with open('media/tweets.csv','w') as output_file:
					dict_w = csv.DictWriter(output_file,keys)
					dict_w.writeheader()
					dict_w.writerows(to_import)

	TweetObject = Filtered_Tweets.objects.all()
	tweet_per_page = 5
	current_page = int(request.GET.get('page',1))
	limit = tweet_per_page*current_page
	offset = limit - tweet_per_page
	tweet_table = TweetObject[offset:limit]
	total_tweets = TweetObject.count()
	total_pages = total_tweets // tweet_per_page

	if total_pages % tweet_per_page != 0 :
		total_pages += 1
	pagination = make_pagination_html(current_page, total_pages)
	return render(request,'twitterApi/filtered_tweets.html',{'tweet_table':tweet_table,'pagination':pagination})


def tweets_list(request):
	all_Words = ""
	TweetObject = Tweets.objects.all()
	Filtered_Tweets.objects.all().delete()
	filter_tweets = filterForm.tweetFilter()
	if request.method == "POST":
		form = formKeyWords.TweetKeyWords(request.POST)
		if form.is_valid():
			all_Words = form.cleaned_data['keyWords']
			formKeyWords.TweetKeyWords.keyWords = ""
			all_Words = re.sub('[!@$,-]', ' ', all_Words)
			all_keyWords = [x.strip() for x in all_Words.split()]
			conn = pymongo.MongoClient('localhost',27017)
			db = conn.TwitterStream;
			collections = db.tweets
			stream_1 = tweetPopulate.StreamTweets()
			# stream_1.stream(key_Words=all_keyWords)

			for obj in collections.find():
				Tweets(Id = obj['id'],user_id=obj['user_id'],favorites=obj['favorites'],friends=obj['friends'],followers=obj['followers'],User_name=obj['User_name'],Screen_name=obj['Screen_name'],
				tweet_date=obj['tweet_date'],retweet_count=obj['retweet_count'],User_mentions=obj['User_mentions'],tweet_text=obj['tweet_text'],Url_text=obj['Url_text']).save()
			TweetObject = Tweets.objects.all()

	print(TweetObject.count())

	tweet_per_page = 10
	current_page = int(request.GET.get('page',1))
	limit = tweet_per_page*current_page
	offset = limit - tweet_per_page
	tweet_table = TweetObject[offset:limit]
	total_tweets = TweetObject.count()

	total_pages = total_tweets // tweet_per_page
	if total_pages % tweet_per_page != 0 :
		total_pages += 1
	pagination = make_pagination_html(current_page, total_pages)

	return render(request,'twitterApi/tweets.html',{'tweet_table':tweet_table,'pagination':pagination,'filter_tweets':filter_tweets})

def make_pagination_html(current_page, total_pages):

	pagination_string = ""
	if current_page > 1:
		pagination_string += '<a href="?page=%s">previous</a>' % (current_page - 1)
	pagination_string += '<span class="current">  Page %s of %s   </span>'%(current_page, total_pages)

	if current_page < total_pages:
		pagination_string += '<a href="?page=%s">  next  </a>' % (current_page + 1)
	pagination_string += '<a href="?page=%s"> last &raquo;</a>'%(int(total_pages))

	return pagination_string

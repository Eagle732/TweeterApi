from .models import Tweets
def filtering(filtering_data):
    filtered_tweets = Tweets.objects.all()

    if filtering_data.cleaned_data['fromDate'] != None:
        filtered_tweets = filtered_tweets.filter(tweet_date__date__gte = filtering_data.cleaned_data['fromDate'])

    if filtering_data.cleaned_data['toDate'] != None:
        filtered_tweets = filtered_tweets.filter(tweet_date__date__lte = filtering_data.cleaned_data['toDate'])

    if filtering_data.cleaned_data['less_retweet'] != None:
        filtered_tweets = filtered_tweets.filter(retweet_count__lt = filtering_data.cleaned_data['less_retweet'])

    if filtering_data.cleaned_data['greater_retweet'] != None:
        filtered_tweets = filtered_tweets.filter(retweet_count__gt = filtering_data.cleaned_data['greater_retweet'])

    if filtering_data.cleaned_data['less_followers'] != None:
        filtered_tweets = filtered_tweets.filter(tweet_length__lt=filtering_data.cleaned_data['less_followers'])

    if filtering_data.cleaned_data['greater_followers'] != None:
        filtered_tweets = filtered_tweets.filter(tweet_length__gt = filtering_data.cleaned_data['greater_followers'])

    if filtering_data.cleaned_data['contains_char'] != None:
        filtered_tweets = filtered_tweets.filter(tweet_text__icontains = filtering_data.cleaned_data['contains_char'])

    if filtering_data.cleaned_data['Text_startWith'] != None:
        filtered_tweets = filtered_tweets.filter(tweet_text__icontains = filtering_data.cleaned_data['Text_startWith'])

    if filtering_data.cleaned_data['Text_endtWith'] != None:
        filtered_tweets = filtered_tweets.filter(tweet_text__icontains = filtering_data.cleaned_data['Text_endtWith'])

    if filtering_data.cleaned_data['Name_starttWith'] != None:
        filtered_tweets = filtered_tweets.filter(User_name__icontains = filtering_data.cleaned_data['Name_starttWith'])

    if filtering_data.cleaned_data['Name_endWith'] != None:
        filtered_tweets = filtered_tweets.filter(User_name__icontains = filtering_data.cleaned_data['Name_endWith'])

    return filtered_tweets

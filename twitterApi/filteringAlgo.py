from .models import Tweets
def filtering(filtering_data):
    filtered_tweets = Tweets.objects.all()
    # print(filtered_tweets.count())
    if filtering_data.cleaned_data['fromDate'] != None:
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(tweet_date__date__gte = filtering_data.cleaned_data['fromDate'])

    if filtering_data.cleaned_data['toDate'] != None:
        # print(2)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(tweet_date__date__lte = filtering_data.cleaned_data['toDate'])

    if filtering_data.cleaned_data['less_retweet'] != None:
        # print(3)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(retweet_count__lt = filtering_data.cleaned_data['less_retweet'])

    if filtering_data.cleaned_data['greater_retweet'] != None:
        # print(4)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(retweet_count__gt = filtering_data.cleaned_data['greater_retweet'])

    if filtering_data.cleaned_data['less_followers'] != None:
        # print(5)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(followers__lt=filtering_data.cleaned_data['less_followers'])

    if filtering_data.cleaned_data['greater_followers'] != None:
        # print(6)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(followers__gt = filtering_data.cleaned_data['greater_followers'])

    if filtering_data.cleaned_data['contains_char'] != "":
        # print(7)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(tweet_text__icontains = filtering_data.cleaned_data['contains_char'])

    if filtering_data.cleaned_data['Text_startWith'] != "":
        # print(8)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(tweet_text__istartswith = filtering_data.cleaned_data['Text_startWith'])

    if filtering_data.cleaned_data['Text_endtWith'] != "":
        # print(9)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(tweet_text__iendswith = filtering_data.cleaned_data['Text_endtWith'])

    if filtering_data.cleaned_data['Name_starttWith'] != "":
        # print("starts with")
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(User_name__startswith = filtering_data.cleaned_data['Name_starttWith'])
        # print(filtered_tweets)

    if filtering_data.cleaned_data['Name_endWith'] != "":
        # print(10)
        # print(filtered_tweets.count())
        filtered_tweets = filtered_tweets.filter(User_name__endswith = filtering_data.cleaned_data['Name_endWith'])

    return filtered_tweets

# TweeterApi
Tweeter Api which let you fetch tweets from twitter and can be used for data analysis
This MVP is made with Django backend framework.
1.  To run this Web app You have to first run requirement.txt to download all the revelent modules
2.  After that in web browser http://127.0.0.1:8000/ enter in url and you will get to front page
3.  After entering HashTag in the input field you have to wait for some time so that it can fetch data from server
4.  after fetching 100 tweets (which you can change in twitterApi/tweetPopulate.py file) it will go to next page where you can      see fetched tweets
5.  In the second page you can apply various filters like according to number to retweets number of followers etc,
6.   you can apply filers based on word start with in tweet text or user name etc, or you can search words in tweets.


I have applied various keys fetching which you can change according to your wish.I have restricted tweets parameters.
  Filtering algorithm is applied in filteringAlgo.py file
  parameters can be changed in models.py and tweetPopulate.py 
  
  
 And at last after filtering you can export filtered data in third page which will store tweets in CSV format in Media        
 directory
 

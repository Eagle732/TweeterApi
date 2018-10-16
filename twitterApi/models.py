from django.db import models

# Create your models here.
class KeyWords(models.Model):
	words = models.CharField(max_length=250)
	def __str__(self):
		return self.words


class Tweets(models.Model):
	Id = models.AutoField(primary_key=True,default=1)
	User_name = models.CharField(max_length=125)
	Screen_name = models.CharField(max_length=125)
	tweet_length = models.IntegerField()
	tweet_date = models.DateField()
	retweet_count = models.IntegerField()
	User_mentions = models.CharField(max_length=125)
	tweet_text = models.TextField(max_length=256)
	Url_text = models.URLField()
	

	def __str__(self):
		return self.User_name

import django_tables2 as tables
from .models import Tweets 
class TweetTables(tables.Table):
    class Meta:
        model = Tweets

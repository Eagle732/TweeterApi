from django.conf.urls import url
from django.urls import include
from . import views

app_name = 'twitterApi'

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tweets', views.tweets_list, name='index'),
    url(r'^filtered_tweets', views.fil_tweets, name='filtered_tweets'),
]

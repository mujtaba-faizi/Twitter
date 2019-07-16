from django.urls import path
from tweets import views


app_name = "tweets"
urlpatterns = [
    path('<int:user_id>/save/', views.save_tweet, name='save_tweet'),
    path('<int:pk>/tweetform/', views.InputTweet.as_view(), name='tweet_form'),

]

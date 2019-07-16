from django.urls import path
from tweets import views


app_name = "tweets"
urlpatterns = [
    path('<int:user_id>/save/', views.save_tweet, name='save_tweet'),
    path('<int:pk>/tweetform/', views.InputTweet.as_view(), name='tweet_form'),
    path('users/', views.show_users, name='show_all_users'),
    path('<int:pk>/profile/', views.ShowProfile.as_view(), name='user_profile'),
]

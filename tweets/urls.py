from django.urls import path
from tweets import views


app_name = "tweets"
urlpatterns = [
    path('<int:user_id>/save/', views.save_tweet, name='save_tweet'),
    path('<int:pk>/tweetform/', views.InputTweet.as_view(), name='tweet_form'),
    path('<int:follower_user_id>/users/', views.show_users, name='show_all_users'),
    path('<int:follower_user_id>/users/<int:followee_user_id>/follow/', views.add_follower, name='add_follower'),
    path('<int:pk>/profile/', views.ShowProfile.as_view(), name='user_profile'),
    path('<int:user_id>/<int:tweet_id>/<str:page>/', views.like, name='like'),
]

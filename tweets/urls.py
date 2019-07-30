from django.urls import path
from tweets import views


app_name = "tweets"
urlpatterns = [
    path('<int:user_id>/save/', views.save_tweet, name='save_tweet'),
    path('<int:pk>/tweetform/', views.InputTweet.as_view(), name='tweet_form'),
    path('<int:follower_user_id>/users/', views.show_users, name='show_all_users'),
    path('<int:user_id>/<int:profile_id>/profile/', views.show_profile, name='user_profile'),
    path('<int:user_id>/<int:profile_id>/<int:tweet_id>/<str:page>/like/', views.like, name='like'),
    path('<int:user_id>/<int:profile_id>/<int:tweet_id>/<str:page>/comment/', views.comment, name='comment_form'),
    path('<int:user_id>/<int:profile_id>/<int:tweet_id>/<str:page>/save_comment/', views.save_comment, name='comment'),
    path('<int:user_id>/<int:tweet_id>/comments/', views.show_comments, name='show_comments'),
    path('<int:user_id>/<int:tweet_id>/likes/', views.show_likes, name='show_likes'),
]

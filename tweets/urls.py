from django.urls import path
from tweets import views


app_name = "tweets"
urlpatterns = [
    path('<int:pk>/', views.save_tweet(), name='save_tweet'),

]

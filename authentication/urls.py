from django.urls import path
from authentication import views as views1
from tweets import views as views2


app_name = "authentication"
urlpatterns = [
    path('', views1.HomeView.as_view(), name='home'),
    path('signup/', views1.SignUp.as_view(), name='signup'),
    path('signup/save/', views1.save_user, name='save_user'),
    path('signup/authenticate/', views1.authenticate, name='authenticate'),
    path('<int:pk>/', views1.ShowUserHomepage.as_view(), name='user_home'),
    path('signin/', views1.SignIn.as_view(), name='signin'),
    path('<int:user_id>/save/', views2.save_tweet, name='save_tweet'),

]

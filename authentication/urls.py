from django.urls import path
from authentication import views


app_name = "authentication"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/save/', views.save, name='save'),
    path('signin/', views.SignIn.as_view(), name='signin'),
]

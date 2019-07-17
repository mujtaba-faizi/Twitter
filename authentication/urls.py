from django.urls import path
from authentication import views as views


app_name = "authentication"
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/save/', views.save_user, name='save_user'),
    path('signup/authenticate/', views.authenticate, name='authenticate'),
    path('<int:user_id>/', views.show_homepage, name='user_home'),
    path('<int:pk>/updateform/', views.Update.as_view(), name='update_form'),
    path('<int:user_id>/update/', views.update_profile, name='update'),
    path('signin/', views.SignIn.as_view(), name='signin'),

]

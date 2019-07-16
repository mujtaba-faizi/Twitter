from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import User


class HomeView(generic.TemplateView):
    template_name = 'authentication/home.html'


class SignUp(generic.TemplateView):
    template_name = 'authentication/signup.html'


class SignIn(generic.TemplateView):
    template_name = 'authentication/signin.html'


class SignOut(generic.TemplateView):
    template_name = 'authentication/home.html'


class ShowUserHomepage(generic.DetailView):
    model = User
    template_name = 'authentication/user_home.html'


def save_user(request):
    new_user = User()
    new_user.email = request.POST['email']
    new_user.password = request.POST['pass']
    new_user.first_name = request.POST['f_name']
    new_user.last_name = request.POST['l_name']
    new_user.username = request.POST['username']
    new_user.phone = request.POST['no']
    new_user.save()
    return HttpResponseRedirect(reverse('authentication:signin'))


def authenticate(request):
    username = request.POST['username']
    password = request.POST['pass']
    user = get_object_or_404(User, username=username, password=password)
    return HttpResponseRedirect(reverse('authentication:user_home', args=(user.id,)))




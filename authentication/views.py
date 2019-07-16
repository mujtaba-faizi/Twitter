from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import User
from tweets.models import Tweet


class HomeView(generic.TemplateView):
    template_name = 'authentication/home.html'


class SignUp(generic.TemplateView):
    template_name = 'authentication/signup.html'


class SignIn(generic.TemplateView):
    template_name = 'authentication/signin.html'


class SignOut(generic.TemplateView):
    template_name = 'authentication/home.html'


class Update(generic.DetailView):
    model = User
    template_name = 'authentication/update_form.html'


def show_homepage(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        tweets = Tweet.objects.all()
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'authentication/user_home.html', {'user': user, 'tweets': tweets})


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


def update_profile(request, user_id):
    try:
        email = request.POST['email']
        password = request.POST['pass']
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        phone = request.POST['no']
        user = User.objects.filter(id=user_id).update(email=email, password=password, first_name=first_name,
                                                      last_name=last_name, phone=phone)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return HttpResponseRedirect(reverse('authentication:user_home', args=(user_id,)))



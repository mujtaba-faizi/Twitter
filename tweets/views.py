from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Tweet, User


class InputTweet(generic.DetailView):
    model = User
    template_name = 'tweets/tweet.html'


class ShowProfile(generic.DetailView):
    model = User
    template_name = 'tweets/profile.html'


def save_tweet(request, user_id):
    new_tweet = Tweet()
    new_tweet.user_id = user_id
    new_tweet.text = request.POST['tweet']
    new_tweet.save()
    return HttpResponseRedirect(reverse('authentication:user_home', args=(user_id,)))


def show_users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'tweets/users.html', context)

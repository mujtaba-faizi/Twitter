from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Tweet, User, Follower


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


def show_users(request, follower_user_id):
    users = User.objects.all()
    context = {
        'users': users,
        'follower_user_id': follower_user_id,
    }
    return render(request, 'tweets/users.html', context)


def add_follower(request, follower_user_id, followee_user_id):
    try:
        Follower.objects.get(followee_id=followee_user_id, follower_id=follower_user_id)
    except (KeyError, Follower.DoesNotExist):       # If the user is not already followed
        new_follower = Follower()
        new_follower.follower_id = follower_user_id
        new_follower.followee_id = followee_user_id
        user = User.objects.get(pk=followee_user_id)
        new_follower.followee_name = user.username
        new_follower.save()
    return HttpResponseRedirect(reverse('tweets:show_all_users', args=(follower_user_id,)))

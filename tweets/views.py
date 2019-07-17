from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Tweet, User, Follower, Comment


class InputTweet(generic.DetailView):
    model = User
    template_name = 'tweets/tweet.html'


def show_profile(request, user_id, profile_id):
    user = User.objects.get(id=profile_id)
    context = {
        'user': user,
        'user_id': user_id,
    }
    return render(request, 'tweets/profile.html', context)


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


def like(request, user_id, tweet_id, page):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    tweet.likes += 1
    tweet.save()
    if page == 'user_home':
        return HttpResponseRedirect(reverse('authentication:user_home', args=(user_id,)))
    elif page == 'profile':
        return HttpResponseRedirect(reverse('tweets:user_profile', args=(user_id,)))


def comment(request, user_id, profile_id, tweet_id, page):
    context = {
        'user_id': user_id,
        'profile_id': profile_id,
        'tweet_id': tweet_id,
        'page': page
    }
    return render(request, 'tweets/comment_form.html', context)


def save_comment(request, user_id, profile_id, tweet_id, page):
    comment = Comment()
    comment.text = request.POST['comment']
    comment.tweet_id = tweet_id
    comment.user_id = user_id
    comment.save()
    if page == 'user_home':
        return HttpResponseRedirect(reverse('authentication:user_home', args=(user_id,)))
    elif page == 'profile':
        return HttpResponseRedirect(reverse('tweets:user_profile', args=(user_id, profile_id)))


def show_comments(request, user_id, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    context = {
        'user_id': user_id,
        'tweet': tweet,
    }
    return render(request, 'tweets/comments.html', context)




from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Tweet


class InputTweet(generic.TemplateView):
    template_name = 'tweets/tweet.html'


def save_tweet(request, user_id):
    new_tweet = Tweet()
    new_tweet.user_id = user_id
    new_tweet.text = request.POST['yo']
    new_tweet.save()
    return HttpResponseRedirect(reverse('authentication:user_home'))

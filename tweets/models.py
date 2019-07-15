from authentication.models import User
from django.db.models import Model, CharField, DateTimeField, IntegerField, ForeignKey, CASCADE


class Tweet(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    text = CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    likes = IntegerField(default=0)

    def __str__(self):
        return self.text


class Comment(Model):
    tweet = ForeignKey(Tweet, on_delete=CASCADE)
    text = CharField(max_length=200)

    def __str__(self):
        return self.text


class Follower(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=200)

    def __str__(self):
        return self.name

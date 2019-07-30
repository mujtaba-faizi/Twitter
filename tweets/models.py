from users.models import User
from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE


class Tweet(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    text = CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Comment(Model):
    tweet = ForeignKey(Tweet, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    text = CharField(max_length=200)

    def __str__(self):
        return self.tweet.text


class Like(Model):
    tweet = ForeignKey(Tweet, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.tweet.text

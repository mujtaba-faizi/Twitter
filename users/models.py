from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE
from django.core.validators import RegexValidator


class User(Model):
    username = CharField(max_length=30)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    email = CharField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = CharField(validators=[phone_regex], max_length=17)
    password = CharField(max_length=20)

    def __str__(self):
        return self.username


class Follower(Model):
    follower_user = ForeignKey(User, on_delete=CASCADE, related_name="following")
    followee_user = ForeignKey(User, on_delete=CASCADE, related_name="followed_by")

    def __str__(self):
        return self.follower_user.username

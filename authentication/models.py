from django.db.models import Model, CharField
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

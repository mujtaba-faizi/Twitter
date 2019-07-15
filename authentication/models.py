from django.db.models import Model, CharField
from django.core.validators import RegexValidator


class User(Model):
    name = CharField(max_length=200)
    password = CharField(max_length=20)
    email = CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.name


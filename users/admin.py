from django.contrib import admin
from .models import User, Follower


admin.site.register(User)
admin.site.register(Follower)
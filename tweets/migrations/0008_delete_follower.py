# Generated by Django 2.2.3 on 2019-07-22 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_comment_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follower',
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-22 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190722_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='followee_id',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='followee_name',
        ),
        migrations.AddField(
            model_name='follower',
            name='followee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followees', to='users.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follower',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='users.User'),
        ),
    ]

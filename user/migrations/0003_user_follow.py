# Generated by Django 4.2.5 on 2023-09-10 12:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(related_name='followee', to=settings.AUTH_USER_MODEL),
        ),
    ]

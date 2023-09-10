from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={"unique": "이미 존재하는 닉네임입니다"},
    )
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')

    def __str__(self):
        return self.email

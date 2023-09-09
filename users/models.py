from django.contrib.auth.models import AbstractUser
from django.db import models

from goodhabits.models import NULLABLE


class User(AbstractUser):
    username = None
    surname = models.CharField(max_length=35, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    chat_id = models.CharField(max_length=20, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

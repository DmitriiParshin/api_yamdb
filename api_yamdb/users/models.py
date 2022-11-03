from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True,)
    first_name = models.CharField(max_length=150,)
    last_name = models.CharField(max_length=150,)
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(max_length=9, choices=ROLE_CHOICES, default='user')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

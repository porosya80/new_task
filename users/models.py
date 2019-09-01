from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length = 30)
    email = models.EmailField(('email address'), unique=True)
    location = models.CharField(blank=True, null= True, max_length = 50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.email}"

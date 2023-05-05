from django.contrib.auth.models import AbstractUser
from django.db import models

from books.models import Book


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    student = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

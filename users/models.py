from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=120, unique=True)
    student = models.BooleanField(default=True)
    blocked = models.BooleanField(null=True, default=False)
    super_user = models.BooleanField(null=True, default=False)

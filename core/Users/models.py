from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    middle_name = models.CharField(max_length=25)
    sex = models.CharField(max_length=10, default="male")

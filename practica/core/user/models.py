from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=150)

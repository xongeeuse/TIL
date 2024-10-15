from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    subscription = models.ManyToManyField('User', symmetrical=False, related_name='subscriber')
    
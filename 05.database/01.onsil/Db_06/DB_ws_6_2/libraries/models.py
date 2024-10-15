from django.db import models
from django.conf import settings

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscribed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribed_authors')
    nickname = models.CharField(max_length=20)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=10)

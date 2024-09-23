from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    description = models.TextField
    pubdate = models.DateField()
    isbn = models.CharField(max_length=10)
    price = models.IntegerField()
    adult = models.BooleanField()
    stockstatus = models.BooleanField()

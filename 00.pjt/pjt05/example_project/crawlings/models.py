from django.db import models


class Article(models.Model):
    query = models.TextField()
    title = models.TextField()

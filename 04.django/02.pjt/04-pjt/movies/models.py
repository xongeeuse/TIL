from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    plot = models.TextField()
    image = models.ImageField(blank=True, upload_to='posters/')
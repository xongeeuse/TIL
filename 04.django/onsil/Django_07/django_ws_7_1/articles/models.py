from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='media/')
    image_description = models.TextField(blank=True)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

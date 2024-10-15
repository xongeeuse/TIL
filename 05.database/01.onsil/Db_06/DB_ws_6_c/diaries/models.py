from django.db import models
from django.conf import settings

# Create your models here.
class Diary(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=125)
    picture = models.ImageField(blank=True, upload_to='diary/%y/%b/%a')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)
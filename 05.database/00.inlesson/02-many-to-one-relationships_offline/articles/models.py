# articles/models.py
from django.db import models
from django.conf import settings
# from accounts.models import User

# Article (N) : User (1)
class Article(models.Model):
    # user에 대한 정보 외래키로 설정
    # 일반적인 다른 app으로부터 Model을 import 받아왔을 때 발생하는 문제
    # settings.py => INSTALLED_APPS에 등록한 순서에 영향을 받는다.
    # 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

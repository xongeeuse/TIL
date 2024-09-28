from django.db import models

# Create your models here.
# ()에 들어가는 요소는 상위 클래스, 상속의 의미
# 위에서 import한 models모듈의 Model 클래스 상속 받겠어!
class Article(models.Model):
    # CharField 이름에서 클래스라는 것을 알 수 있음!
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
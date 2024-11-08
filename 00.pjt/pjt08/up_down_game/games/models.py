from django.db import models

# Create your models here.
class GameSession(models.Model):
    target_number = models.IntegerField()       # 정답
    user_guess = models.IntegerField(null=True)          # 사용자의 추측
    attempts = models.IntegerField(default=0)   # 추측 횟수
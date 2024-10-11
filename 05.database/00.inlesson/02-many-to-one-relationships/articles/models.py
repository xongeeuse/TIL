from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # ForeignKey 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성 권장
    # 외래 키는 ForeignKey 클래스를 작성하는 위치와 관계 없이 테이블의 마지막 필드로 생성
    # 참조할 모델 클래스 = models.ForeignKey(상대 모델 클래스, 상대 모델 클래스가 삭제되었을 때 댓글 처리 방식)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# 인증된 사용자에게 자동으로 토큰을 생성해주는 역할
# 당연히 DRF 가이드에 맞추어 작성한 코드
# 외워서 하는거 아님~!

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

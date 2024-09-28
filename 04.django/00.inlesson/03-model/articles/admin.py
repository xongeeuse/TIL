from django.contrib import admin
from .models import Article

# Register your models here.
# `admin` `site`에 `등록`한다! 순서로 기억하기!
admin.site.register(Article)
from django.db import models


# 제약조건을 반드시 파악하고 아래 코드를 작성
class Weather(models.Model):
    date = models.DateField() # 연도-월-일 형식의 날짜 데이터, 결측치 X
    temp_avg_f = models.IntegerField() # 정수형, 결측치 X
    # sqlite3 는 리스트 필드가 없다!!
    # 문자열 저장, 활용할 때 콤마로 분리(split)
    events = models.CharField(max_length=255, blank=True, null=True) # 결측치 O, 1개 이상일 수 있다.
    

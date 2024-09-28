from django.db import models
import requests

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    @classmethod
    def insert_data(cls):
        response = requests.get('https://api.example.com/data')
        data = response.json()

        for item in data:
            my_model = cls(field1=item['field1'], field2=item['field2'])
            my_model.save()

# django shell에서 아래 코드 실행
# MyModel.insert_data()
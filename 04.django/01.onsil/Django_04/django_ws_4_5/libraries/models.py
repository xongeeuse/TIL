from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
        API_KEY = 'ttbjiyyyyy_1123001'
        params = {
             'ttbkey': API_KEY,
             'QueryType': 'ItemNewSpecial',
             'SearchTarget': 'Book',
             'Start': 1,
             'MaxResults': 50,
             'Output': 'JS',
             'Version': '20131101',
        }

        response = requests.get(API_URL, params=params).json()
        data = response['item']

        for d in data:
            book = cls(isbn = d['isbn'],
                       author = d['author'],
                       title = d['title'],
                       category_name = d['categoryName'],
                       category_id = d['categoryId'],
                       price = d['priceSales'],
                       fixed_price = d['fixedPrice'],
                       pub_date = d['pubDate'],
                       )
            book.save()

# django shell에서 아래 코드 실행
# book.insert_data()


# class MyModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()

#     @classmethod
#     def insert_data(cls):
#         response = requests.get('https://api.example.com/data')
#         data = response.json()

#         for item in data:
#             my_model = cls(field1=item['field1'], field2=item['field2'])
#             my_model.save()

# django shell에서 아래 코드 실행
# MyModel.insert_data()
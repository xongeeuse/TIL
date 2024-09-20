import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbjiyyyyy_1123001'

params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

response = requests.get(API_URL, params=params).json()

result = []
for item in response['item']:
    info = {
        'isbn': item['isbn'],
        'title': item['title'],
        'pubDate': item['pubDate'],
        'author': item['author'],
        'bestDuration': item.get('bestDuration'),
    }
    result.append(info)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)

def bestseller(request):
    context = {
        'result': result
    }
    return render(request, 'bestseller.html', context)
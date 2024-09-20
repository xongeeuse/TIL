from django.shortcuts import render
import requests

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

books_info = []
for i in range(len(response['item'])):
    temp = {}
    temp['국제 표준 도서 번호'] = response['item'][i]['isbn']
    temp['author'] = response['item'][i]['author']
    temp['title'] = response['item'][i]['title']
    temp['출간일'] = response['item'][i]['pubDate']
    books_info.append(temp)

# Create your views here.
def intro(request):
    return render(request, 'libraries/intro.html')

def recommend(request):
    context = {
        'books_info' : books_info,
    }
    
    return render(request, 'libraries/recommend.html', context)
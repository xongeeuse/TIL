import requests
from pprint import pprint

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

result = []
for i in range(len(response['item'])):
    temp = {}
    temp['국제 표준 도서 번호'] = response['item'][i]['isbn']
    temp['저자'] = response['item'][i]['author']
    temp['제목'] = response['item'][i]['title']
    temp['출간일'] = response['item'][i]['pubDate']
    result.append(temp)
pprint(result)
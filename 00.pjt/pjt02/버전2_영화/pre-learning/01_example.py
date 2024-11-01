# requests 사용 예시 1

from pprint import pprint
import requests


URL = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(URL).json()
pprint(response)

results = response.get('message')
pprint(results)

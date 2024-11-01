from bs4 import BeautifulSoup
import requests

def crawling_basic():
    # 가져올 url 문자열로 입력
    url = 'https://www.google.com/search?q=%ED%83%95%EC%88%98%EC%9C%A1&oq=%ED%83%95%EC%88%98%EC%9C%A1&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDE2MTBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'  

    # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
    response = requests.get(url)    

    # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
    html_text = response.text

    print(html_text)

    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(html_text)

    



crawling_basic()

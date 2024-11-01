from django.shortcuts import render
from .models import Article

from bs4 import BeautifulSoup
from selenium import webdriver

def get_google_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")

    # div 태그 중 g 클래스를 가진 모든 요소 선택
    g_list = soup.select("div.g")

    titles = []
    # 해당 요소를 반복하며
    for g in g_list:
        # 요소 안에 LC20lb MBeuO DKV0Md 클래스를 가진 특정 요소 선택
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")
        # 요소가 존재 한다면
        if title is not None:
            title_text = title.text
            titles.append(title_text)

    return titles
            


def index(request):
    # 사용자가 검색을 하면 크롤링을 진행
    if request.method == 'POST':
        results = []  # 검색 결과
        query = request.POST.get('query')
        titles = get_google_data(query)
        
        for title in titles:
            # Article 을 저장
            # Article.objects.create(query=query, title=title)

            # # 중복을 제거하자
            # if not Article.objects.filter(query=query, title=title).exists():
            #     Article.objects.create(query=query, title=title)

            # get_or_create: 있으면 가져오고, 없으면 저장해라!
            article, created_article = Article.objects.get_or_create(query=query, title=title)

    context = {
        'results': Article.objects.all()
        # [도전] 버그 없도록 수정해보기!
        # 'results': Article.objects.filter(query=query)
    }

    # 아니라면, 그냥 검색 페이지를 제공
    return render(request, 'crawlings/index.html', context)

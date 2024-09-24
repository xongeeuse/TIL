from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # URL로부터 전달받은 pk를 활용해 데이터 조회
    # 단일 게시글 조회니까 get()메서드 사용할 것
    # get() 이용 시 고유한 값으로 검색해야 함 => 검색 결과 없거나 복수면 에러
    
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }    
    
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

# 과거 catch에서 했던 역할
def create(request):
    # 사용자 요청으로부터 입력 데이터를 추출
    # 추출한 입력 데이터를 활용해 DB에 저장 요청
        # 입력 데이터가 어디 있냐? => request
        # request.GET에 querydict라는 딕셔너리 형태로 저장되어 있음
    title = request.POST.get('title')
    content = request.POST.get('content')


    # 1, 2번 방식은 유효성 검사할 타이밍 있음 => save 전
    # 3번은 타이밍이 없어 but 우리는 유효성 검사할거라서
    # 조금 더 편한 2번 쓸게~!

    # 저장 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 저장 2
    article = Article(title=title, content=content)
    article.save()

    # 저장 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    # 삭제하려면 먼저 조회가 이루어져야 함
    # 어떤 게시글 삭제할 지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 어떤 게시글 수정할지 조회
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 사용자로부터 받은 새로운 입력 데이터 추출
    article.title = title
    article.content = content
    # 기존 게시글의 데이터를 사용자로 받은 데이터로 새로 할당
    article.save()
    
    return redirect('articles:detail', article.pk)
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 전체 게시글 목록 확인
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def new(request):
    # 게시글 생성 위한 form 보여주기
    
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')
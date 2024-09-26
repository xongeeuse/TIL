from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def create(request):
    
    # CRUD 안보고 다시 만들어보자
    # create 함수 작성하기!!!!!
    # 여기서부터 할 차례!!!!!
    return render(request, 'my_app/create.html')

# def detail(request, pk):
#     return

# def update(request, pk):
#     return

# def delete(request, pk):
#     return
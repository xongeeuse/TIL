from django.shortcuts import render, redirect
from .models import Author, Book

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors' : authors,
    }
    return render(request, 'libraries/index.html', context)

def detail(request, pk):
    author = Author.objects.get(pk=pk)
    context = {
        'author' : author,
    }
    return render(request, 'libraries/detail.html', context)
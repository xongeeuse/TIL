from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    context = {
        'book': book,
    }
    return render(request, 'libraries/detail.html', context)

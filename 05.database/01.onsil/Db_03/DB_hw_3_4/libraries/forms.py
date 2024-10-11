from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('author',)
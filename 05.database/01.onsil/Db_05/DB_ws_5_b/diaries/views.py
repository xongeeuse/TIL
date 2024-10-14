from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comment_form = CommentForm()
    context = {
        'diaries': diaries,
        'comment_form': comment_form
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comments_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary = diary
            comment.save()
    return redirect('diaries:index')

def comments_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('diaries:index')


@login_required
def likes(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    if request.user not in diary.like_users.all():
        diary.like_users.add(request.user)
    else:
        diary.like_users.remove(request.user)
    return redirect('diaries:index')
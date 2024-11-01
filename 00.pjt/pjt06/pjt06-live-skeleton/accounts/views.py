from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원 가입 후 바로 로그인
            auth_login(request, user)
            return redirect("boards:index")
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # next 가 있다면, next 경로로 보내라
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


@require_http_methods(["POST"])
def logout(request):
    # DB 에서 세션 삭제, 쿠키에서 sessionId 삭제 등등
    auth_logout(request)
    return redirect("boards:index")

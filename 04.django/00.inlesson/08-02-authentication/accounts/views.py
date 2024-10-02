from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    # 인증된 사용자(로그인된 사용자)는 아래 로직을 수행할 수 없도록!
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


# create 함수 로직과 유사
def signup(request):
    # 인증된 사용자(로그인된 사용자)는 아래 로직을 수행할 수 없도록!
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # 굳이 User가 누구인지 검색할 필요없음
    # 이미 로그인된 상태로 여기까지 왔으니까 request에 user정보가 담겨 있음
    # user = request.user
    # user.delete()
    # 변수 안 담고 그냥 아래 형식으로 써도 됨
    request.user.delete()

    # 탈퇴와 함께 기존 사용자의 Session Data 삭제 방법
    # '탈퇴 후 로그아웃'의 순서가 바뀌면 안ㄴ됨
    auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request, user_pk):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 변경이 일어난 다음에 추가
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
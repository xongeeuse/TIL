from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == "POST":
        # 모델폼과 매개변수의 구성 순서 다름
        # 첫번째 인자가 데이터가 아니라는 것!
        # 첫번째 인자는 request, 두번째가 data
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 만약 인증된 사용자라면 로그인 진행(session데이터 생성)
            # auth_login(request, 인증된 유저 객체)
            user = form.get_user()
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    # if request.method = "POST":
    # 세션 데이터 삭제
    auth_logout(request)
    return redirect('articles:index')
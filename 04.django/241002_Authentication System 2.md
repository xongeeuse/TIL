# 241002_Authentication System 2

## 회원 가입
- User 객체를 Create하는 과정

### UserCreationForm()
- 회원 가입 시 사용자 입력 데이터를 받는 built-in ModelForm
- 로그인할 때는 Form이었지만, 회원가입은 ModelForm 사용!

#### 커스텀 유저 모델을 사용하려면 다시 작성해야 하는 Form
- `UserCreationForm`, `UserChangeForm`
- 두 Form 모두 Meta class 에서 User가 작성되었기 때문에 재작성 필요

  ```python
  from django.contrib.auth.forms import UserCreationForm, UserChangeForm
  # django는 User모델을 직접 참조하는 것을 권장하지 않음
  # from .models import User
  # 그래서 django는 User모델을 간접적으로 참조할 수 있는 방법을 별도로 제공
  # get_user_model << 함수니까 리턴 있겠쥬 : 현재 프로젝트에서 활성화된 User모델 객체 반환
  from django.contrib.auth import get_user_model

  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
          model = get_user_model()

  class CustomUserChangeForm(UserChangeForm):
      class Meta(UserChangeForm.Meta):
          model = get_user_model()
  ```

  ```python
  # 기존 create 함수 로직과 유사
  def signup(request):
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
  ```

##### get_user_model()
- 현재 프로젝트에서 활성화된 사용자 모델을 반환하는 *함수*
- User 모델을 직접 참조하지 않는 이유
  - `get_user_model()`을 사용해 User 모델을 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문
  - Django는 필수적으로 User 클래스를 직접 참조하는 대신, `get_user_model()`을 사용해 참 조해야 한다고 강조하고 있음
  - User model 참조에 대한 자세한 내용은 추후 모델 관계에서 다룰 예정

## 회원 탈퇴
- User 객체를 `Delete`하는 과정
- `logout`과 유사하지만 삭제하는 대상이 다름
- *`logout`은 만들어진 session 삭제, 탈퇴는 만들어진 회원 정보 완전 삭제*

  ```python
  def delete(request):
      # 굳이 User가 누구인지 검색할 필요없음
      # 이미 로그인된 상태로 여기까지 왔으니까 request에 user정보가 담겨 있음
      user = request.user
      user.delete()
      # 변수 안 담고 그냥 아래 형식으로 써도 됨
      # request.user.delete()
      return redirect('articles:index')
  ```

## 회원정보 수정
- User 객체를 Update하는 과정
- Session 정보 변경

### UserChangeForm()
- 위에서 UserCreateForm() 커스텀할 때, 미리 모델폼 수정 생성해뒀음
  ```python
  # accounts/forms.py
  class CustomUserChangeForm(UserChangeForm):
      # password = None

      class Meta(UserChangeForm.Meta):
          model = get_user_model()
          fields = ('first_name', 'last_name', 'email')

  # accounts/views.py
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
  ```

## 비밀번호 변경
- 인증된 사용자의 session 데이터를 update하는 과정

### PasswordChangeForm()
- 비밀번호 변경 시 사용자 입력 데이터를 받는 built-in **Form**
- django에서 주어지는 `/user_pk/password/` 이용할 예정

### update_session_auth_hash(request, user)
- 암호 변경 시 세션 무효화를 막아주는 함수
- 필수는 아니고 비밀번호 변경 이후 로그아웃을 방지하고 싶다면 이용!
> 암호가 변경되면 새로운 password의 session data로 기존 session을 자동으로 갱신

  ```python
  # 프로젝트/urls.py
  # 기존 urlpatterns에 경로 추가
    urlpatterns = [
      path('<int:user_pk>/password/', views.change_password, name="change_password"),
    ]

    # accounts/views.py
    def change_password(request, user_pk):
        if request.method == "POST":
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                # 비밀번호 변경이 일어난 다음에 추가
                update_session_auth_hash(request, user)
                return redirect('articles:index')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form' : form,
        }
        return render(request, 'accounts/change_password.html', context)
  ```

## 인증된 사용자에 대한 접근 제한
- 로그인 사용자에 대해 접근을 제한하는 2가지 방법
1. `is_authenticated` 속성
2. `login_required` 데코레이터
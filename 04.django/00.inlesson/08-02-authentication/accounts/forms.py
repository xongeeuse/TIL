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
    # password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')


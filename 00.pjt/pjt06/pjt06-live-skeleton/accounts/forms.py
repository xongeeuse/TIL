from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    # model 속성을 제외하고는 나머지는 모두 Meta 클래스 내용을 그대로 가져오면 된다.
    # 아래처럼 Meta class 도 상속받아서 써도 된다.
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

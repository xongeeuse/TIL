from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        # id, password, password2 만 입력받음
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
        
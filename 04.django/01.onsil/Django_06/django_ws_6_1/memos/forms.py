from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    # memo에 플레이스 홀더 추가
    # memo 사이즈 가로세로50
    # summary에 플레이스 홀더 추가
    memo = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'placeholder' : 'memo를 입력하세요.',
                'rows' : 5,
                'cols' : 50,
            }
        )
    )

    summary = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'summary를 입력하세요.',
                'maxlength' : 20,
            }
        )
    )

    class Meta:
        model = Memo
        fields = '__all__'
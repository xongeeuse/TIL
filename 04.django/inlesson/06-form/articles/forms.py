from django import forms
from .models import Article

# 그냥 Form 사용하는 방식
# 틀린 건 아니지만 적합한 form은 아님
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


# ModelForm 사용
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'px-5 mt-5',
                'placeholder' : '제목을 입력해주세요.',
                'maxlength' : 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력해주세요.'}
    )

    class Meta:
        model = Article
        fields = '__all__'
        # title 빼고 폼 생성하려면 (,)
        # 튜플에 요소 하나만 넣을 때는 ,넣어서 튜플인거 알려주기!
        # exclude = ('title',)
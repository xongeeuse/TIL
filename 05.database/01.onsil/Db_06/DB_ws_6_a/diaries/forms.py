from django import forms
from .models import Diary, Comment


class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        # fields = '__all__'
        exclude = ('like_users', )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ('content',)
        exclude = ('diary', )
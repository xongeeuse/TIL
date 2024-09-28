from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    # location에 ex)제주도 플레이스홀더 추가
    # start_date, end_date에 ex)2022-02-22 플레이스홀더 추가

    location = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'ex)제주도',
                'maxlength' : 10,
            }
        )
    )

    start_date = forms.DateField(
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'ex)2022-02-22',
            }
        )
    )

    end_date = forms.DateField(
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'ex)2022-02-22',
            }
        )
    )

    class Meta:
        model = Travel
        fields = "__all__"


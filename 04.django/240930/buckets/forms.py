from django import forms
from .models import TravelBucketList


class TravelBucketListForm(forms.ModelForm):
    class Meta:
        model = TravelBucketList
        # fields = '__all__'
        exclude = ['reason', 'city']
        widgets = {
            'destination_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
            'planned_visit_date': forms.DateInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }

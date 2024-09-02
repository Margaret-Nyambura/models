from django import forms
from .models import Period

class PeriodRegistationForm(forms.ModelForm):
    class Meta:
        model=Period
        fields="__all__"
from django import forms
from .models import Student


class StudentRegistationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=["first_name","last_name","code","email","age","country","phone_number","next_of_kin","bio","course","classes"]
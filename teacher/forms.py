from django import forms
from .models import Teacher

class TeacherRegistationForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=["teacher_age","teacher_name","teacher_id","teacher_course","teacher_contact","teacher_description","teacher_occupation","teacher_salary","teacher_bank_account","course","classes"]
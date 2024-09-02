from django import forms
from .models import Course

class CourseRegistationForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=["course_name","course_id","course_code","course_TA","course_term","course_description","course_department","course_syllabus","course_instructor","course_duration"]
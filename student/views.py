from django.shortcuts import render
from .forms import StudentRegistationForm

# Create your views here.

def register_student(request):
    form=StudentRegistationForm()
    return render(request,"student/register_student.html", {"forms":form})


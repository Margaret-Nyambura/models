from django.shortcuts import render
from .forms import TeacherRegistationForm

# Create your views here.

def register_teacher(request):
    
    if request.method=="POST":
        form=TeacherRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register_teacher")
        
    else:
        form=TeacherRegistationForm()
        
    return render(request,"teacher/register_teacher.html",{"form":form})

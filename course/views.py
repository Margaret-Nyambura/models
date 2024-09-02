from django.shortcuts import render,redirect
from .forms import CourseRegistationForm

# Create your views here.

def register_course(request):
    form=CourseRegistationForm()
    
    if request.method=="POST":
        form= CourseRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("register_course")
    
    else:
        form=CourseRegistationForm()
        
    return render(request,"course/register_course.html", {"form":form})

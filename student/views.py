from django.shortcuts import render,redirect
from .forms import StudentRegistationForm

# Create your views here.

def register_student(request):
    # form=StudentRegistationForm()
    # return render(request,"student/register_student.html", {"form":form})

    if request.method=="POST":
        form= StudentRegistationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("register_student")
    
    else:
        form=StudentRegistationForm()
        
    return render(request,"student/register_student.html", {"form":form})


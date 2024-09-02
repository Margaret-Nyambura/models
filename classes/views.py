from django.shortcuts import render,redirect
from .forms import ClassesRegistationForm

# Create your views here.

def register_classes(request):
    
    if request.method=="POST":
        form=ClassesRegistationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("register_classes")
        
    else:
        form=ClassesRegistationForm()
        
    return render(request,"classes/register_classes.html", {"form":form})

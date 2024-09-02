from django.shortcuts import render
from .forms import PeriodRegistationForm

# Create your views here.

def register_period(request):
    if request.method=="POST":
        form=PeriodRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register_period")
        
    else:
        form=PeriodRegistationForm()
    
    return render(request,"period/register_period.html", {"form":form})

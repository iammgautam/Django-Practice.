from django.shortcuts import render
from .models import Student
from .forms import PersonForm

# Create your views here.

def get_list(request):
    list = Student.objects.all()
    context = {
        'fullview':list,
    }
    return render(request, 'app/main.html', context)

def startingWithB(request):
    StartsWithB = Student.objects.filter(stuname__startswith = 'R')
    print(StartsWithB)
    context_filter = {
        'filter':StartsWithB,
    }
    return render(request, 'app/main.html', context_filter)

def getform(request):
    fm = PersonForm()
    return render(request, 'app/main.html', {'form':fm})
from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
# Create your views here.

def form(request):
    if request.method == 'POST':
        fm = PersonForm(request.POST)
        if fm.is_valid():
            Name = fm.cleaned_data['name']
            Email = fm.cleaned_data['email']
            Pass = fm.cleaned_data['password']
            reg = Person(name =Name, email = Email, password=Pass)
            reg.save()
            fm = PersonForm()
            return redirect(request.path)
    else:
        fm = PersonForm()
    return render(request, 'app2/mail.html', {'form':fm})

def getlist(request):
    list = Person.objects.all()
    return render(request, 'app2/mail.html', {'fullview':list})
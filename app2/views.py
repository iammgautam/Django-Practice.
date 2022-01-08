from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
# Create your views here.

#this function will signup users.
def register(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created SUccessfully!!')
            fm.save()
            return redirect("signup")
    else:
        fm = RegisterForm()
    return render(request, 'app2/signup.html', {'form':fm})

#this function will sumbit the form and display the list.
def form(request):
    if request.method == 'POST':
        fm = PersonForm(request.POST)
        if fm.is_valid():
            Name = fm.cleaned_data['name']
            Email = fm.cleaned_data['email']
            Pass = fm.cleaned_data['password']
            reg = Person(name =Name, email = Email, password=Pass)
            reg.save()
            messages.add_message(request, messages.SUCCESS, 'Your Account has been created!!')
            fm = PersonForm()
            return redirect(request.path)
    else:
        fm = PersonForm()

    list = Person.objects.all()
    context = {
        'form':fm,
        'fullview':list,
    }
    return render(request, 'app2/mail.html', context)

def detail(request, id):
    getit = Person.objects.get(pk=id)
    context = {
        'detail':getit,
    }
    context['data'] = Person.objects.get(pk=id)
    return render(request, 'app2/detail.html', context)

def update(request, id):
    person = Person.objects.get(pk = id)
    if request.method == 'POST':
        updateitem = Person.objects.get(pk = id)
        fm = PersonForm(request.POST, instance = updateitem)
        if fm.is_valid():
            fm.save()
    else:
        updateitem = Person.objects.get(pk = id)
        fm = PersonForm(instance = updateitem)
    context = {
        'form':fm,
        'person':person
    }
    return render(request, 'app2/update.html', context)

    #this function is for deleting the item
def delete(request, id):
    if request.method == 'POST':
        delitem = Person.objects.get(pk=id)
        delitem.delete()
        return HttpResponseRedirect('/')
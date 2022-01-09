from django.contrib import auth
from django.contrib.auth.backends import RemoteUserBackend
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#this function will allow users to login
def signin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:
            fm = AuthenticationForm()
        return render(request,'app2/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/')

#this function will help o logout the user
def user_logout(request):
    logout(request)
    # return render_to_response('login.html', {'request': request})
    return HttpResponseRedirect('/login/')

# this function will signup users.
def register(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created SUccessfully!!')
            fm.save()
            return redirect("login")
    else:
        fm = RegisterForm()
    return render(request, 'app2/signup.html', {'form':fm})

#this function will sumbit the form and display the list.
def form(request):
    if request.user.is_authenticated:
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

        list = Person.objects.all()
        context = {
            'form':fm,
            'fullview':list,
        }
        return render(request, 'app2/mail.html', context)
    else:
        return render(request, 'app2/error404.html')

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

def mainpage(request):
    if request.user.is_authenticated:
        return render(request, 'app2/profile.html', {'form':request.user})
    else:
        return render(request, 'app2/error404.html')
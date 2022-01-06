from django.shortcuts import render
from .forms import Person
# Create your views here.

def postform(request):
    if request.method == 'POST':
        fm = Person(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name:',fm.cleaned_data['name'])
    else:
        fm = Person()
    return render(request, 'app2/mail.html', {'form':fm})
from django import forms
from django.forms import widgets
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','email', 'password']
        widgets = {
            'password':forms.PasswordInput(attrs={'placeholder':'Enter password'}),
        }
from django import forms
from django.forms import widgets
from .models import Person

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password(again)',
    widget =forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']
        label = {
            'email':'Email',
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','email', 'password']
        widgets = {
            'password':forms.PasswordInput(attrs={'placeholder':'Enter password'}),
        }
from django import forms

GENDER_CHOICE = [
    ('Male','Male'),
    ('Female','Female'),
]

class Person(forms.Form):
    name = forms.CharField(label = 'Your Name:: ')

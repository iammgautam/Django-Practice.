from django import forms

# GENDER_CHOICE = [
#         ('Male','Male'),
#         ('Female', 'Female'),
#     ]

class PersonForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    # gender = forms.ChoiceField(choices= GENDER_CHOICE)
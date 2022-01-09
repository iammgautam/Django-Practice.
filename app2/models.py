from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
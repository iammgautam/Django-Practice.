from django.urls import path
from .views import postform
urlpatterns = [
    path('', postform, name='form'),
]

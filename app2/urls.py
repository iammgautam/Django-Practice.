from django.urls import path
from .views import form, getlist
urlpatterns = [
    path('', form, name='form'),
    path('list/', getlist, name='list')
]

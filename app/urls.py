from django.urls import path
from .views import get_list

urlpatterns = [
    path('', get_list, name='home'),
]
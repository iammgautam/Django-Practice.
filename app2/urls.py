from django.urls import path
from .views import delete, form, detail, update, register
urlpatterns = [
    path('signup/', register, name='signup'),
    path('', form, name='form'),
    path('<int:id>/',detail, name='detail'),
    path('delete/<int:id>/', delete, name='delete'),
    path('update/<int:id>/',update, name='update'),
]

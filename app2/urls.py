from django.urls import path
from .views import delete, form, detail, update, register,signin, user_logout, mainpage
urlpatterns = [
    path('login/',signin, name='login'),
    path('logout/',user_logout, name='logout'),
    path('signup/', register, name='signup'),
    path('profile/',mainpage,name='profile'),
    path('', form, name='form'),
    path('<int:id>/',detail, name='detail'),
    path('delete/<int:id>/', delete, name='delete'),
    path('update/<int:id>/',update, name='update'),
]

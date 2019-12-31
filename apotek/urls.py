from django.urls import path
from . import views

app_name = 'apotek'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/landing/', views.user_landing, name='user_landing'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/register/', views.user_register, name='user_register'),
    path('user/logout/', views.user_logout, name='user_logout')
]
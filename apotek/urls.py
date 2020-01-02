from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'apotek'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/auth/', views.user_auth, name='user_auth'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('<int:page>/', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
]
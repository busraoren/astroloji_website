from django.urls import path
from . import views

urlpatterns = [
    path('', views.numeroloji_formu, name='numeroloji'),
]
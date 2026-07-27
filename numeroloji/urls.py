from django.urls import path
from . import views

urlpatterns = [
    path('', views.numeroloji_formu, name='numeroloji'),
    path('gecmis/', views.gecmis_numerolojim, name='gecmis_numerolojim'),
]
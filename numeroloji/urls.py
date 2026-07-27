from django.urls import path
from . import views

urlpatterns = [
    path('', views.numeroloji_formu, name='numeroloji'),
    path('sonuc/<int:id>/', views.sonuc_detay, name='numeroloji_sonuc'),
    path('gecmis/', views.gecmis_numerolojim, name='gecmis_numerolojim'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('burclar/<str:burc_kodu>/', views.burc_detay, name='burc_detay'),
    path('arama/', views.arama, name='arama'),
    path('gunluk-yorumum/', views.gunluk_yorumum, name='gunluk_yorumum'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    # burcs/urls.py
    path('testler/', views.test_listesi, name='test_listesi'),
    path('test/<slug:slug>/', views.test_detay, name='test_detay'),
]
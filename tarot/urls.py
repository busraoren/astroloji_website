from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarot_anasayfa, name='tarot_anasayfa'),
    path('sec/', views.tarot_kartlari_sec, name='tarot_kartlari_sec'),
    path('sonuc/<int:fal_id>/', views.tarot_sonuc, name='tarot_sonuc'),
]
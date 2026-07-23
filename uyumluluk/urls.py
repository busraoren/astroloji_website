from django.urls import path
from . import views

urlpatterns = [
    path('', views.uyumluluk_formu, name='uyumluluk'),
    path('sonuc/<int:sonuc_id>/', views.uyumluluk_sonuc, name='uyumluluk_sonuc'),
]
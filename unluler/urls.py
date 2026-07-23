from django.urls import path
from . import views

urlpatterns = [
    path('', views.unlu_listesi, name='unlu_listesi'),
    path('<int:unlu_id>/uyumluluk/', views.unlu_ile_uyumluluk, name='unlu_uyumluluk'),
]
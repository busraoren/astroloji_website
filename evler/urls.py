from django.urls import path
from . import views

urlpatterns = [
    path('', views.ev_listesi, name='ev_listesi'),
    path('<int:ev_no>/', views.ev_detay, name='ev_detay'),
]
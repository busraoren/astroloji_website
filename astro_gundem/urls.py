from django.urls import path
from . import views

urlpatterns = [
    path('', views.gundem_listesi, name='gundem_listesi'),
    path('<int:gundem_id>/', views.gundem_detay, name='gundem_detay'),
]
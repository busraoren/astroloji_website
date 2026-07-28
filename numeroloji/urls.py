from django.urls import path
from . import views

urlpatterns = [
    path('', views.numeroloji_formu, name='numeroloji'),
    path('sonuc/<int:sonuc_id>/', views.numeroloji_sonuc, name='numeroloji_sonuc'),
    path('gecmis/', views.gecmis_numerolojim, name='gecmis_numerolojim'),
]
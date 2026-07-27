from django.urls import path
from . import views

urlpatterns = [
    path('', views.dogum_haritasi_formu, name='dogum_haritasi'),
    path('gecmis/', views.gecmis_haritalarim, name='gecmis_haritalarim'),
    path('sonuc/<int:harita_id>/', views.dogum_haritasi_sonuc, name='dogum_haritasi_sonuc'),
]
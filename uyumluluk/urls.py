from django.urls import path
from . import views

urlpatterns = [
    path('', views.uyumluluk_formu, name='uyumluluk'),
    path('gecmis/', views.gecmis_uyumluluklarim, name='gecmis_uyumluluklarim'),
    path('sonuc/<int:sonuc_id>/', views.uyumluluk_sonuc, name='uyumluluk_sonuc'),
]
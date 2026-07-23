from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('kayit/', views.kayit_ol, name='kayit'),
    path('giris/', views.giris_yap, name='giris'),
    path('cikis/', views.cikis_yap, name='cikis'),
    path('profil/', views.profil, name='profil'),

path('sifremi-unuttum/',
     auth_views.PasswordResetView.as_view(
         template_name='kullanicilar/sifre_sifirla.html',
         email_template_name='kullanicilar/sifre_sifirla_email.html'
     ),
     name='password_reset'),

    path('sifremi-unuttum/gonderildi/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='kullanicilar/sifre_sifirla_gonderildi.html'
         ),
         name='password_reset_done'),

    path('sifre-yenile/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='kullanicilar/sifre_yenile.html'
         ),
         name='password_reset_confirm'),

    path('sifre-yenile/tamamlandi/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='kullanicilar/sifre_yenile_tamamlandi.html'
         ),
         name='password_reset_complete'),
]
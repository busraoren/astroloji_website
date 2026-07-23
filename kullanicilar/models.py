from django.db import models
from django.contrib.auth.models import User

class KullaniciProfili(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    dogum_tarihi = models.DateField(null=True, blank=True, verbose_name='Doğum Tarihi')
    dogum_saati = models.TimeField(null=True, blank=True, verbose_name='Doğum Saati')
    dogum_yeri = models.CharField(max_length=100, null=True, blank=True, verbose_name='Doğum Yeri')

    def __str__(self):
        return self.user.username
from operator import truediv

from django.db import models
from django.contrib.auth.models import User

class NumerolojiSonucu(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='numeroloji_sonucu' )
    isim = models.CharField(max_length=100)
    dogum_tarihi = models.DateField()
    yasam_yolu_sayisi = models.IntegerField()
    kader_sayisi = models.IntegerField()
    ai_yorumu = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.isim} - {self.dogum_tarihi}"


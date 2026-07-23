from django.db import models
from django.contrib.auth.models import User
import datetime

class UyumlulukTesti(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='uyumluluk_testleri')

    kisi1_isim = models.CharField(max_length=100, default='')
    kisi1_dogum_tarihi = models.DateField(default=datetime.date(2000, 1, 1))
    kisi1_dogum_saati = models.TimeField(default=datetime.time(0, 0))
    kisi1_dogum_yeri = models.CharField(max_length=100, blank=True, default='')

    kisi2_isim = models.CharField(max_length=100, default='')
    kisi2_dogum_tarihi = models.DateField(default=datetime.date(2000, 1, 1))
    kisi2_dogum_saati = models.TimeField(default=datetime.time(0, 0))
    kisi2_dogum_yeri = models.CharField(max_length=100, blank=True, default='')

    kisi1_gezegenler = models.JSONField(default=dict)
    kisi2_gezegenler = models.JSONField(default=dict)
    ai_yorumu = models.TextField(default='')

    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kisi1_isim} & {self.kisi2_isim}"
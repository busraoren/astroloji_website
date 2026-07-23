from django.db import models
from django.contrib.auth.models import User

class DogumHaritasi(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='dogum_haritalari')
    isim = models.CharField(max_length=100, blank=True)
    dogum_tarihi = models.DateField()
    dogum_saati = models.TimeField()
    dogum_yeri = models.CharField(max_length=100, blank=True)
    gezegen_konumlari = models.JSONField()
    ai_yorumu = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.isim or 'Anonim'} - {self.dogum_tarihi}"
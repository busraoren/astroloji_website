from django.db import models
from django.contrib.auth.models import User

class TarotFali(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarot_fallari')
    cekilen_kartlar = models.JSONField()  # [{"isim": "Ölüm", "ters_mi": false}, ...]
    ai_yorumu = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fal - {self.olusturulma_tarihi.strftime('%Y-%m-%d')}"
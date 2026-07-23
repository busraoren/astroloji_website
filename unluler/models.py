from django.db import models

class Unlu(models.Model):
    isim = models.CharField(max_length=100)
    meslek = models.CharField(max_length=100, blank=True)
    dogum_tarihi = models.DateField()
    dogum_saati = models.TimeField(default='12:00')
    dogum_yeri = models.CharField(max_length=100, blank=True)
    gorsel_url = models.URLField(blank=True, help_text="Ünlünün fotoğraf linki (opsiyonel)")

    def __str__(self):
        return self.isim
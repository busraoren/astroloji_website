from django.db import models

class BurcYorumu(models.Model):
    PERIYOT_SECENEKLERI = [
        ('aylik', 'Aylık'),
    ]

    BURC_SECENEKLERI = [
        ('koc', 'Koç'), ('boga', 'Boğa'), ('ikizler', 'İkizler'), ('yengec', 'Yengeç'),
        ('aslan', 'Aslan'), ('basak', 'Başak'), ('terazi', 'Terazi'), ('akrep', 'Akrep'),
        ('yay', 'Yay'), ('oglak', 'Oğlak'), ('kova', 'Kova'), ('balik', 'Balık'),
    ]

    burc = models.CharField(max_length=20, choices=BURC_SECENEKLERI)
    periyot = models.CharField(max_length=10, choices=PERIYOT_SECENEKLERI, default='aylik')
    yil = models.IntegerField()
    ay = models.IntegerField()
    yorum = models.TextField()
    olusturulma_zamani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.burc} - {self.ay}/{self.yil}"

class GunlukYorum(models.Model):
    burc = models.CharField(max_length=20)
    tarih = models.DateField()
    yorum = models.TextField()
    olusturulma_zamani = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('burc', 'tarih')

    def __str__(self):
        return f"{self.burc} - {self.tarih}"
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

# burcs/models.py dosyanın en altına ekle:

class KozmikTest(models.Model):
    baslik = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL'de görünecek isim (Örn: hangi-hayvansin)")
    aciklama = models.TextField()
    ikon = models.CharField(max_length=50, help_text="FontAwesome class (Örn: fa-paw)")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik

class TestSonucu(models.Model):
    test = models.ForeignKey(KozmikTest, related_name='sonuclar', on_delete=models.CASCADE)
    kategori_kodu = models.CharField(max_length=50, help_text="Örn: aslan, lofi, earth_water")
    baslik = models.CharField(max_length=100)
    ikon = models.CharField(max_length=50, help_text="Emoji veya ikon (Örn: 🦁)")
    aciklama = models.TextField()

    def __str__(self):
        return f"{self.test.baslik} - {self.baslik}"

class Soru(models.Model):
    test = models.ForeignKey(KozmikTest, related_name='sorular', on_delete=models.CASCADE)
    sira = models.PositiveIntegerField(default=1)
    metin = models.CharField(max_length=300)
    gorsel_url = models.URLField(blank=True, null=True, help_text="Soru için GIF/Resim linki (Giphy, Imgur vb.)")

    class Meta:
        ordering = ['sira']

    def __str__(self):
        return f"{self.test.baslik} | Soru {self.sira}"

class Secenek(models.Model):
    soru = models.ForeignKey(Soru, related_name='secenekler', on_delete=models.CASCADE)
    metin = models.CharField(max_length=200)
    kategori_kodu = models.CharField(max_length=50, help_text="Bu seçenek hangi sonuca puan verecek?")

    def __str__(self):
        return self.metin
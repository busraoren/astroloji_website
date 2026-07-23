from django.db import models

class AstroGundem(models.Model):
    TUR_SECENEKLERI = [
        ('retro', 'Retro'),
        ('dolunay', 'Dolunay'),
        ('yeniay', 'Yeni Ay'),
        ('burc_gecisi', 'Burç Geçişi'),
        ('tutulma', 'Tutulma'),
        ('diger', 'Diğer'),
    ]

    baslik = models.CharField(max_length=150, help_text="Örn: Merkür Retrosu")
    tur = models.CharField(max_length=20, choices=TUR_SECENEKLERI, default='diger')
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    kisa_aciklama = models.CharField(max_length=200, help_text="Kart üzerinde görünecek kısa özet")
    detay_aciklama = models.TextField(help_text="Bu olayın ne anlama geldiğine dair detaylı açıklama")
    etkilenen_burclar = models.CharField(max_length=200, blank=True, help_text="Opsiyonel, virgülle ayır: Koç, Boğa, İkizler")
    aktif_mi = models.BooleanField(default=True, help_text="Anasayfada gösterilsin mi?")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-baslangic_tarihi']

    def __str__(self):
        return f"{self.baslik} ({self.baslangic_tarihi} - {self.bitis_tarihi})"
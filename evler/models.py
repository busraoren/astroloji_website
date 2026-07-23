from django.db import models
from django.contrib.auth.models import User

class EvYorumu(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ev_yorumlari')
    ev_no = models.IntegerField()
    burc = models.CharField(max_length=20)
    dogum_tarihi = models.DateField()
    dogum_saati = models.TimeField()
    ai_yorumu = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('kullanici', 'ev_no', 'dogum_tarihi', 'dogum_saati')

    def __str__(self):
        return f"{self.kullanici.username} - {self.ev_no}. Ev"

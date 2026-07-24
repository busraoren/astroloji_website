from django.shortcuts import render
from django.utils import timezone
from .models import BurcYorumu
from astro_gundem.views import anasayfa_icin_aktif_gundem
from .burc_bilgileri import BURC_BILGILERI
from .ai_yardimcisi import burc_yorumu_uret

AY_ISIMLERI = ['', 'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
               'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']


def anasayfa(request):
    burc_listesi = BurcYorumu.BURC_SECENEKLERI
    burclar = []
    for burc_kodu, burc_adi in burc_listesi:
        burclar.append({
            'kodu': burc_kodu,
            'ad': burc_adi,
            'sembol': BURC_BILGILERI[burc_kodu]['sembol'],
        })

    aktif_gundem = anasayfa_icin_aktif_gundem()

    return render(request, 'burcs/anasayfa.html', {'burclar': burclar, 'aktif_gundem': aktif_gundem})

def burc_detay(request, burc_kodu):
    burc_adi = dict(BurcYorumu.BURC_SECENEKLERI)[burc_kodu]
    bilgi = BURC_BILGILERI[burc_kodu]

    simdi = timezone.now()
    yil, ay = simdi.year, simdi.month
    ay_adi = AY_ISIMLERI[ay]

    yorum_kaydi = BurcYorumu.objects.filter(burc=burc_kodu, yil=yil, ay=ay).first()
    if not yorum_kaydi:
        yorum_metni = burc_yorumu_uret(burc_adi, ay_adi)
        yorum_kaydi = BurcYorumu.objects.create(burc=burc_kodu, yil=yil, ay=ay, yorum=yorum_metni)

    return render(request, 'burcs/detay.html', {
        'burc_kodu': burc_kodu,
        'burc_adi': burc_adi,
        'bilgi': bilgi,
        'yorum': yorum_kaydi.yorum,
        'ay_adi': ay_adi,
    })
def test_detay(request):
    return render(request, 'test_detay.html')
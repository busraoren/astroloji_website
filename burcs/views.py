from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import BurcYorumu
from .burc_bilgileri import BURC_BILGILERI
from .ai_yardimcisi import burc_yorumu_uret
from unluler.models import Unlu
from astro_gundem.views import anasayfa_icin_aktif_gundem
import datetime
from .motivasyon_sozleri import MOTIVASYON_SOZLERI
from .ay_fazi import ay_fazini_hesapla

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
    gun_no = datetime.date.today().timetuple().tm_yday  # yılın kaçıncı günü
    gunun_sozu = MOTIVASYON_SOZLERI[gun_no % len(MOTIVASYON_SOZLERI)]
    ay_fazi = ay_fazini_hesapla()

    return render(request, 'burcs/anasayfa.html',
                  {'burclar': burclar, 'aktif_gundem': aktif_gundem,'ay_fazi': ay_fazi, 'gunun_sozu': gunun_sozu})
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
    # 'burcs/' takısını ekliyoruz çünkü HTML dosyan o klasörün içinde
    return render(request, 'burcs/test_detay.html')

def arama(request):
    query = request.GET.get('q', '').strip()

    burc_sonuclari = []
    unlu_sonuclari = []
    kullanici_sonuclari = []

    if query:
        for kod, ad in BurcYorumu.BURC_SECENEKLERI:
            if query.lower() in ad.lower():
                burc_sonuclari.append({'kodu': kod, 'ad': ad, 'sembol': BURC_BILGILERI[kod]['sembol']})

        unlu_sonuclari = Unlu.objects.filter(isim__icontains=query)[:10]
        kullanici_sonuclari = User.objects.filter(username__icontains=query)[:10]

    return render(request, 'burcs/arama_sonuc.html', {
        'query': query,
        'burc_sonuclari': burc_sonuclari,
        'unlu_sonuclari': unlu_sonuclari,
        'kullanici_sonuclari': kullanici_sonuclari,
    })
import json
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

# Modüllerimiz
from .models import BurcYorumu, GunlukYorum, KozmikTest
from .burc_bilgileri import BURC_BILGILERI
from .ai_yardimcisi import burc_yorumu_uret
from .burc_hesapla import dogum_tarihinden_burc_bul
from unluler.models import Unlu
from astro_gundem.views import anasayfa_icin_aktif_gundem

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
    # YENİ: Anasayfaya en son eklenen 4 testi yolluyoruz
    vitrin_testleri = KozmikTest.objects.all().order_by('-olusturulma_tarihi')[:4]

    return render(request, 'burcs/anasayfa.html', {
        'burclar': burclar,
        'aktif_gundem': aktif_gundem,
        'vitrin_testleri': vitrin_testleri
    })

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

@login_required
def gunluk_yorumum(request):
    profil = request.user.profil
    if not profil.dogum_tarihi:
        return render(request, 'burcs/gunluk_eksik.html')

    burc_kodu = dogum_tarihinden_burc_bul(profil.dogum_tarihi)
    burc_adi = dict(BurcYorumu.BURC_SECENEKLERI)[burc_kodu]
    bugun = timezone.localdate()

    yorum_kaydi = GunlukYorum.objects.filter(burc=burc_kodu, tarih=bugun).first()
    if not yorum_kaydi:
        yorum_metni = burc_yorumu_uret(burc_adi, "bugün")
        yorum_kaydi = GunlukYorum.objects.create(burc=burc_kodu, tarih=bugun, yorum=yorum_metni)

    return render(request, 'burcs/gunluk_yorumum.html', {
        'burc_adi': burc_adi,
        'bilgi': BURC_BILGILERI[burc_kodu],
        'yorum': yorum_kaydi.yorum,
        'tarih': bugun,
    })

def oyunlar(request):
    return render(request, 'burcs/oyunlar.html')

# YENİ: Tüm Testler Sayfası
def test_listesi(request):
    tum_testler = KozmikTest.objects.all().order_by('-olusturulma_tarihi')
    return render(request, 'burcs/test_listesi.html', {'tum_testler': tum_testler})

# YENİ: Dinamik Test Detay Sayfası
def test_detay(request, slug):
    test_obj = get_object_or_404(KozmikTest, slug=slug)

    # Veritabanındaki veriyi Javascript'in sevdiği JSON formatına otomatik çeviriyoruz
    test_data = {
        "title": test_obj.baslik,
        "desc": test_obj.aciklama,
        "icon": f"<i class='fas {test_obj.ikon}'></i>",
        "questions": [],
        "results": {}
    }

    for soru in test_obj.sorular.all():
        soru_data = {
            "text": soru.metin,
            "gorsel_url": soru.gorsel_url, # GIF linkimiz burada!
            "options": [{"text": sec.metin, "category": sec.kategori_kodu} for sec in soru.secenekler.all()]
        }
        test_data["questions"].append(soru_data)

    for sonuc in test_obj.sonuclar.all():
        test_data["results"][sonuc.kategori_kodu] = {
            "title": sonuc.baslik,
            "icon": sonuc.ikon,
            "desc": sonuc.aciklama
        }

    context = {
        'test_json': json.dumps(test_data),
        'test_obj': test_obj
    }
    return render(request, 'burcs/test_detay.html', context)
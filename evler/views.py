from django.shortcuts import render
from .ev_bilgileri import EV_BILGILERI
from .ai_yorumcu import ev_yorumla
from .models import EvYorumu
from dogum_haritasi.hesaplama import gezegen_konumlarini_hesapla


def ev_listesi(request):
    return render(request, 'evler/liste.html', {'evler': EV_BILGILERI})


def ev_detay(request, ev_no):
    bilgi = EV_BILGILERI[ev_no]

    kullanici_burcu = None
    kisisel_yorum = None

    # Kullanıcının giriş yapıp yapmadığını VE bir profili olup olmadığını güvenli bir şekilde kontrol ediyoruz
    if request.user.is_authenticated and hasattr(request.user, 'profil'):
        profil = request.user.profil
        if profil.dogum_tarihi and profil.dogum_saati:
            hesaplama_sonucu = gezegen_konumlarini_hesapla(
                profil.dogum_tarihi, profil.dogum_saati, profil.dogum_yeri
            )
            evler = hesaplama_sonucu.get('evler')
            if evler and ev_no in evler:
                kullanici_burcu = evler[ev_no]['burc']

                mevcut_yorum = EvYorumu.objects.filter(
                    kullanici=request.user, ev_no=ev_no,
                    dogum_tarihi=profil.dogum_tarihi, dogum_saati=profil.dogum_saati
                ).first()

                if not mevcut_yorum:
                    yorum_metni = ev_yorumla(ev_no, bilgi['anahtar_kelime'], kullanici_burcu)
                    mevcut_yorum = EvYorumu.objects.create(
                        kullanici=request.user, ev_no=ev_no, burc=kullanici_burcu,
                        dogum_tarihi=profil.dogum_tarihi, dogum_saati=profil.dogum_saati,
                        ai_yorumu=yorum_metni
                    )
                kisisel_yorum = mevcut_yorum.ai_yorumu

    return render(request, 'evler/detay.html', {
        'ev_no': ev_no,
        'bilgi': bilgi,
        'kullanici_burcu': kullanici_burcu,
        'kisisel_yorum': kisisel_yorum,
    })
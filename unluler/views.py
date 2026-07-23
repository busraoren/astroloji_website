from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dogum_haritasi.hesaplama import gezegen_konumlarini_hesapla
from uyumluluk.ai_yorumcu import uyumluluk_yorumla
from uyumluluk.models import UyumlulukTesti
from .models import Unlu
from django.contrib.auth.decorators import login_required


def unlu_listesi(request):
    unluler = Unlu.objects.all()
    return render(request, 'unluler/liste.html', {'unluler': unluler})


@login_required
def unlu_ile_uyumluluk(request, unlu_id):
    profil = request.user.profil
    if not profil.dogum_tarihi or not profil.dogum_saati:
        return render(request, 'unluler/eksik_bilgi.html')

    unlu = Unlu.objects.get(id=unlu_id)

    kisi1_gezegenler = gezegen_konumlarini_hesapla(
        profil.dogum_tarihi, profil.dogum_saati, profil.dogum_yeri
    )
    kisi2_gezegenler = gezegen_konumlarini_hesapla(
        unlu.dogum_tarihi, unlu.dogum_saati, unlu.dogum_yeri
    )

    yorum = uyumluluk_yorumla(
        request.user.username, kisi1_gezegenler,
        unlu.isim, kisi2_gezegenler
    )

    sonuc = UyumlulukTesti.objects.create(
        kullanici=request.user,
        kisi1_isim=request.user.username,
        kisi1_dogum_tarihi=profil.dogum_tarihi,
        kisi1_dogum_saati=profil.dogum_saati,
        kisi1_dogum_yeri=profil.dogum_yeri or '',
        kisi2_isim=unlu.isim,
        kisi2_dogum_tarihi=unlu.dogum_tarihi,
        kisi2_dogum_saati=unlu.dogum_saati,
        kisi2_dogum_yeri=unlu.dogum_yeri or '',
        kisi1_gezegenler=kisi1_gezegenler,
        kisi2_gezegenler=kisi2_gezegenler,
        ai_yorumu=yorum
    )

    return redirect('uyumluluk_sonuc', sonuc_id=sonuc.id)
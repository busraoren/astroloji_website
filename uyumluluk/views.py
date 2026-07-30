import markdown
from django.shortcuts import render, redirect
from dogum_haritasi.hesaplama import gezegen_konumlarini_hesapla
from .forms import UyumlulukFormu
from .ai_yorumcu import uyumluluk_yorumla
from .models import UyumlulukTesti


def uyumluluk_formu(request):
    if request.method == 'POST':
        form = UyumlulukFormu(request.POST)
        if form.is_valid():
            veri = form.cleaned_data

            kisi1_gezegenler = gezegen_konumlarini_hesapla(
                veri['kisi1_dogum_tarihi'], veri['kisi1_dogum_saati'], veri['kisi1_dogum_yeri']
            )
            kisi2_gezegenler = gezegen_konumlarini_hesapla(
                veri['kisi2_dogum_tarihi'], veri['kisi2_dogum_saati'], veri['kisi2_dogum_yeri']
            )

            yorum = uyumluluk_yorumla(
                veri['kisi1_isim'], kisi1_gezegenler,
                veri['kisi2_isim'], kisi2_gezegenler
            )

            kullanici = request.user if request.user.is_authenticated else None

            sonuc = UyumlulukTesti.objects.create(
                kullanici=kullanici,
                kisi1_isim=veri['kisi1_isim'],
                kisi1_dogum_tarihi=veri['kisi1_dogum_tarihi'],
                kisi1_dogum_saati=veri['kisi1_dogum_saati'],
                kisi1_dogum_yeri=veri['kisi1_dogum_yeri'],
                kisi2_isim=veri['kisi2_isim'],
                kisi2_dogum_tarihi=veri['kisi2_dogum_tarihi'],
                kisi2_dogum_saati=veri['kisi2_dogum_saati'],
                kisi2_dogum_yeri=veri['kisi2_dogum_yeri'],
                kisi1_gezegenler=kisi1_gezegenler,
                kisi2_gezegenler=kisi2_gezegenler,
                ai_yorumu=yorum
            )
            return redirect('uyumluluk_sonuc', sonuc_id=sonuc.id)
    else:
        form = UyumlulukFormu()

    return render(request, 'uyumluluk/form.html', {'form': form})


def uyumluluk_sonuc(request, sonuc_id):
    sonuc = UyumlulukTesti.objects.get(id=sonuc_id)
    yorum_html = markdown.markdown(sonuc.ai_yorumu)
    return render(request, 'uyumluluk/sonuc.html', {'sonuc': sonuc, 'yorum_html': yorum_html})
from django.contrib.auth.decorators import login_required

@login_required
def gecmis_uyumluluklarim(request):
    testler = UyumlulukTesti.objects.filter(kullanici=request.user).order_by('-olusturulma_tarihi')
    return render(request, 'uyumluluk/gecmis.html', {'testler': testler})

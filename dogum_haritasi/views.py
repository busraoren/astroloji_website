import markdown
from django.shortcuts import render, redirect
from .hesaplama import gezegen_konumlarini_hesapla
from .ai_yorumcu import dogum_haritasi_yorumla
from .forms import DogumHaritasiFormu
from .models import DogumHaritasi


def dogum_haritasi_formu(request):
    if request.user.is_authenticated:
        mevcut = DogumHaritasi.objects.filter(kullanici=request.user).order_by('-olusturulma_tarihi').first()
        if mevcut:
            return redirect('dogum_haritasi_sonuc', harita_id=mevcut.id)

    if request.method == 'POST':
        form = DogumHaritasiFormu(request.POST)
        if form.is_valid():
            veri = form.cleaned_data

            hesaplama_sonucu = gezegen_konumlarini_hesapla(
                veri['dogum_tarihi'], veri['dogum_saati'], veri['dogum_yeri']
            )
            yorum = dogum_haritasi_yorumla(hesaplama_sonucu)

            kullanici = request.user if request.user.is_authenticated else None

            harita = DogumHaritasi.objects.create(
                kullanici=kullanici,
                isim=veri['isim'],
                dogum_tarihi=veri['dogum_tarihi'],
                dogum_saati=veri['dogum_saati'],
                dogum_yeri=veri['dogum_yeri'],
                gezegen_konumlari=hesaplama_sonucu,
                ai_yorumu=yorum
            )
            return redirect('dogum_haritasi_sonuc', harita_id=harita.id)
    else:
        form = DogumHaritasiFormu()

    return render(request, 'dogum_haritasi/form.html', {'form': form})


def dogum_haritasi_sonuc(request, harita_id):
    harita = DogumHaritasi.objects.get(id=harita_id)
    yorum_html = markdown.markdown(harita.ai_yorumu)
    return render(request, 'dogum_haritasi/sonuc.html', {'harita': harita, 'yorum_html': yorum_html})
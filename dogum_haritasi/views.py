import markdown
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .hesaplama import gezegen_konumlarini_hesapla
from .ai_yorumcu import dogum_haritasi_yorumla
from .forms import DogumHaritasiFormu
from .models import DogumHaritasi


def dogum_haritasi_formu(request):
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
    harita = get_object_or_404(DogumHaritasi, id=harita_id)
    yorum_html = markdown.markdown(harita.ai_yorumu)
    return render(request, 'dogum_haritasi/sonuc.html', {'harita': harita, 'yorum_html': yorum_html})


@login_required
def gecmis_haritalarim(request):
    haritalar = DogumHaritasi.objects.filter(kullanici=request.user).order_by('-olusturulma_tarihi')
    return render(request, 'dogum_haritasi/gecmis.html', {'haritalar': haritalar})
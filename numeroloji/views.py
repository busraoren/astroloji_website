import markdown
from django.shortcuts import render, redirect
from .hesaplama import numeroloji_hesapla
from .ai_yorumcu import numeroloji_yorumla
from .forms import NumerolojiFormu
from .models import NumerolojiSonucu


def numeroloji_formu(request):
    if request.method == 'POST':
        form = NumerolojiFormu(request.POST)
        if form.is_valid():
            veri = form.cleaned_data

            hesaplama_sonucu = numeroloji_hesapla(veri['isim'], veri['dogum_tarihi'])
            yorum = numeroloji_yorumla(veri['isim'], hesaplama_sonucu)

            kullanici = request.user if request.user.is_authenticated else None

            sonuc = NumerolojiSonucu.objects.create(
                kullanici=kullanici,
                isim=veri['isim'],
                dogum_tarihi=veri['dogum_tarihi'],
                yasam_yolu_sayisi=hesaplama_sonucu['yasam_yolu_sayisi'],
                kader_sayisi=hesaplama_sonucu['kader_sayisi'],
                ai_yorumu=yorum
            )
            return redirect('numeroloji_sonuc', sonuc_id=sonuc.id)
    else:
        form = NumerolojiFormu()

    return render(request, 'numeroloji/form.html', {'form': form})


def numeroloji_sonuc(request, sonuc_id):
    sonuc = NumerolojiSonucu.objects.get(id=sonuc_id)
    yorum_html = markdown.markdown(sonuc.ai_yorumu)
    return render(request, 'numeroloji/sonuc.html', {'sonuc': sonuc, 'yorum_html': yorum_html})
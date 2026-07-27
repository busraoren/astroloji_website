import markdown
from django.shortcuts import render
from .hesaplama import numeroloji_hesapla
from .ai_yorumcu import numeroloji_yorumla
from .forms import NumerolojiFormu
from .models import NumerolojiSonucu


def numeroloji_formu(request):
    # Eğer sayfada form gönderildiyse (Hesapla butonuna basıldıysa)
    if request.method == 'POST':
        form = NumerolojiFormu(request.POST)
        if form.is_valid():
            veri = form.cleaned_data

            hesaplama_sonucu = numeroloji_hesapla(veri['isim'], veri['dogum_tarihi'])
            yorum = numeroloji_yorumla(veri['isim'], hesaplama_sonucu)
            yorum_html = markdown.markdown(yorum)  # Markdown'ı HTML'e çevirdik

            kullanici = request.user if request.user.is_authenticated else None

            sonuc = NumerolojiSonucu.objects.create(
                kullanici=kullanici,
                isim=veri['isim'],
                dogum_tarihi=veri['dogum_tarihi'],
                yasam_yolu_sayisi=hesaplama_sonucu['yasam_yolu_sayisi'],
                kader_sayisi=hesaplama_sonucu['kader_sayisi'],
                ai_yorumu=yorum
            )

            # DİKKAT: Yönlendirme (redirect) yapmıyoruz!
            # Formu, sonucu ve yorumu aynı anda aynı sayfaya gönderiyoruz.
            return render(request, 'numeroloji/form.html', {
                'form': form,
                'sonuc': sonuc,
                'yorum_html': yorum_html
            })

    # Eğer sayfaya ilk defa giriliyorsa boş formu göster
    else:
        form = NumerolojiFormu()

    # Sayfa ilk açıldığında sadece formu gönder (sonuç daha yok)
    return render(request, 'numeroloji/form.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def gecmis_numerolojim(request):
    sonuclar = NumerolojiSonucu.objects.filter(kullanici=request.user).order_by('-olusturulma_tarihi')
    return render(request, 'numeroloji/gecmis.html', {'sonuclar': sonuclar})
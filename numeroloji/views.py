import markdown
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .hesaplama import numeroloji_hesapla
from .ai_yorumcu import numeroloji_yorumla
from .models import NumerolojiSonucu

# Form sınıfını projene dahil etmelisin (Adının NumerolojiFormu olduğunu varsayıyorum)
from .forms import NumerolojiFormu


def numeroloji_formu(request):
    if request.method == 'POST':
        # DİKKAT: Görünümün (view) kendi adını değil, Form sınıfının adını kullanmalısın!
        form = NumerolojiFormu(request.POST)
        if form.is_valid():
            veri = form.cleaned_data

            hesaplama_sonucu = numeroloji_hesapla(veri['isim'], veri['dogum_tarihi'])
            yorum = numeroloji_yorumla(veri['isim'], hesaplama_sonucu)
            yorum_html = markdown.markdown(yorum)

            kullanici = request.user if request.user.is_authenticated else None

            sonuc = NumerolojiSonucu.objects.create(
                kullanici=kullanici,
                isim=veri['isim'],
                dogum_tarihi=veri['dogum_tarihi'],
                yasam_yolu_sayisi=hesaplama_sonucu['yasam_yolu_sayisi'],
                kader_sayisi=hesaplama_sonucu['kader_sayisi'],
                ai_yorumu=yorum
            )

            return render(request, 'numeroloji/form.html', {
                'form': form,
                'sonuc': sonuc,
                'yorum_html': yorum_html
            })

    else:
        # DİKKAT: Burada da Form sınıfını çağırmalısın
        form = NumerolojiFormu()

    return render(request, 'numeroloji/form.html', {'form': form})


@login_required
def gecmis_numerolojim(request):
    sonuclar = NumerolojiSonucu.objects.filter(kullanici=request.user).order_by('-olusturulma_tarihi')
    return render(request, 'numeroloji/gecmis.html', {'sonuclar': sonuclar})


# --- İŞTE EKSİK OLAN VE ÇÖKMEYE SEBEP OLAN YENİ FONKSİYON ---
def numeroloji_sonuc(request, sonuc_id):
    # Veritabanından o ID'ye ait sonucu bul, yoksa 404 hatası ver
    sonuc = get_object_or_404(NumerolojiSonucu, id=sonuc_id)

    # AI yorumunu tekrar HTML formatına çevir
    yorum_html = markdown.markdown(sonuc.ai_yorumu)

    # Detayları göstereceğin tasarım sayfasını render et (form.html veya detay.html)
    return render(request, 'numeroloji/form.html', {
        'sonuc': sonuc,
        'yorum_html': yorum_html
    })
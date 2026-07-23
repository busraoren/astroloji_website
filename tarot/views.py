import markdown
from django.shortcuts import render, redirect
from .kart_verileri import TAROT_DESTESI
from .kart_gorselleri import kart_gorsel_yolu
from .ai_yorumcu import tarot_yorumla
from .models import TarotFali
import random


def tarot_anasayfa(request):
    karisik_deste = TAROT_DESTESI.copy()
    random.shuffle(karisik_deste)

    deste_durumu = []
    for kart_ismi in karisik_deste:
        deste_durumu.append({
            'isim': kart_ismi,
            'ters_mi': False
        })

    request.session['tarot_destesi'] = deste_durumu

    return render(request, 'tarot/anasayfa.html', {
        'kart_sayisi': range(len(deste_durumu))
    })


def tarot_kartlari_sec(request):
    if request.method == 'POST':
        secilen_pozisyonlar = request.POST.getlist('pozisyon')

        deste = request.session.get('tarot_destesi')
        if not deste or len(secilen_pozisyonlar) != 3:
            return redirect('tarot_anasayfa')

        cekilen_kartlar = [deste[int(pozisyon)] for pozisyon in secilen_pozisyonlar]

        yorum = tarot_yorumla(cekilen_kartlar)

        kullanici = request.user if request.user.is_authenticated else None
        fal = TarotFali.objects.create(
            kullanici=kullanici,
            cekilen_kartlar=cekilen_kartlar,
            ai_yorumu=yorum
        )

        return redirect('tarot_sonuc', fal_id=fal.id)

    return redirect('tarot_anasayfa')


def tarot_sonuc(request, fal_id):
    fal = TarotFali.objects.get(id=fal_id)
    yorum_html = markdown.markdown(fal.ai_yorumu)

    # Her çekilen karta görsel yolu ekleyelim
    kartlar_gorsel_ile = []
    for kart in fal.cekilen_kartlar:
        kartlar_gorsel_ile.append({
            'isim': kart['isim'],
            'ters_mi': kart['ters_mi'],
            'gorsel': kart_gorsel_yolu(kart['isim'])
        })

    return render(request, 'tarot/sonuc.html', {
        'fal': fal,
        'yorum_html': yorum_html,
        'kartlar': kartlar_gorsel_ile
    })
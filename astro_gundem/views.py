from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import AstroGundem


def gundem_listesi(request):
    bugun = timezone.localdate()
    aktif_olaylar = AstroGundem.objects.filter(
        aktif_mi=True, baslangic_tarihi__lte=bugun, bitis_tarihi__gte=bugun
    )
    yaklasan_olaylar = AstroGundem.objects.filter(
        aktif_mi=True, baslangic_tarihi__gt=bugun
    )
    gecmis_olaylar = AstroGundem.objects.filter(
        aktif_mi=True, bitis_tarihi__lt=bugun
    )
    return render(request, 'astro_gundem/liste.html', {
        'aktif_olaylar': aktif_olaylar,
        'yaklasan_olaylar': yaklasan_olaylar,
        'gecmis_olaylar': gecmis_olaylar,
    })


def gundem_detay(request, gundem_id):
    olay = get_object_or_404(AstroGundem, id=gundem_id)
    return render(request, 'astro_gundem/detay.html', {'olay': olay})


def anasayfa_icin_aktif_gundem():
    """Anasayfada göstermek için, şu an aktif olan ilk gündemi döndürür."""
    bugun = timezone.localdate()
    return AstroGundem.objects.filter(
        aktif_mi=True, baslangic_tarihi__lte=bugun, bitis_tarihi__gte=bugun
    ).first()
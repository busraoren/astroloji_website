# Dosyanın en üstüne bunu eklemeyi unutma
from django.core.exceptions import ObjectDoesNotExist


# Mevcut profil görünümünü şu mantıkla güncelle:
def profil(request):
    # Kullanıcının profili var mı diye dene (try), yoksa (except) yeni oluştur!
    try:
        kullanici_profili = request.user.profil
    except ObjectDoesNotExist:
        # Profil modeli adın neyse onu kullan (Profil, UserProfile vb.)
        kullanici_profili = Profil.objects.create(user=request.user)

    # ... fonksiyonun geri kalan kodları ...
    context = {
        'profil': kullanici_profili
    }
    return render(request, 'kullanicilar/profil.html', context)
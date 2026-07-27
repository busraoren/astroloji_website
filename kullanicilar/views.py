from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# DİKKAT: Profil modelinin adı farklıysa (örneğin UserProfile), aşağıdaki 'Profil' yazan yerleri değiştirmelisin.
from .models import KullaniciProfili


@login_required
def profil(request):
    # Kullanıcının profili varsa alır, yoksa veritabanında anında boş bir tane oluşturur.
    # Sayfanın "Profil yok" diyerek çökmesini kökten çözer.
    kullanici_profili, created = KullaniciProfili.objects.get_or_create(user=request.user)

    context = {
        'profil': kullanici_profili
    }
    return render(request, 'kullanicilar/profil.html', context)
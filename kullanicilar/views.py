from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import KayitFormu, ProfilFormu
from .models import KullaniciProfili

def kayit_ol(request):
    if request.method == 'POST':
        form = KayitFormu(request.POST)
        if form.is_valid():
            user = form.save()
            KullaniciProfili.objects.get_or_create(user=user)
            login(request, user)
            return redirect('anasayfa')
        # form geçersizse (örn. kullanıcı adı alınmışsa) buraya düşer,
        # hatalar otomatik olarak form içinde kullanıcıya gösterilir
    else:
        form = KayitFormu()
    return render(request, 'kullanicilar/kayit.html', {'form': form})


def giris_yap(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('anasayfa')
        else:
            return render(request, 'kullanicilar/giris.html', {'hata': 'Kullanıcı adı veya şifre yanlış'})
    return render(request, 'kullanicilar/giris.html')


def cikis_yap(request):
    logout(request)
    return redirect('anasayfa')


@login_required
def profil(request):
    profil = request.user.profil
    if request.method == 'POST':
        form = ProfilFormu(request.POST, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = ProfilFormu(instance=profil)
    return render(request, 'kullanicilar/profil.html', {'form': form})

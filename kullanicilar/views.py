from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import KullaniciProfili


# --- KAYIT OLMA İŞLEMİ ---
def kayit_ol(request):
    if request.method == 'POST':
        # Eğer senin yazdığın özel bir kayıt formun varsa
        # UserCreationForm yerine kendi formunun adını (örn: KayitFormu) yazabilirsin.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Kullanıcı kayıt olduğu an boş bir profil de sisteme eklenir
            KullaniciProfili.objects.get_or_create(user=user)
            login(request, user)
            return redirect('anasayfa')  # Kayıt sonrası gideceği sayfa
    else:
        form = UserCreationForm()

    return render(request, 'kullanicilar/kayit.html', {'form': form})


# --- GİRİŞ YAPMA İŞLEMİ ---
def giris_yap(request):
    # Eğer urls.py dosyasında bu yolun adı sadece 'giris' ise
    # fonksiyonun adını def giris(request): olarak değiştirebilirsin.
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('anasayfa')
    else:
        form = AuthenticationForm()

    return render(request, 'kullanicilar/giris.html', {'form': form})


# --- ÇIKIŞ YAPMA İŞLEMİ ---
def cikis_yap(request):
    logout(request)
    return redirect('anasayfa')


# --- PROFİL GÖRÜNTÜLEME İŞLEMİ (DÜZELTİLDİ) ---
@login_required
def profil(request):
    # Kullanıcının profili varsa getirir, yoksa anında boş bir tane oluşturur.
    # RelatedObjectDoesNotExist hatasını kökten çözer.
    kullanici_profili, created = KullaniciProfili.objects.get_or_create(user=request.user)

    context = {
        'profil': kullanici_profili
    }
    return render(request, 'kullanicilar/profil.html', context)
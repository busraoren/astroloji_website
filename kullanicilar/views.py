from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import KullaniciProfili

# KENDİ YAZDIĞIN FORMLARI İÇERİ AKTARIYORSUN
from .forms import KayitFormu, ProfilFormu

# --- KAYIT OLMA İŞLEMİ ---
def kayit_ol(request):
    if request.method == 'POST':
        # Senin hazırladığın Tailwind tasarımlı özel formu kullanıyoruz
        form = KayitFormu(request.POST)
        if form.is_valid():
            user = form.save()
            KullaniciProfili.objects.get_or_create(user=user)
            login(request, user)
            return redirect('anasayfa')
    else:
        form = KayitFormu()

    return render(request, 'kullanicilar/kayit.html', {'form': form})


# --- GİRİŞ YAPMA İŞLEMİ ---
def giris_yap(request):
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


# --- PROFİL GÖRÜNTÜLEME VE GÜNCELLEME İŞLEMİ ---
@login_required
def profil(request):
    # 1. Kullanıcının profilini bul veya anında oluştur
    kullanici_profili, created = KullaniciProfili.objects.get_or_create(user=request.user)

    # 2. Form gönderildiyse (Bilgilerimi Güncelle butonuna basıldıysa)
    if request.method == 'POST':
        form = ProfilFormu(request.POST, instance=kullanici_profili)
        if form.is_valid():
            form.save()
            return redirect('profil') # Başarıyla kaydedince sayfayı yenile
    else:
        # 3. Sayfaya ilk girildiğinde formu mevcut bilgilerle doldur
        form = ProfilFormu(instance=kullanici_profili)

    # 4. Formu HTML sayfasına (template) gönder! (Kutucukların görünmesini sağlayan asıl yer)
    context = {
        'profil': kullanici_profili,
        'form': form
    }
    return render(request, 'kullanicilar/profil.html', context)
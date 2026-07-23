# Pisagor numeroloji harf-sayı tablosu (Türkçe karakterler İngilizce karşılıklarına çevrilir)
HARF_DEGERLERI = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8,
}

TURKCE_KARAKTER_DONUSUM = {
    'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
}

USTAT_SAYILAR = [11, 22, 33]  # Master numbers - indirgenmez


def tek_haneye_indirge(sayi):
    """Bir sayıyı, usta sayı değilse tek haneye indirger."""
    while sayi > 9 and sayi not in USTAT_SAYILAR:
        sayi = sum(int(rakam) for rakam in str(sayi))
    return sayi


def yasam_yolu_sayisi_hesapla(dogum_tarihi):
    """Doğum tarihindeki tüm rakamları toplar."""
    tarih_str = dogum_tarihi.strftime('%d%m%Y')
    toplam = sum(int(rakam) for rakam in tarih_str)
    return tek_haneye_indirge(toplam)


def isim_normallestir(isim):
    """Türkçe karakterleri İngilizce karşılıklarına çevirir, büyük harfe çevirir."""
    isim = isim.upper()
    for tr_karakter, en_karakter in TURKCE_KARAKTER_DONUSUM.items():
        isim = isim.replace(tr_karakter, en_karakter)
    return isim


def kader_sayisi_hesapla(isim):
    """İsimdeki harflerin sayısal değerlerini toplar."""
    isim = isim_normallestir(isim)
    toplam = 0
    for harf in isim:
        if harf in HARF_DEGERLERI:
            toplam += HARF_DEGERLERI[harf]
    return tek_haneye_indirge(toplam)


def numeroloji_hesapla(isim, dogum_tarihi):
    return {
        'yasam_yolu_sayisi': yasam_yolu_sayisi_hesapla(dogum_tarihi),
        'kader_sayisi': kader_sayisi_hesapla(isim),
    }
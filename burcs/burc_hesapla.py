def dogum_tarihinden_burc_bul(dogum_tarihi):
    ay, gun = dogum_tarihi.month, dogum_tarihi.day
    if (ay == 3 and gun >= 21) or (ay == 4 and gun <= 19): return 'koc'
    if (ay == 4 and gun >= 20) or (ay == 5 and gun <= 20): return 'boga'
    if (ay == 5 and gun >= 21) or (ay == 6 and gun <= 20): return 'ikizler'
    if (ay == 6 and gun >= 21) or (ay == 7 and gun <= 22): return 'yengec'
    if (ay == 7 and gun >= 23) or (ay == 8 and gun <= 22): return 'aslan'
    if (ay == 8 and gun >= 23) or (ay == 9 and gun <= 22): return 'basak'
    if (ay == 9 and gun >= 23) or (ay == 10 and gun <= 22): return 'terazi'
    if (ay == 10 and gun >= 23) or (ay == 11 and gun <= 21): return 'akrep'
    if (ay == 11 and gun >= 22) or (ay == 12 and gun <= 21): return 'yay'
    if (ay == 12 and gun >= 22) or (ay == 1 and gun <= 19): return 'oglak'
    if (ay == 1 and gun >= 20) or (ay == 2 and gun <= 18): return 'kova'
    return 'balik'
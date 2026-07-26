import swisseph as swe
from datetime import datetime, timezone

FAZ_ISIMLERI = [
    (0, 1.84566, "Yeni Ay", "🌑"),
    (1.84566, 5.53699, "Hilal", "🌒"),
    (5.53699, 9.22831, "İlk Dördün", "🌓"),
    (9.22831, 12.91963, "Büyüyen Ay", "🌔"),
    (12.91963, 16.61096, "Dolunay", "🌕"),
    (16.61096, 20.30228, "Küçülen Ay" , "🌖"),
    (20.30228, 23.99361, "Son Dördün", "🌗"),
    (23.99361, 27.68493, "Hilal", "🌘"),
    (27.68493, 29.53059, "Yeni Ay", "🌑"),
]


def ay_fazini_hesapla():
    simdi = datetime.now(timezone.utc)
    jd = swe.julday(simdi.year, simdi.month, simdi.day, simdi.hour + simdi.minute / 60)

    gunes_konum, _ = swe.calc_ut(jd, swe.SUN)
    ay_konum, _ = swe.calc_ut(jd, swe.MOON)

    aci_farki = (ay_konum[0] - gunes_konum[0]) % 360
    ay_gunu = aci_farki / 360 * 29.53059  # sinodik ay döngüsü ~29.53 gün

    for min_gun, max_gun, isim, emoji in FAZ_ISIMLERI:
        if min_gun <= ay_gunu < max_gun:
            return {'isim': isim, 'emoji': emoji, 'yuzde': round(aci_farki / 360 * 100)}

    return {'isim': 'Yeni Ay', 'emoji': '🌑', 'yuzde': 0}
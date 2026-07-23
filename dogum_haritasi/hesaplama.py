import swisseph as swe
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

GEZEGENLER = {
    'Güneş': swe.SUN,
    'Ay': swe.MOON,
    'Merkür': swe.MERCURY,
    'Venüs': swe.VENUS,
    'Mars': swe.MARS,
    'Jüpiter': swe.JUPITER,
    'Satürn': swe.SATURN,
    'Uranüs': swe.URANUS,
    'Neptün': swe.NEPTUNE,
    'Plüton': swe.PLUTO,
}

BURCLAR = [
    'Koç', 'Boğa', 'İkizler', 'Yengeç', 'Aslan', 'Başak',
    'Terazi', 'Akrep', 'Yay', 'Oğlak', 'Kova', 'Balık'
]


def derece_to_burc(derece):
    burc_index = int(derece / 30)
    burc_ici_derece = derece % 30
    return BURCLAR[burc_index], round(burc_ici_derece, 1)


def sehir_koordinat_bul(sehir_adi):
    """Şehir ismini enlem/boylama çevirir."""
    geolocator = Nominatim(user_agent="astroloji_sitesi")
    konum = geolocator.geocode(sehir_adi)
    if konum:
        return konum.latitude, konum.longitude
    return None, None


def yerel_saati_utc_ye_cevir(dogum_tarihi, dogum_saati, enlem, boylam):
    """Doğum saatini (yerel) UTC saatine çevirir."""
    tf = TimezoneFinder()
    saat_dilimi_adi = tf.timezone_at(lat=enlem, lng=boylam)

    if not saat_dilimi_adi:
        saat_dilimi_adi = 'Europe/Istanbul'  # bulunamazsa varsayılan

    yerel_dt = datetime.combine(dogum_tarihi, dogum_saati)
    saat_dilimi = pytz.timezone(saat_dilimi_adi)
    yerel_dt_with_tz = saat_dilimi.localize(yerel_dt)
    utc_dt = yerel_dt_with_tz.astimezone(pytz.utc)

    return utc_dt


def gezegen_konumlarini_hesapla(dogum_tarihi, dogum_saati, dogum_yeri=None):
    enlem, boylam = None, None

    if dogum_yeri:
        enlem, boylam = sehir_koordinat_bul(dogum_yeri)

    if enlem and boylam:
        utc_dt = yerel_saati_utc_ye_cevir(dogum_tarihi, dogum_saati, enlem, boylam)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                         utc_dt.hour + utc_dt.minute / 60)
    else:
        # Koordinat bulunamazsa, saat dilimi dönüşümü yapmadan hesapla (daha az kesin)
        yil, ay, gun = dogum_tarihi.year, dogum_tarihi.month, dogum_tarihi.day
        saat = dogum_saati.hour + dogum_saati.minute / 60
        jd = swe.julday(yil, ay, gun, saat)

    sonuclar = {}
    for isim, kod in GEZEGENLER.items():
        pozisyon, _ = swe.calc_ut(jd, kod)
        derece = pozisyon[0]
        burc, burc_ici_derece = derece_to_burc(derece)
        sonuclar[isim] = {'burc': burc, 'derece': burc_ici_derece}

    # Ev hesaplaması (sadece koordinat varsa yapılabilir)
    evler = {}
    yukselen = None
    if enlem and boylam:
        ev_sonuclari, ascmc = swe.houses(jd, enlem, boylam, b'P')  # Placidus ev sistemi
        for i, ev_derecesi in enumerate(ev_sonuclari, start=1):
            burc, burc_ici_derece = derece_to_burc(ev_derecesi)
            evler[i] = {'burc': burc, 'derece': burc_ici_derece}

        # Yükselen burç (Ascendant) = ascmc listesinin ilk elemanı
        yukselen_derece = ascmc[0]
        yukselen_burc, yukselen_ici_derece = derece_to_burc(yukselen_derece)
        yukselen = {'burc': yukselen_burc, 'derece': yukselen_ici_derece}

    return {
        'gezegenler': sonuclar,
        'evler': evler,
        'yukselen': yukselen,
    }

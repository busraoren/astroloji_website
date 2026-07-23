KART_GORSEL_ESLESTIRME = {
    # Majör Arkana
    "Deli": "00-TheFool.jpg",
    "Büyücü": "01-TheMagician.jpg",
    "Azize": "02-TheHighPriestess.jpg",
    "İmparatoriçe": "03-TheEmpress.jpg",
    "İmparator": "04-TheEmperor.jpg",
    "Aziz": "05-TheHierophant.jpg",
    "Aşıklar": "06-TheLovers.jpg",
    "Savaş Arabası": "07-TheChariot.jpg",
    "Güç": "08-Strength.jpg",
    "Ermiş": "09-TheHermit.jpg",
    "Kader Çarkı": "10-WheelOfFortune.jpg",
    "Adalet": "11-Justice.jpg",
    "Asılan Adam": "12-TheHangedMan.jpg",
    "Ölüm": "13-Death.jpg",
    "Denge": "14-Temperance.jpg",
    "Şeytan": "15-TheDevil.jpg",
    "Kule": "16-TheTower.jpg",
    "Yıldız": "17-TheStar.jpg",
    "Ay": "18-TheMoon.jpg",
    "Güneş": "19-TheSun.jpg",
    "Mahkeme": "20-Judgement.jpg",
    "Dünya": "21-TheWorld.jpg",

    # Kupalar
    "Kupa Ası": "Cups01.jpg",
    "Kupa İkilisi": "Cups02.jpg",
    "Kupa Üçlüsü": "Cups03.jpg",
    "Kupa Dörtlüsü": "Cups04.jpg",
    "Kupa Beşlisi": "Cups05.jpg",
    "Kupa Altılısı": "Cups06.jpg",
    "Kupa Yedilisi": "Cups07.jpg",
    "Kupa Sekizlisi": "Cups08.jpg",
    "Kupa Dokuzlusu": "Cups09.jpg",
    "Kupa Onlusu": "Cups10.jpg",
    "Kupa Prensi": "Cups11.jpg",
    "Kupa Şövalyesi": "Cups12.jpg",
    "Kupa Kraliçesi": "Cups13.jpg",
    "Kupa Kralı": "Cups14.jpg",

    # Tılsımlar (Pentacles)
    "Tılsım Ası": "Pentacles01.jpg",
    "Tılsım İkilisi": "Pentacles02.jpg",
    "Tılsım Üçlüsü": "Pentacles03.jpg",
    "Tılsım Dörtlüsü": "Pentacles04.jpg",
    "Tılsım Beşlisi": "Pentacles05.jpg",
    "Tılsım Altılısı": "Pentacles06.jpg",
    "Tılsım Yedilisi": "Pentacles07.jpg",
    "Tılsım Sekizlisi": "Pentacles08.jpg",
    "Tılsım Dokuzlusu": "Pentacles09.jpg",
    "Tılsım Onlusu": "Pentacles10.jpg",
    "Tılsım Prensi": "Pentacles11.jpg",
    "Tılsım Şövalyesi": "Pentacles12.jpg",
    "Tılsım Kraliçesi": "Pentacles13.jpg",
    "Tılsım Kralı": "Pentacles14.jpg",

    # Kılıçlar (Swords)
    "Kılıç Ası": "Swords01.jpg",
    "Kılıç İkilisi": "Swords02.jpg",
    "Kılıç Üçlüsü": "Swords03.jpg",
    "Kılıç Dörtlüsü": "Swords04.jpg",
    "Kılıç Beşlisi": "Swords05.jpg",
    "Kılıç Altılısı": "Swords06.jpg",
    "Kılıç Yedilisi": "Swords07.jpg",
    "Kılıç Sekizlisi": "Swords08.jpg",
    "Kılıç Dokuzlusu": "Swords09.jpg",
    "Kılıç Onlusu": "Swords10.jpg",
    "Kılıç Prensi": "Swords11.jpg",
    "Kılıç Şövalyesi": "Swords12.jpg",
    "Kılıç Kraliçesi": "Swords13.jpg",
    "Kılıç Kralı": "Swords14.jpg",

    # Değnekler (Wands)
    "Değnek Ası": "Wands01.jpg",
    "Değnek İkilisi": "Wands02.jpg",
    "Değnek Üçlüsü": "Wands03.jpg",
    "Değnek Dörtlüsü": "Wands04.jpg",
    "Değnek Beşlisi": "Wands05.jpg",
    "Değnek Altılısı": "Wands06.jpg",
    "Değnek Yedilisi": "Wands07.jpg",
    "Değnek Sekizlisi": "Wands08.jpg",
    "Değnek Dokuzlusu": "Wands09.jpg",
    "Değnek Onlusu": "Wands10.jpg",
    "Değnek Prensi": "Wands11.jpg",
    "Değnek Şövalyesi": "Wands12.jpg",
    "Değnek Kraliçesi": "Wands13.jpg",
    "Değnek Kralı": "Wands14.jpg",
}

def kart_gorsel_yolu(kart_ismi):
    dosya_adi = KART_GORSEL_ESLESTIRME.get(kart_ismi)
    if dosya_adi:
        return f"tarot/kartlar/Cards-jpg/{dosya_adi}"
    return None

def kart_sirti_yolu():
    return "tarot/kartlar/Cards-jpg/CardBacks.jpg"
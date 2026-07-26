import datetime
from .motivasyon_sozleri import MOTIVASYON_SOZLERI
from .ay_fazi import ay_fazini_hesapla


def global_widgetler(request):
    gun_no = datetime.date.today().timetuple().tm_yday
    gunun_sozu = MOTIVASYON_SOZLERI[gun_no % len(MOTIVASYON_SOZLERI)]
    ay_fazi = ay_fazini_hesapla()
    return {
        'gunun_sozu': gunun_sozu,
        'ay_fazi': ay_fazi,
    }
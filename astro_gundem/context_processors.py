from .views import anasayfa_icin_aktif_gundem

def aktif_gundem_context(request):
    return {'nav_aktif_gundem': anasayfa_icin_aktif_gundem()}
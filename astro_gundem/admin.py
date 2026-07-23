from django.contrib import admin
from .models import AstroGundem

@admin.register(AstroGundem)
class AstroGundemAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'tur', 'baslangic_tarihi', 'bitis_tarihi', 'aktif_mi')
    list_filter = ('tur', 'aktif_mi')
    search_fields = ('baslik',)

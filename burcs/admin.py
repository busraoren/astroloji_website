# burcs/admin.py
from django.contrib import admin
from .models import BurcYorumu, KozmikTest, TestSonucu, Soru, Secenek

admin.site.register(BurcYorumu)

class TestSonucuInline(admin.TabularInline):
    model = TestSonucu
    extra = 3

class SoruInline(admin.TabularInline):
    model = Soru
    extra = 1
    show_change_link = True

@admin.register(KozmikTest)
class KozmikTestAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'olusturulma_tarihi')
    prepopulated_fields = {'slug': ('baslik',)}
    inlines = [TestSonucuInline, SoruInline]

class SecenekInline(admin.TabularInline):
    model = Secenek
    extra = 4

@admin.register(Soru)
class SoruAdmin(admin.ModelAdmin):
    list_display = ('test', 'sira', 'metin')
    list_filter = ('test',)
    inlines = [SecenekInline]
from django import forms

TAILWIND_INPUT = 'w-full p-3 rounded-lg bg-white/10 border border-purple-800/40 mb-4 text-white'

class UyumlulukFormu(forms.Form):
    kisi1_isim = forms.CharField(label='1. Kişinin İsmi', max_length=100)
    kisi1_dogum_tarihi = forms.DateField(
        label='1. Kişinin Doğum Tarihi',
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    kisi1_dogum_saati = forms.TimeField(
        label='1. Kişinin Doğum Saati',
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    kisi1_dogum_yeri = forms.CharField(label='1. Kişinin Doğum Yeri', max_length=100, required=False)

    kisi2_isim = forms.CharField(label='2. Kişinin İsmi', max_length=100)
    kisi2_dogum_tarihi = forms.DateField(
        label='2. Kişinin Doğum Tarihi',
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    kisi2_dogum_saati = forms.TimeField(
        label='2. Kişinin Doğum Saati',
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    kisi2_dogum_yeri = forms.CharField(label='2. Kişinin Doğum Yeri', max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': TAILWIND_INPUT})
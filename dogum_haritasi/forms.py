from django import forms

TAILWIND_INPUT = 'w-full p-3 rounded-lg bg-white/10 border border-purple-800/40 mb-4 text-white'

class DogumHaritasiFormu(forms.Form):
    isim = forms.CharField(label='İsim', max_length=100, required=False)
    dogum_tarihi = forms.DateField(
        label='Doğum Tarihi',
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    dogum_saati = forms.TimeField(
        label='Doğum Saati',
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    dogum_yeri = forms.CharField(label='Doğum Yeri', max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': TAILWIND_INPUT})
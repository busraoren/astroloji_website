from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import KullaniciProfili

TAILWIND_INPUT = 'w-full p-3 rounded-lg bg-white/10 border border-purple-800/40 mb-4 text-white'

class KayitFormu(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': TAILWIND_INPUT})


class ProfilFormu(forms.ModelForm):
    dogum_tarihi = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
        required=False,
        label='Doğum Tarihi'
    )

    class Meta:
        model = KullaniciProfili
        fields = ['dogum_tarihi', 'dogum_saati', 'dogum_yeri']
        widgets = {
            'dogum_saati': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dogum_yeri'].label = 'Doğum Yeri'
        self.fields['dogum_saati'].label = 'Doğum Saati'
        for field in self.fields.values():
            field.widget.attrs.update({'class': TAILWIND_INPUT})
from django import forms
from .models import Film, Dizi

class FilmEklemeFormu(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('isim', 'yil', 'tur', 'resim_yolu')

class DiziEklemeFormu(forms.ModelForm):
    class Meta:
        model = Dizi
        fields = ('isim', 'yil', 'tur', 'resim_yolu')

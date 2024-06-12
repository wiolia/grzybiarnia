from django import forms
from .models import Grzyb, Kategoria, Zdjecie

class GrzybForm(forms.ModelForm):
    class Meta:
        model = Grzyb
        fields = ['nazwa', 'opis', 'kategoria', 'zdjecia']  

class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = ['nazwa', 'jadalne']

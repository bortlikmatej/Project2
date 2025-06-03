from django import forms
from .models import Ram, Vidlice, Brzdy, Prehazovacka

class KonfiguratorForm(forms.Form):
    ram = forms.ModelChoiceField(queryset=Ram.objects.all(), label="Rám", 
                                 widget=forms.Select(attrs={'class': 'custom-select'}))
    vidlice = forms.ModelChoiceField(queryset=Vidlice.objects.all(), label="Vidlice", 
                                     widget=forms.Select(attrs={'class': 'custom-select'}))
    brzdy = forms.ModelChoiceField(queryset=Brzdy.objects.all(), label="Brzdy", 
                                   widget=forms.Select(attrs={'class': 'custom-select'}))
    prehazovacka = forms.ModelChoiceField(queryset=Prehazovacka.objects.all(), label="Přehazovačka", 
                                          widget=forms.Select(attrs={'class': 'custom-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in ['ram', 'vidlice', 'brzdy', 'prehazovacka']:
            field = self.fields[field_name]
            field.widget.choices = [(str(obj.pk), f"{obj.nazev} ({self.format_cena(obj.cena)})") for obj in field.queryset]

    def format_cena(self, cena):
        
        return f"{cena:,} Kč".replace(',', ' ')  
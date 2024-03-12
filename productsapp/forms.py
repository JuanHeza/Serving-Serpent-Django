from django import forms
from .models import Price


class PriceForm(forms.ModelForm):

    class Meta:
        model = Price
        fields = ('producto', 'precio')

from django import forms

from webapp.models import CATEGORY

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=True, label='Описание')
    category = forms.ChoiceField(choices=CATEGORY, required=True, label='Категория')
    remainder = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label='Цена')

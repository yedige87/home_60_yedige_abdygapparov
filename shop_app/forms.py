from django import forms
from django.core.exceptions import ValidationError

from shop_app.models import Product, Basket, Customer


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'text', 'price', 'photo', 'qty', 'category']
        labels = {
            'title': 'Наименование',
            'text': 'Описание',
            'price': 'Стоимость',
            'photo': 'Изображение',
            'qty': 'Остатки',
            'category': 'Категория'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


class BasketForm(forms.ModelForm):
    qty_prod = forms.IntegerField(disabled=True, label='Остаток товара в магазине')

    class Meta:
        model = Basket
        fields = ('qty_prod', 'qty')

    def clean_qty(self):
        qty = self.cleaned_data.get('qty')
        qty_prod = self.cleaned_data.get('qty_prod')
        if qty > qty_prod:
            raise ValidationError('Превышение количества товаров в магазине!')
        return qty

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'address')

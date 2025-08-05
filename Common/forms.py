from django import forms
from django.core.exceptions import ValidationError
from Shop.models import Product

class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['size']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'price': forms.TextInput(attrs={'class': 'form-input'}),
            'image_url': forms.TextInput(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price






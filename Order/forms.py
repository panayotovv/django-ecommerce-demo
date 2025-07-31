from django import forms
from Order.models import Order


class CartForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['total_price', 'user', 'profile']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-input'}),
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'postal_code': forms.NumberInput(attrs={'class': 'form-input'}),
            'city': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-input'}),
            'shipping_address': forms.TextInput(attrs={'class': 'form-input'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-input'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-input'}),
        }

class CheckoutForm(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    expiration_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-input'}))
    security_code = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-input'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))

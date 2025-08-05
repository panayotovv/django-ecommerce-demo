from django import forms
from Order.models import Order, CardDetails


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
            'size': forms.RadioSelect,
        }


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CardDetails
        exclude = ['order']
        widgets = {
            'card_number': forms.PasswordInput(attrs={'class': 'form-input'}),
            'expiration_date': forms.TextInput(attrs={'class': 'form-input'}),
            'security_code': forms.TextInput(attrs={'class': 'form-input'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }


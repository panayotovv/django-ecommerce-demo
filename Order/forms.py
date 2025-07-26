from django import forms

class CartForm(forms.Form):
    country = forms.CharField(
        label="Country/Region",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",
    )
    full_name = forms.CharField(
        label="Full name",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",
    )
    postal_code = forms.CharField(
        label="Postal code",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",
    )
    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",
    )
    email = forms.CharField(
        label="Email",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",
    )
    phone_number = forms.CharField(
        label="Phone number",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",
    )
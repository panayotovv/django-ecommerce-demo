from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from Accounts.validators import validate_email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
        })
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",

    )
    email = forms.CharField(
        label="Email",
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        help_text="",
        validators=[validate_email]
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        help_text="",
    )
    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        help_text="",
    )




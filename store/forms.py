from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
    {
        'class': 'form-control',
        'placeholder': "Foydalanuvchi ismi"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolni tasdiqlang'
    }))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Foydalanuvchi ismi"
            }),
            "email": forms.EmailInput(attrs={
                "class": 'form-control',
                "placeholder": "Email"
            })
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comments.....',
            })
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismingiz...'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sizning Familyangiz...'
            })
        }


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('address', 'city', 'state', 'phone')
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adress...'
            }),
            'city': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Shahar nomi...'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rayon nomi...'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Raqamingiz...'
            }),
        }

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded', 'rows': 3
    }))
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded'
    }))

    class Meta:
        model = Profile
        fields = ['address', 'profile_image']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-300 p-2 w-full rounded',
            'placeholder': 'Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 p-2 w-full rounded',
            'placeholder': 'Password'
        })
    )
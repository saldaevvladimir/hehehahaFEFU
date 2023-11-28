from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Погоняло'}))
    password = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Секретное слово', 'type': 'password'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Погоняло'}))
    password1 = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Секретное слово', 'type': 'password'}))
    password2 = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Секретное слово', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

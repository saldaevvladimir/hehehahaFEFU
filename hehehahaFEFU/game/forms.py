from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Погоняло'}))
    password1 = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Секретное слово', 'type': 'password'}))
    password2 = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Секретное слово', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')



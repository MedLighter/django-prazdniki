from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': "username", 'placeholder': 'Почта'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password', 'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Почта'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password', 'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password', 'placeholder': 'Повторите пароль'
    }))
    

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control'
    }),
        required=False)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control'
    }),
        required=False)
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input',
               'id': 'image-upload',
               }),
        required=False
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image')
from django import forms

from .models import Application

class UserCreateApplicationForm(forms.ModelForm):
    customer_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'clearble form-control', 'placeholder': 'Ваше имя', 'style': 'margin-top: 20px;', 'size': '20'
    }))
    customer_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'clearble form-control ', 'placeholder': 'Ваш телефон', 'style': 'margin-top: 15px;', 'size': '20'
    }))
    
    
    class Meta:
        model = Application
        fields = ("customer_name", "customer_number")
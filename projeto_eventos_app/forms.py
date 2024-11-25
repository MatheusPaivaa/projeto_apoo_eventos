from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefone', 'cpf', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Nome Completo'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['telefone'].widget = forms.TextInput(attrs={'placeholder': 'Telefone'})
        self.fields['cpf'].widget = forms.TextInput(attrs={'placeholder': 'CPF'})

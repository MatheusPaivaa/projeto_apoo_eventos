from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import Evento

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefone', 'cpf', 'user_type', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirme sua senha'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Nome Completo'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})
        self.fields['telefone'].widget = forms.TextInput(attrs={'placeholder': 'Telefone'})
        self.fields['cpf'].widget = forms.TextInput(attrs={'placeholder': 'CPF'})
        self.fields['user_type'].widget = forms.Select(
            attrs={'placeholder': 'Escolha como você usará a plataforma'},
            choices=CustomUser.USER_TYPE_CHOICES
        )
        self.fields['user_type'].label = "Como você usará a plataforma?"

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_approved:
            raise forms.ValidationError(
                "Sua conta ainda não foi liberada pelo moderador.",
                code='inactive',
            )
        

class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefone', 'cpf']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data', 'local', 'publico_alvo', 'colaboradores', 'imagem_capa'] 
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do evento'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição detalhada'}),
            'data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o local'}),
            'publico_alvo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Estudantes, Profissionais'}),
            'colaboradores': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
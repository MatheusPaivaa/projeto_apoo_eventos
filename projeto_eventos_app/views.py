from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

@login_required
def home(request):
    return render(request, 'projeto_eventos/home.html')

@login_required
def events(request):
    return render(request, 'projeto_eventos/events.html')

@login_required
def user_events(request):
    return render(request, 'projeto_eventos/user_events.html')

@login_required
def notifications(request):
    return render(request, 'projeto_eventos/notification.html')

@login_required
def certificates(request):
    return render(request, 'projeto_eventos/certificates.html')

@login_required
def my_account(request):
    return render(request, 'projeto_eventos/my_account.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['nome']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')

    return render(request, 'projeto_eventos/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso.')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro realizado com sucesso! Você pode fazer login agora.')
            return redirect('/login')
        else:
            messages.error(request, 'Erro ao registrar. Verifique os dados informados.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'projeto_eventos/register.html', {'form': form})

def forgot_pass(request):
    return render(request, 'projeto_eventos/forgot_pass.html')

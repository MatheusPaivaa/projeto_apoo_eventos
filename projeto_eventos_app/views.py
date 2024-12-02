from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from .models import Evento, CustomUser
from .forms import EventoForm, EditUserForm

User = get_user_model()

@staff_member_required
def gerenciar_eventos(request):
    return render(request, 'projeto_eventos/gerenciar_eventos.html')

@user_passes_test(lambda u: u.is_staff)  # Apenas administradores podem acessar
def gerenciar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'projeto_eventos/gerenciar_usuarios.html', {'usuarios': usuarios})

def detalhes_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)  # Busca o evento pelo ID
    return render(request, 'projeto_eventos/detalhes_evento.html', {'evento': evento})

@user_passes_test(lambda u: u.is_staff)
def aprovar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.is_approved = True
        user.save()
        messages.success(request, f"Usuário {user.username} foi aprovado com sucesso!")
    return redirect('gerenciar_usuarios')

def home(request):
    total_eventos = Evento.objects.count()
    total_usuarios = CustomUser.objects.count()
    eventos_populares = Evento.objects.filter(popular=True)[:5]  # Exemplo de filtro
    return render(request, 'projeto_eventos/home.html', {
        'total_eventos': total_eventos,
        'total_usuarios': total_usuarios,
    })

@login_required
def events(request):
    eventos = Evento.objects.all()  # Busca todos os eventos
    return render(request, 'projeto_eventos/events.html', {'eventos': eventos})

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
    user = request.user
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Suas informações foram atualizadas com sucesso!")
            return redirect('home')
    else:
        form = EditUserForm(instance=user)
    
    return render(request, 'projeto_eventos/my_account.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('nome')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_approved:
                login(request, user)
                return redirect('home')  # Redireciona para a página inicial
            else:
                messages.error(request, 'Sua conta ainda não foi liberada pelo moderador.')
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
            user = form.save(commit=False)  # Cria o usuário, mas não salva ainda
            # Verifica o tipo de usuário e define o status de aprovação
            if user.user_type != 'comum':  
                user.is_approved = False  # Usuários não comuns aguardam liberação
            user.save()  # Agora salva no banco com o status correto
            # Exibe mensagens apropriadas
            if not user.is_approved:
                messages.success(request, 'Cadastro realizado! Aguardando liberação do moderador.')
            else:
                messages.success(request, 'Registro realizado com sucesso! Você pode fazer login agora.')
            return redirect('/login')  # Redireciona para a página de login
        else:
            messages.error(request, 'Erro ao registrar. Verifique os dados informados.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'projeto_eventos/register.html', {'form': form})


def forgot_pass(request):
    return render(request, 'projeto_eventos/forgot_pass.html')

@login_required
@user_passes_test(lambda u: u.user_type == 'organizador', login_url='/')
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)  # Inclua request.FILES para processar uploads
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user
            evento.save()
            form.save_m2m()  # Salva os colaboradores
            messages.success(request, "Evento criado com sucesso!")
            return redirect('meus_eventos_organizador')
    else:
        form = EventoForm()

    return render(request, 'projeto_eventos/criar_evento.html', {'form': form})


@login_required
def editar_evento(request):
    if request.method == 'POST':
        evento_id = request.POST.get('id')
        evento = get_object_or_404(Evento, id=evento_id, organizador=request.user)
        evento.nome = request.POST.get('nome')
        evento.descricao = request.POST.get('descricao')
        evento.data = request.POST.get('data')
        evento.local = request.POST.get('local')
        evento.save()
        messages.success(request, "Evento atualizado com sucesso!")
    return redirect('home')

@login_required
def excluir_evento(request):
    if request.method == 'POST':
        evento_id = request.POST.get('id')
        evento = get_object_or_404(Evento, id=evento_id, organizador=request.user)
        evento.delete()
        messages.success(request, "Evento excluído com sucesso!")
    return redirect('home')

@login_required
def meus_eventos_organizador(request):
    eventos = Evento.objects.filter(organizador=request.user)
    return render(request, 'projeto_eventos/meus_eventos_organizador.html', {'eventos': eventos})

@login_required
@user_passes_test(lambda u: u.user_type == 'profissional', login_url='/')  # Apenas profissionais
def minhas_contratacoes(request):
    contratacoes = [] 
    return render(request, 'projeto_eventos/minhas_contratacoes.html', {'contratacoes': contratacoes})

@login_required
@user_passes_test(lambda u: u.user_type == 'profissional', login_url='/')  # Apenas profissionais
def cadastrar_servicos(request):
    if request.method == 'POST':
        pass
    return render(request, 'projeto_eventos/cadastrar_servicos.html')

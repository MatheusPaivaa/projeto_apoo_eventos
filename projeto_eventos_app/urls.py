from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from projeto_eventos_app import views

urlpatterns = [
    # Páginas públicas
    path("", views.login_view, name="login"),
    path("registrar/", views.register, name="registrar"),
    path("esqueceuSenha/", views.forgot_pass, name="esqueceuSenha"),
    path("logout/", views.logout_view, name="logout"),

    # Páginas gerais (protegidas)
    path("home/", login_required(views.home), name="home"),
    path("eventos/", login_required(views.events), name="eventos"),
    path("meusEventos/", login_required(views.user_events), name="meusEventos"),
    path("notificacoes/", login_required(views.notifications), name="notificacoes"),
    path("certificados/", login_required(views.certificates), name="certificados"),
    path("minhaConta/", login_required(views.my_account), name="minhaConta"),

    # Páginas de gerenciamento (protegidas - staff only)
    path("gerenciar-eventos/", login_required(views.gerenciar_eventos), name="gerenciar_eventos"),
    path("gerenciar-usuarios/", login_required(views.gerenciar_usuarios), name="gerenciar_usuarios"),
    path("aprovar-usuario/<int:user_id>/", login_required(views.aprovar_usuario), name="aprovar_usuario"),

    # Eventos (protegidos - organizador)
    path("criar-evento/", login_required(views.criar_evento), name="criar_evento"),
    path("meus-eventos-organizador/", login_required(views.meus_eventos_organizador), name="meus_eventos_organizador"),
    path("editar-evento/", login_required(views.editar_evento), name="editar_evento"),
    path("excluir-evento/", login_required(views.excluir_evento), name="excluir_evento"),
    path("eventos/<int:evento_id>/", login_required(views.detalhes_evento), name="detalhes_evento"),

    # Profissionais (protegidas)
    path("minhas-contratacoes/", login_required(views.minhas_contratacoes), name="minhas_contratacoes"),
    path("cadastrar-servicos/", login_required(views.cadastrar_servicos), name="cadastrar_servicos"),
]

# Adiciona suporte a arquivos estáticos em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from projeto_eventos_app import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("registrar/", views.register, name="registrar"),
    path("esqueceuSenha/", views.forgot_pass, name="esqueceuSenha"),
    path("", views.home, name="home"),
    path("eventos/", views.events, name="eventos"),
    path("meusEventos/", views.user_events, name="meusEventos"),
    path("notificacoes/", views.notifications, name="notificacoes"),
    path("certificados/", views.certificates, name="certificados"),
    path("minhaConta/", views.my_account, name="minhaConta"),
    path("logout/", views.logout_view, name="logout"),
    path('gerenciar-eventos/', views.gerenciar_eventos, name='gerenciar_eventos'),
    path('gerenciar-usuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),
    path('aprovar-usuario/<int:user_id>/', views.aprovar_usuario, name='aprovar_usuario'),
    path('criar-evento/', views.criar_evento, name='criar_evento'),
    path('meus-eventos-organizador/', views.meus_eventos_organizador, name='meus_eventos_organizador'),
    path('minhas-contratacoes/', views.minhas_contratacoes, name='minhas_contratacoes'),
    path('cadastrar-servicos/', views.cadastrar_servicos, name='cadastrar_servicos'),
    path('eventos/<int:evento_id>/', views.detalhes_evento, name='detalhes_evento'),
    path('editar-evento/', views.editar_evento, name='editar_evento'),
    path('excluir-evento/', views.excluir_evento, name='excluir_evento'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
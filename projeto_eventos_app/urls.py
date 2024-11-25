from django.urls import path
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
]

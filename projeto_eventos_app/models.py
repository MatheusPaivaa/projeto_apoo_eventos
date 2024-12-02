from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, verbose_name="Telefone")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    email = models.EmailField(unique=True, verbose_name="Email")

    # Tipos de usuário
    ORGANIZADOR_EVENTOS = 'organizador'
    PROFISSIONAL_EVENTOS = 'profissional'
    USUARIO_COMUM = 'comum'

    USER_TYPE_CHOICES = [
        (ORGANIZADOR_EVENTOS, 'Organizador de Eventos'),
        (PROFISSIONAL_EVENTOS, 'Profissional de Eventos'),
        (USUARIO_COMUM, 'Usuário Comum'),
    ]

    user_type = models.CharField(
        max_length=15,
        choices=USER_TYPE_CHOICES,
        default=USUARIO_COMUM,
        verbose_name="Tipo de Usuário"
    )
    
    is_approved = models.BooleanField(
        default=True,
        verbose_name="Usuário Liberado"
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=255)
    publico_alvo = models.CharField(max_length=255, blank=True, null=True)
    organizador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="eventos")
    colaboradores = models.ManyToManyField(CustomUser, related_name="colaboracoes", blank=True)
    imagem_capa = models.ImageField(upload_to='eventos/capas/', blank=True, null=True)  # Caminho para salvar a imagem

    def __str__(self):
        return self.nome
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Exibição dos campos no formulário de edição do usuário
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'cpf', 'user_type')}),
    )

    # Exibição dos campos no formulário de adição de usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefone', 'cpf', 'user_type')}),
    )

    # Colunas exibidas na lista de usuários no Django Admin
    list_display = ('username', 'email', 'telefone', 'cpf', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active', 'groups')

    # Campos utilizados na busca
    search_fields = ('username', 'email', 'telefone', 'cpf')

    # Ordenação padrão
    ordering = ('username',)

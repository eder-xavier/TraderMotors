from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('nome_completo', 'telefone', 'endereco')}),
    )
    list_display = ('username', 'nome_completo', 'email', 'telefone')

admin.site.register(CustomUser, CustomUserAdmin)

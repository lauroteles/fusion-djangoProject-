
from django.contrib import admin
from .models import Servico, Cargo, Equipe

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ( 'modificado', 'criados')
    search_fields = ('modificado', 'criados')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'modificado', 'criados')
    search_fields = ('cargo', 'modificado', 'criados')

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'criados')
    search_fields = ('nome', 'cargo', 'modificado', 'criados')
from django.contrib import admin
from core.models import Servico

# Register your models here.

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'empresa','telefone', 'email', 'prioridade', 'servico', 'descricao', 'data_criacao', 'status',)
    list_filter = ('nome_completo','status',)

admin.site.register(Servico, ServicoAdmin)


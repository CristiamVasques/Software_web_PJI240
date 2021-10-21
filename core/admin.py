from django.contrib import admin
from core.models import Servico

# Register your models here.

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'data_criacao')
    list_filter = ('nome_completo',)

admin.site.register(Servico, ServicoAdmin)


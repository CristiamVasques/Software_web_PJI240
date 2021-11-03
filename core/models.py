from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Servico(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    empresa = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=50)
    servico = models.CharField(max_length=50, verbose_name='Serviço')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data_criacao= models.DateTimeField(auto_now=True, verbose_name='Solicitado')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='Pendente')



    class Meta:
        db_table = 'servico'

    def __str__(self):
        return self.servico





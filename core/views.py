from django.shortcuts import render
from core.models import Servico


# Create your views here.

def lista_servicos(request):
    usuario = request.user
    servicos = Servico.objects.all()
    dados = {'servicos':servicos}
    return render(request, 'servicos.html', dados)

from django.shortcuts import render, redirect
from core.models import Servico
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def lista_servicos(request):
    usuario = request.user
    servicos = Servico.objects.filter(usuario=usuario)
    dados = {'servicos':servicos}
    return render(request, 'servicos.html', dados)

@login_required(login_url='/login/')
def solicitacao(request):
    return render(request, 'solicitacao.html')

@login_required(login_url='/login/')
def submit_solicitacao(request):
    if request.POST:
        nome_completo = request.POST.get('nome_completo')
        empresa = request.POST.get('empresa')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        prioridade = request.POST.get('prioridade')
        servico = request.POST.get('servico')
        usuario = request.user
        Servico.objects.create(nome_completo=nome_completo,
                               empresa=empresa,
                               telefone=telefone,
                               email=email,
                               prioridade=prioridade,
                               servico=servico,
                               usuario=usuario)
    return redirect('/accounts/profile/')


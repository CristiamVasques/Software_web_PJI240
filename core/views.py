from django.shortcuts import render, redirect
from core.models import Servico
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect ('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

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
    return redirect('/')

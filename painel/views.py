from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Imovel, AtividadeUsuario, EventoFundiario

# Overview (painel principal)
def painel_overview(request):
    imoveis = Imovel.objects.all()
    total = imoveis.count()

    completos = imoveis.filter(
        tem_ccir=True,
        tem_georreferenciamento=True,
        tem_reserva_legal=True
    ).count()

    faltando_ccir = imoveis.filter(tem_ccir=False).count()
    faltando_geo = imoveis.filter(tem_georreferenciamento=False).count()
    faltando_reserva = imoveis.filter(tem_reserva_legal=False).count()

    pendentes = total - completos

    # Simulando usuário logado (nome e email via session)
    nome_usuario = request.session.get('nome', 'Augusto França')
    email_usuario = request.session.get('email', 'augustofranca0701@gmail.com')

    # Atualização via POST
    if request.method == 'POST':
        nome_novo = request.POST.get('nome')
        email_novo = request.POST.get('email')
        request.session['nome'] = nome_novo
        request.session['email'] = email_novo
        messages.success(request, 'Dados atualizados com sucesso!')
        return redirect('painel_overview')

    atividades = AtividadeUsuario.objects.order_by('-data')[:10]

    context = {
        "imoveis": imoveis,
        "total": total,
        "completos": completos,
        "pendentes": pendentes,
        "faltando_ccir": faltando_ccir,
        "faltando_geo": faltando_geo,
        "faltando_reserva": faltando_reserva,
        "atividades": atividades,
        "nome": nome_usuario,
        "email": email_usuario,
    }
    return render(request, 'painel/overview.html', context)

# Lista de imóveis
def lista_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'painel/lista_imoveis.html', {'imoveis': imoveis})

# Detalhes (com eventos fundiários)
def detalhes_imovel(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    eventos = imovel.eventos.order_by('-data')
    return render(request, 'painel/detalhes_imovel.html', {'imovel': imovel, 'eventos': eventos})

# Página da equipe
def equipe_view(request):
    return render(request, 'painel/equipe.html')

# Relatórios (histórico de compras)
def relatorios_view(request):
    return render(request, 'painel/relatorios.html')

# Modo simulação
def modo_simulacao(request):
    return render(request, 'painel/modo_simulacao.html')

# Comparador de imóveis
def comparador_view(request):
    imoveis = Imovel.objects.all()
    imovel1 = imovel2 = None

    if request.method == 'GET':
        id1 = request.GET.get('imovel1')
        id2 = request.GET.get('imovel2')

        if id1 and id2 and id1 != id2:
            imovel1 = Imovel.objects.filter(pk=id1).first()
            imovel2 = Imovel.objects.filter(pk=id2).first()

    context = {
        'imoveis': imoveis,
        'imovel1': imovel1,
        'imovel2': imovel2,
    }
    return render(request, 'painel/comparador.html', context)

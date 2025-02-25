from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import CustomUserForm
from django.views.decorators.csrf import csrf_exempt
from .models import Peca, InteracaoUsuario
from django.db.models import Q
from .api_fipe import buscar_automoveis_fipe, obter_detalhes_automovel_fipe
from .utils import obter_dados_interacao_automoveis, preparar_dados_para_modelo # Importe as funções de utils.py

def home(request):
    return render(request, 'home/home.html')

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('MainTM:home')
    else:
        form = CustomUserForm()
    return render(request, 'home/register.html', {'form': form})

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('MainTM:home')
    return render(request, 'home/login.html')

def buscar_automoveis(request):
    query = request.GET.get('q')
    automoveis = []
    if query:
        automoveis = buscar_automoveis_fipe(query)
        for automovel in automoveis:
            if request.user.is_authenticated:
                InteracaoUsuario.objects.create(
                    usuario=request.user,
                    codigo_fipe=automovel['codigo_fipe'],
                    tipo_interacao='busca'
                )
    return render(request, 'automoveis/buscar_automoveis.html', {'automoveis': automoveis, 'query': query})

def detalhe_automovel(request, codigo_fipe):
    automovel = obter_detalhes_automovel_fipe(codigo_fipe)

    InteracaoUsuario.objects.create(
        usuario=request.user,
        codigo_fipe=codigo_fipe,
        tipo_interacao='visualizacao'
    )
    return render(request, 'automoveis/detalhe_automovel.html', {'automovel': automovel})

def buscar_pecas(request):
    query = request.GET.get('q')
    pecas = Peca.objects.all()
    if query:
        pecas = pecas.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))
    for peca in pecas:
        if request.user.is_authenticated:
            InteracaoUsuario.objects.create(
                usuario=request.user,
                peca=peca,
                tipo_interacao='busca'
            )
    return render(request, 'pecas/buscar_pecas.html', {'pecas': pecas, 'query': query})

def detalhe_peca(request, peca_id):
    peca = get_object_or_404(Peca, pk=peca_id)
    if request.user.is_authenticated:
        InteracaoUsuario.objects.create(
            usuario=request.user,
            peca=peca,
            tipo_interacao='visualizacao'
        )
    return render(request, 'pecas/detalhe_peca.html', {'peca': peca})

from .recomendacoes import treinar_modelo_recomendacao

def obter_recomendacoes_automoveis(request):
    usuario_id = request.user.id
    modelo_knn, matriz_usuario_item = treinar_modelo_recomendacao()
    usuario_index = matriz_usuario_item.index.get_loc(usuario_id)
    distancias, vizinhos = modelo_knn.kneighbors(matriz_usuario_item.iloc[usuario_index].values.reshape(1, -1), n_neighbors=6)
    recomendacoes_ids = matriz_usuario_item.columns[vizinhos.flatten()[1:]]
    recomendacoes = []
    for codigo_fipe in recomendacoes_ids:
        automovel = obter_detalhes_automovel_fipe(codigo_fipe)
        if automovel:
            recomendacoes.append(automovel)
    return render(request, 'automoveis/recomendacoes_automoveis.html', {'recomendacoes': recomendacoes})


def consultar_veiculo_fipe(request):
    if request.method == 'POST':
        codigo_fipe = request.POST.get('codigo_fipe')
        if codigo_fipe:
            automovel = obter_detalhes_automovel_fipe(codigo_fipe)
            if automovel:
                return render(request, 'automoveis/detalhe_automovel.html', {'automovel': automovel})
            else:
                mensagem_erro = "Veículo não encontrado."
                return render(request, 'automoveis/consultar_veiculo.html', {'mensagem_erro': mensagem_erro})
        else:
            mensagem_erro = "Por favor, insira o código FIPE."
            return render(request, 'automoveis/consultar_veiculo.html', {'mensagem_erro': mensagem_erro})
    else:
        return render(request, 'automoveis/consultar_veiculo.html')
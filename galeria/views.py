from django.shortcuts import redirect, render
from .models import Atividade
from .forms import AtividadeForm 


def index(request):
    dados = {
    1: {'nome': 'Dev Ops',
        'legenda': 'BDO/SEM5'},
    2: {'nome': 'Redes',
        'legenda': 'RDS/SEM4'}
}
    return render(request, 'galeria/index.html', {"cards" : dados})


def imagem(request):
    return render(request, 'galeria/imagem.html')

def novaAtividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()  # Isso irá salvar os dados do formulário na tabela Atividade
            return redirect('url_para_sua_view')  # Redireciona para a página desejada após o envio do formulário
    else:
        form = AtividadeForm()
    return render(request, 'galeria/novaAtividade.html', {'form': form})
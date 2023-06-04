from django.shortcuts import render
from .models import locacao, filme




def index(request):
    return render(request, 'locadora/index.html')

def lista_locacao(request):
    lista = locacao.objects.all()
    context={'locacoes': lista}
    return render(request,'locadora/lista_locacao.html',context)

def lista_filmes(request):
    lista = filme.objects.all()
    context={'filmes': lista}
    return render(request,'locadora/lista_filmes.html',context)
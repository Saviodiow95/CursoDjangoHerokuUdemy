from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})

@login_required
def nova(request):
    form = PessoaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('pessoa_listar')
    else:
        return render(request, 'pessoaForm.html', {'form': form})
@login_required
def atualizar(request, id):
    pessoa = get_object_or_404(Pessoa, pk = id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance = pessoa)

    if form.is_valid():
        form.save()
        return redirect('pessoa_listar')
    else:
        return render(request, 'pessoaForm.html', {'form': form})
@login_required
def deletar(request,id):
    pessoa = get_object_or_404(Pessoa, pk = id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

    if(request.method == 'POST'):
        pessoa.delete()
        return redirect('pessoa_listar')
    else:
        return render(request, 'pessoaDelete.html', {'form': form})
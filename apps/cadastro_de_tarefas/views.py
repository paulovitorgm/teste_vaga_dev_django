from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import resolve

from apps.cadastro_de_tarefas.forms import TarefasForm
from apps.cadastro_de_tarefas.models import TarefasModel


def cadastrar_tarefa(request):
    form = TarefasForm()
    if request.method == 'POST':
        form = TarefasForm(request.POST)
        if form.is_valid():
            try:
                tarefa = TarefasModel.objects.create(
                    responsavel=form.cleaned_data.get('responsavel'),
                    descricao=form.cleaned_data.get('descricao'),
                )
                messages.success(request, f'A tarefa "{tarefa}" foi criada.')
                return redirect('tarefas')
            except IntegrityError:
                messages.error(
                    request,
                    'Não foi possível cadastrar a tarefa.'
                    ' Por favor contate o suporte.',
                )
                return redirect('tarefas')
        else:
            messages.error(request, 'Não foi possível cadastrar a tarefa.')
    url_name = resolve(request.path_info).url_name
    contexto = {'form': form, 'url_name': url_name}
    return render(request, 'cadastro_de_tarefas/cadastrar_tarefa.html', contexto)


def visualizar_lista_de_tarefas(request):
    lista = TarefasModel.objects.all()
    mensagem = 'Ainda não há tarefas registradas' if not lista.exists() else None
    contexto = {
        'lista': lista,
        'mensagem': mensagem,
    }
    return render(request, 'cadastro_de_tarefas/lista_de_tarefas.html', contexto)


def visualizar_tarefa(request, tarefa_id):
    lista = TarefasModel.objects.filter(pk=tarefa_id)
    mensagem = 'Tarefa não encontrada'
    contexto = {'lista': lista, 'mensagem': mensagem}
    return render(request, 'cadastro_de_tarefas/lista_de_tarefas.html', contexto)

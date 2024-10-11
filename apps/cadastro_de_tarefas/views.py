from django.contrib import messages
from django.shortcuts import redirect, render
from django.db import IntegrityError
from apps.cadastro_de_tarefas.forms import TarefasForm
from apps.cadastro_de_tarefas.models import TarefasModel


def form_tarefas(request):
    form = TarefasForm()
    if request.method == 'POST':
        form = TarefasForm(request.POST)
        if form.is_valid():
            try:
                tarefa = TarefasModel.objects.create(
                    responsavel=request.POST.get('responsavel'),
                    descricao=request.POST.get('descricao'),
                )
                messages.success(request, f'A tarefa "{tarefa}" foi criada.')
                return redirect('tarefas')
            except IntegrityError:
                messages.error(request, 'Não foi possível cadastrar a tarefa. Por favor contate o suporte.')
                return redirect('tarefas')
        else:
            messages.error(request, 'Não foi possível cadastrar a tarefa.')
    contexto = {'form': form}
    return render(request, 'cadastro_de_tarefas/cadastrar_tarefa.html', contexto)


def visualizar_lista_de_tarefas(request):
    lista = TarefasModel.objects.all()
    mensagem = 'Ainda não há tarefas registradas' if not lista.exists() else None
    contexto = {'lista': lista, 'mensagem': mensagem}
    return render(request, 'cadastro_de_tarefas/lista_de_tarefas.html', contexto)

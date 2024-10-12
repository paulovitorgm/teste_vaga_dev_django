from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import resolve

from apps.cadastro_de_tarefas.models import TarefasModel
from apps.tempo_de_trabalho.forms import TempoDeTrabalhoForm
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


def cadastrar_tempo_de_trabalho(request):
    form = TempoDeTrabalhoForm()
    url_name = resolve(request.path_info).url_name
    if request.method == "POST":
        form = TempoDeTrabalhoForm(request.POST)
        if form.is_valid():
            tarefa = form.cleaned_data.get('tarefa')
            tempo_de_trabalho = TempoDeTrabalhoModel.objects.create(
                tempo_trabalhado=form.cleaned_data.get('tempo_trabalhado'),
                descricao_trab_realizado=form.cleaned_data.get('descricao_trab_realizado'),
                tarefa_id=tarefa.id,
            )
            messages.success(request, 'Tempo de trabalho cadastrado com sucesso.')
        else:
            messages.error(request, 'Tempo de trabalho não cadastrado. Contate o suporte.')
        return redirect('cadastrar_tempo')
    contexto = {'form': form, 'url_name': url_name}
    return render(
        request, 'tempo_de_trabalho/cadastrar_tempo_de_trabalho.html', contexto
    )


def listar_tempo_de_trabalho(request):
    lista = TempoDeTrabalhoModel.objects.all()
    mensagem = 'Ainda não registro de tempo.' if not lista.exists() else None

    contexto = {
        'lista': lista,
        'mensagem': mensagem
    }
    return render(request, 'tempo_de_trabalho/lista_tempo_trabalhado.html', contexto)
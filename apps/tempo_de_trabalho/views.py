from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import resolve

from apps.cadastro_de_tarefas.apps import CadastroDeTarefasConfig
from apps.cadastro_de_tarefas.models import TarefasModel
from apps.tempo_de_trabalho.forms import TempoDeTrabalhoForm
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


def cadastrar_tempo_de_trabalho(request):
    form = TempoDeTrabalhoForm()
    url_name = resolve(request.path_info).url_name

    if request.method == "POST":
        print(request.POST.get('descricao'))
        print(request.POST.get('tempo_trabalhado'))
        print(TarefasModel.objects.get(id=1).id)
        if form.is_valid():

            tempo_de_trabalho = TempoDeTrabalhoModel.objects.create(
                tempo_trabalhado=request.POST.get('tempo_trabalhado'),
                descricao_do_trabalho_realizado=request.POST.get('descricao'),
                tarefa_id=TarefasModel.objects.get(id=1).id,
            )
            messages.success(request, 'Tempo de trabalho cadastrado com sucesso.')
        else:
            form = TempoDeTrabalhoForm()
            messages.error(request, 'Tempo de trabalho não cadastrado. Contate o suporte.')
        return redirect('cadastrar_tempo')
    contexto = {'form': form, 'url_name': url_name}
    return render(
        request, 'tempo_de_trabalho/cadastrar_tempo_de_trabalho.html', contexto
    )

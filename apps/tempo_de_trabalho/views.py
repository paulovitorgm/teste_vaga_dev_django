from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import resolve

from apps.tempo_de_trabalho.filters import TempoDeTrabalhoFilter
from apps.tempo_de_trabalho.forms.cadastrar_tempo_forms import TempoDeTrabalhoForm
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


def cadastrar_tempo_de_trabalho(request):
    form = TempoDeTrabalhoForm()
    url_name = resolve(request.path_info).url_name
    if request.method == 'POST':
        form = TempoDeTrabalhoForm(request.POST)
        if form.is_valid():
            tarefa = form.cleaned_data.get('tarefa')
            tempo_de_trabalho = TempoDeTrabalhoModel.objects.create(  # noqa: F841
                tempo_trabalhado=form.cleaned_data.get('tempo_trabalhado'),
                descricao_trab_realizado=form.cleaned_data.get(
                    'descricao_trab_realizado'
                ),
                tarefa_id=tarefa.id,
            )
            messages.success(request, 'Tempo de trabalho cadastrado com sucesso.')
        else:
            messages.error(
                request, 'Tempo de trabalho não cadastrado. Contate o suporte.'
            )
        return redirect('cadastrar_tempo')
    contexto = {'form': form, 'url_name': url_name}
    return render(
        request, 'tempo_de_trabalho/cadastrar_tempo_de_trabalho.html', contexto
    )


def listar_tempo_de_trabalho(request):
    query = TempoDeTrabalhoModel.objects.all()
    filtro = TempoDeTrabalhoFilter(request.GET, queryset=query)
    mensagem = 'Não foram encontrados registros.'
    contexto = {'mensagem': mensagem, 'filtro': filtro}
    return render(request, 'tempo_de_trabalho/lista_tempo_trabalhado.html', contexto)

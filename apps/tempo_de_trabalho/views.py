from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import resolve

from apps.tempo_de_trabalho.forms.cadastrar_tempo_forms import TempoDeTrabalhoForm
from apps.tempo_de_trabalho.forms.filtro_form import FiltroForm
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


def cadastrar_tempo_de_trabalho(request):
    form = TempoDeTrabalhoForm()
    url_name = resolve(request.path_info).url_name
    if request.method == 'POST':
        form = TempoDeTrabalhoForm(request.POST)
        if form.is_valid():
            tarefa = form.cleaned_data.get('tarefa')
            tempo_de_trabalho = TempoDeTrabalhoModel.objects.create(  # noqa: F841
                tempo_trabalhado=form.cleaned_data.get(
                    'tempo_trabalhado'
                ),
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
    lista = TempoDeTrabalhoModel.objects.all()
    mensagem = 'Ainda não registro de tempo.' if not lista.exists() else None

    contexto = {'lista': lista, 'mensagem': mensagem}
    return render(request, 'tempo_de_trabalho/lista_tempo_trabalhado.html', contexto)


def filtrar_tempo(request):
    form = FiltroForm()
    url_name = resolve(request.path_info).url_name
    contexto = {'form': form, 'url_name': url_name}

    if request.method == 'POST':
        form = FiltroForm(request.POST)

        if form.is_valid():
            resultado = busca(request, form)
            mensagem = 'Nenhum resultado foi encontrado. Tente novamente.'
            contexto = {'resultado': resultado, 'mensagem': mensagem}
            return render(request,
                              'tempo_de_trabalho/lista_tempo_trabalhado_filtrada.html',
                              contexto)

    return render(
        request,
'tempo_de_trabalho/filtrar_tempo.html',
        contexto)


def busca(request, form):
    objeto = TempoDeTrabalhoModel.objects
    resultado = None
    if request.POST.get('tarefa'):
        tarefa = form.cleaned_data.get('tarefa')
        resultado = objeto.filter(
            tarefa_id=tarefa
        )
    elif request.POST.get('tempo_trabalhado'):
        tempo = form.cleaned_data.get('tempo_trabalhado')
        resultado = objeto.filter(
            tempo_trabalhado__hour__lte=tempo.hour,
            tempo_trabalhado__hour__gte=tempo.hour
        )
    elif request.POST.get('descricao_trab_realizado'):
        descricao = form.cleaned_data.get('descricao_trab_realizado')
        resultado = objeto.filter(
            descricao_trab_realizado__icontains=descricao
        )
    elif request.POST.get('data_inicial') and request.POST.get('data_final'):
        data_inicial = form.cleaned_data.get('data_inicial')
        data_final = form.cleaned_data.get('data_final')
        resultado = objeto.filter(
            data_do_registro__range=[data_inicial, data_final + timedelta(1)])
    return resultado


def listar_tempo_filtrado(request):
    contexto = TempoDeTrabalhoModel

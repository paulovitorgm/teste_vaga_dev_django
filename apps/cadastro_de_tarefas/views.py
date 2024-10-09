from django.shortcuts import render

from apps.cadastro_de_tarefas.forms import TarefasForm


def form_tarefas(request):
    form = TarefasForm()
    return render(request, 'index.html', {'form': form})


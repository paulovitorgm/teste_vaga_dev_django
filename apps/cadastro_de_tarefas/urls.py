from django.urls import path

from apps.cadastro_de_tarefas.views import (
    form_tarefas,
    visualizar_lista_de_tarefas,
)

urlpatterns = [
    path('', form_tarefas, name='tarefas'),
    path('lista/', visualizar_lista_de_tarefas, name='lista'),
]

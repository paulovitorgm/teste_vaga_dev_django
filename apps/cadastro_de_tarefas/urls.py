from django.urls import path

from apps.cadastro_de_tarefas.views import (
    cadastrar_tarefa,
    visualizar_lista_de_tarefas,
    visualizar_tarefa,
)

urlpatterns = [
    path('criar/', cadastrar_tarefa, name='tarefas'),
    path('lista/', visualizar_lista_de_tarefas, name='lista'),
    path('lista/<int:tarefa_id>/', visualizar_tarefa, name='tarefa'),
]

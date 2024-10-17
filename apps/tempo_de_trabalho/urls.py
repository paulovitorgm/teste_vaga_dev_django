from django.urls import path

from apps.tempo_de_trabalho.views import (
    cadastrar_tempo_de_trabalho,
    listar_tempo_de_trabalho,
)

urlpatterns = [
    path('cadastrar/', cadastrar_tempo_de_trabalho, name='cadastrar_tempo'),
    path('lista/', listar_tempo_de_trabalho, name='listar_tempo'),
]

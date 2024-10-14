from django.urls import path

from apps.tempo_de_trabalho.views import (
    cadastrar_tempo_de_trabalho,
    filtrar_tempo,
    listar_tempo_de_trabalho,
)

urlpatterns = [
    path('', cadastrar_tempo_de_trabalho, name='cadastrar_tempo'),
    path('lista/', listar_tempo_de_trabalho, name='listar_tempo'),
    path('filtrar/', filtrar_tempo, name='filtrar_tempo'),
    path('resultado/', filtrar_tempo, name='resultado'),
]

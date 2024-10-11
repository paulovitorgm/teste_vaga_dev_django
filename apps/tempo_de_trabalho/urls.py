from django.urls import path

from apps.tempo_de_trabalho.views import cadastrar_tempo_de_trabalho

urlpatterns = [
    path('', cadastrar_tempo_de_trabalho, name='cadastrar_tempo')


]

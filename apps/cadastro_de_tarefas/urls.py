from django.urls import path

from apps.cadastro_de_tarefas.views import form_tarefas

urlpatterns = [
    path('/', form_tarefas, name='tarefas')
]
from django.contrib import admin
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


class TempoDeTrabalhoAdmin(admin.ModelAdmin):
    list_display = [
        'descricao_trab_realizado',
        'tarefa',
        'data_do_registro',
        'tempo_trabalhado',
    ]
    list_display_links = [
        'data_do_registro',
        'tempo_trabalhado',
        'descricao_trab_realizado',
        'tarefa'
    ]
    list_per_page = 10
    search_fields = [
        'descricao_trab_realizado'
    ]



admin.site.register(TempoDeTrabalhoModel, TempoDeTrabalhoAdmin)

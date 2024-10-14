from django.contrib import admin

from apps.cadastro_de_tarefas.models import TarefasModel


class TarefasAdmin(admin.ModelAdmin):
    list_display = ['responsavel', 'data_criacao', 'descricao']
    list_display_links = ['responsavel', 'data_criacao', 'descricao']
    list_per_page = 10
    search_fields = ['responsavel']


admin.site.register(TarefasModel, TarefasAdmin)

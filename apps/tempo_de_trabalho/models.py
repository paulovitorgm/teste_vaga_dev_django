from django.db import models
from django.db.models.functions import Now

from apps.cadastro_de_tarefas.models import TarefasModel


class TempoDeTrabalhoModel(models.Model):
    data_do_registro = models.DateField(db_column='data_do_registro', db_default=Now())
    tempo_trabalhado_minutos = models.IntegerField(db_column='tempo_de_trabalho_em_minutos')
    descricao_trab_realizado = models.TextField(db_column='descricao_do_trabalho_realizado',
                                                blank=False, max_length=360)
    tarefa = models.ForeignKey(TarefasModel, on_delete=models.CASCADE)

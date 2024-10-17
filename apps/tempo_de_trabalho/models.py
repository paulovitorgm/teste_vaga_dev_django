from django.db import models
from django.db.models.functions import Now

from apps.cadastro_de_tarefas.models import TarefasModel


class TempoDeTrabalhoModel(models.Model):
    data_do_registro = models.DateTimeField(
        db_column='data_do_registro', db_default=Now()
    )

    tempo_trabalhado = models.TimeField(db_column='tempo_trabalhado')

    descricao_trab_realizado = models.TextField(
        db_column='descricao_do_trabalho_realizado',
        blank=False,
        max_length=360,
    )

    tarefa = models.ForeignKey(TarefasModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

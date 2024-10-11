from django.db import models
from django.db.models.functions import Now


class TarefasModel(models.Model):
    responsavel = models.CharField(
        db_column='responsavel',
        max_length=60,
        blank=False,
        null=False,
    )

    data_criacao = models.DateTimeField(
        db_column='data_de_criacao',
        null=False,
        unique=False,
        db_default=Now()
    )

    descricao = models.TextField(
        db_column='descricao', max_length=360, blank=False
    )

    def __str__(self):
        return self.descricao

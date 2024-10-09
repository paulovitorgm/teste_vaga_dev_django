from django.db import models
from django.db.models.functions import Now


class TarefasModel(models.Model):
    nome_usuario = models.CharField(db_column='nome_de_usuario', max_length=60, 
                                    blank=False, null=False, unique=True)
    data_criacao = models.DateField(db_column='data_de_criacao', null=False, unique=False,
                                    db_default=Now())
    descricao = models.TextField(db_column='descricao', max_length=360, blank=False)

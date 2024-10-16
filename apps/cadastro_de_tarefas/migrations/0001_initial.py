# Generated by Django 5.1.2 on 2024-10-10 16:50

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TarefasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(db_column='nome_de_usuario', max_length=60, unique=True)),
                ('data_criacao', models.DateField(db_column='data_de_criacao', db_default=django.db.models.functions.datetime.Now())),
                ('descricao', models.TextField(db_column='descricao', max_length=360)),
            ],
        ),
    ]

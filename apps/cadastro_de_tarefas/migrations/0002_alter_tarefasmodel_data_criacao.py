# Generated by Django 5.1.2 on 2024-10-10 17:48

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_de_tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefasmodel',
            name='data_criacao',
            field=models.DateTimeField(db_column='data_de_criacao', db_default=django.db.models.functions.datetime.Now()),
        ),
    ]

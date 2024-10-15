from datetime import datetime
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from apps.cadastro_de_tarefas.models import TarefasModel
from apps.tempo_de_trabalho.forms.cadastrar_tempo_forms import TempoDeTrabalhoForm
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


class TestTempoDeTrabalhoModel(TestCase):
    def setUp(self):
        self.tarefa = TarefasModel.objects.create(
            responsavel='José', descricao='Tarefa'
        )
        self.tempo_de_trabalho = TempoDeTrabalhoModel.objects.create(
            tempo_trabalhado=datetime.strptime('2:30', '%H:%M').time(),
            descricao_trab_realizado='Trabalho',
            tarefa=self.tarefa,
        )

    def test_criar_tempo_de_trabalho(self):
        objeto = TempoDeTrabalhoModel.objects.get(pk=1)
        self.assertEqual(
            self.tempo_de_trabalho.tempo_trabalhado, objeto.tempo_trabalhado
        )
        self.assertEqual(
            self.tempo_de_trabalho.descricao_trab_realizado,
            objeto.descricao_trab_realizado,
        )
        self.assertEqual(self.tempo_de_trabalho.tarefa, objeto.tarefa)


class TestTempoDeTrabalhoForm(TestCase):
    def setUp(self):
        self.tarefa = TarefasModel.objects.create(
            responsavel='José', descricao='Tarefa'
        )

    def test_se_formulario_e_valido(self):
        form = TempoDeTrabalhoForm(
            data={
                'tempo_trabalhado': datetime.strptime('2:30', '%H:%M').time(),
                'descricao_trab_realizado': 'Trabalho',
                'tarefa': self.tarefa,
            }
        )
        self.assertTrue(form.is_valid())

    def test_se_formulario_e_invalido_passando_tempo_incompleto(self):
        form = TempoDeTrabalhoForm(
            data={
                'tempo_trabalhado': '12',
                'descricao_trab_realizado': 'Trabalho',
                'tarefa': self.tarefa,
            }
        )
        self.assertFalse(form.is_valid())

    def test_se_formulario_e_invalido_passando_tempo_vazio(self):
        form = TempoDeTrabalhoForm(
            data={
                'tempo_trabalhado': '',
                'descricao_trab_realizado': 'Trabalho',
                'tarefa': self.tarefa,
            }
        )
        self.assertFalse(form.is_valid())

    def test_se_formulario_e_invalido_passando_descricao_vazia(self):
        form = TempoDeTrabalhoForm(
            data={
                'tempo_trabalhado': '12:00',
                'descricao_trab_realizado': '',
                'tarefa': self.tarefa,
            }
        )
        self.assertFalse(form.is_valid())

    def test_se_formulario_e_valido_passando_tafera_id_e_nao_instancia(self):
        form = TempoDeTrabalhoForm(
            data={
                'tempo_trabalhado': '12:00',
                'descricao_trab_realizado': 'Trabalho',
                'tarefa': self.tarefa.pk,
            }
        )
        self.assertTrue(form.is_valid())


class TestFiltro(TestCase):
    def setUp(self):
        self.tarefa = TarefasModel.objects.create(
            responsavel='Alexandre', descricao='Trabalho'
        )
        self.tarefa1 = TarefasModel.objects.create(
            responsavel='José', descricao='Descrição'
        )
        self.tarefa2 = TarefasModel.objects.create(
            responsavel='Tiago', descricao='Trabalho 2'
        )

        self.tempo_de_trabalho = TempoDeTrabalhoModel.objects.create(
            tempo_trabalhado=datetime.strptime('2:30', '%H:%M').time(),
            descricao_trab_realizado='Trabalho',
            tarefa=self.tarefa,
        )
        self.tempo_de_trabalho = TempoDeTrabalhoModel.objects.create(
            tempo_trabalhado=datetime.strptime('7:30', '%H:%M').time(),
            descricao_trab_realizado='Descrição',
            tarefa=self.tarefa1,
        )
        self.tempo_de_trabalho = TempoDeTrabalhoModel.objects.create(
            tempo_trabalhado=datetime.strptime('4:30', '%H:%M').time(),
            descricao_trab_realizado='Trabalho 2',
            tarefa=self.tarefa2,
        )

    def test_listar_tempo(self):
        response = self.client.get(reverse('listar_tempo'))
        consulta = TempoDeTrabalhoModel.objects.all()
        self.assertListEqual(
            [self.tarefa, self.tarefa1, self.tarefa2],
            [consulta[0], consulta[1], consulta[2]],
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_filtrar_tempo_por_tempo_trabalhado(self):
        """Deve retornar apenas 2 objetos do banco na consulta."""
        response = self.client.get(reverse('filtrar_tempo'))
        consulta = TempoDeTrabalhoModel.objects.filter(tempo_trabalhado__hour=4)
        self.assertEqual(len(consulta), 1)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_filtrar_tempo_por_tarefa(self):
        """Deve retornar apenas 1 objeto do banco na consulta."""
        response = self.client.get(reverse('filtrar_tempo'))
        consulta = TempoDeTrabalhoModel.objects.filter(
            descricao_trab_realizado__icontains='Trabalho'
        )
        self.assertEqual(len(consulta), 2)
        self.assertEqual(response.status_code, HTTPStatus.OK)

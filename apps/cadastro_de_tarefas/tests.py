# from http import HTTPStatus

from django.test import TestCase

# from django.urls import reverse
from apps.cadastro_de_tarefas.forms import TarefasForm
from apps.cadastro_de_tarefas.models import TarefasModel


class TestTarefasModel(TestCase):
    def setUp(self):
        self.tarefa = TarefasModel.objects.create(responsavel='José', descricao='Tarefa')

    def test_criar_tarefa(self):
        objeto = TarefasModel.objects.get(pk=self.tarefa.pk)
        self.assertEqual(self.tarefa.responsavel, objeto.responsavel)
        self.assertEqual(self.tarefa.descricao, objeto.descricao)


class TestTarefasForm(TestCase):
    def setUp(self):
        self.tarefa = TarefasModel.objects.create(responsavel='José', descricao='Tarefa')
        self.tarefa1 = TarefasModel.objects.create(responsavel='João', descricao='Tarefa 1')
        self.form = TarefasForm(data={'responsavel': 'José', 'descricao': 'Tarefa'})

    def test_se_formulario_e_valido(self):
        self.assertTrue(self.form.is_valid())

    def test_se_formulario_e_invalido_passando_responsavel_numerico(self):
        form = TarefasForm(data={'responsavel': '123456', 'descricao': 'Tarefa'})
        self.assertFalse(form.is_valid())

    def test_se_formulario_e_invalido_passando_responsavel_vazio(self):
        form = TarefasForm(data={'responsavel': '', 'descricao': 'Tarefa'})
        self.assertFalse(form.is_valid())

    def test_se_formulario_e_invalido_passando_descricao_vazia(self):
        form = TarefasForm(data={'responsavel': 'José', 'descricao': ''})
        self.assertFalse(form.is_valid())


class TestListaTarefa(TestCase):
    def setUp(self):
        self.tarefa = TarefasModel.objects.create(
            responsavel='José',
            descricao='Tarefa'
        )
        self.tarefa1 = TarefasModel.objects.create(
            responsavel='João',
            descricao='Tarefa 1'
        )
    #
    # def test_listar_tarefas(self):
    #     response = self.client.get(reverse('lista'))
    #     consulta = TarefasModel.objects.all()
    #
    #
    #     self.assertEqual(len(consulta), 2)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)

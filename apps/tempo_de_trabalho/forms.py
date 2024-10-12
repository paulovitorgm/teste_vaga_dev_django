from django import forms
from django.core.exceptions import ValidationError
from django.forms import TimeField

from apps.cadastro_de_tarefas.models import TarefasModel
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel



class TempoDeTrabalhoForm(forms.ModelForm):
    tarefa = forms.ModelChoiceField(
        queryset=TarefasModel.objects.all(),
        label='Tarefa',
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        error_messages={'invalid_choice': 'A tarefa selecionada é inválida.',
                        'required': 'Escolha uma tarefa.'}
    )

    tempo_trabalhado = forms.TimeField(
        label='Tempo de trabalho',
        required=True,
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'autocomplete': 'off',
                'class': 'form-control',
            },
        ),
        input_formats=['%H:%M'],
        error_messages={'invalid': 'Insira o tempo em formato HH:MM.',
                        'required': 'O campo é obrigatório'},
    )

    descricao_trab_realizado = forms.CharField(
        strip=True,
        required=True,
        label='Descrição',
        max_length=360,
        widget=forms.Textarea(
            attrs={'rows': 4, 'autocomplete': 'off', 'class': 'form-control'}
        ),
        error_messages={'required': 'O campo é obrigatório'}
    )

    class Meta:
        model = TempoDeTrabalhoModel
        fields = ['tarefa', 'tempo_trabalhado', 'descricao_trab_realizado']

    def clean_tarefa(self):
        id_tarefa = self.cleaned_data['tarefa']
        # if id_tarefa and not TarefasModel.objects.filter(pk=id_tarefa).exists():
        if id_tarefa is None:
            raise forms.ValidationError('A tarefa selecionada não existe.')
        return id_tarefa

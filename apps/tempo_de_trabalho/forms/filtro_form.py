from django import forms

from apps.cadastro_de_tarefas.models import TarefasModel
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


class FiltroForm(forms.Form):
    tarefa = forms.ModelChoiceField(
        queryset=TarefasModel.objects.all(),
        label='Tarefa',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={
            'invalid_choice': 'A tarefa selecionada é inválida.',
        },
    )

    tempo_trabalhado = forms.TimeField(
        label='Tempo de trabalho',
        required=False,
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'autocomplete': 'off',
                'class': 'form-control',
            },
        ),
        error_messages={
            'invalid': 'Insira o tempo em formato HH:MM.',
        },
    )

    descricao_trab_realizado = forms.CharField(
        strip=True,
        required=False,
        label='Descrição',
        max_length=360,
        widget=forms.Textarea(
            attrs={'rows': 4, 'autocomplete': 'off', 'class': 'form-control'}
        ),
    )

    data_inicial = forms.DateField(
        label='Data inicial',
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
    )

    data_final = forms.DateField(
        label='Data final',
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
    )

    class Meta:
        model = TempoDeTrabalhoModel
        fields = '__all__'
        exclude = [
            'data_do_registro',
        ]

    def clean(self):
        cleaned_data = super().clean()
        data_inicial = self.cleaned_data.get('data_inicial')
        data_final = self.cleaned_data.get('data_final')

        if data_inicial and not data_final:
            raise forms.ValidationError(
                'Quando existe data inicial a data final torna-se obrigatória'
            )
        if not data_inicial and data_final:
            raise forms.ValidationError(
                'Quando existe data final a data inicial torna-se obrigatória'
            )
        if (data_inicial and data_final) and (data_final < data_inicial):
            raise forms.ValidationError(
                'A data final precisa ser maior ou igual à data inicial.'
            )

        return cleaned_data

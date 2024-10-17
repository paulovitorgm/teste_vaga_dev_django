import django_filters
from django import forms

from apps.cadastro_de_tarefas.models import TarefasModel
from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


class TempoDeTrabalhoFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(
        label='Id',
        lookup_expr='exact',
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        ),

    )

    data_do_registro = django_filters.DateFilter(
        label='Data do registro',
        lookup_expr='exact',
        widget=forms.DateInput(
            attrs={'class': 'form-control',
                   'type': 'date'
                   }
        )
    )

    tempo_trabalhado = django_filters.TimeFilter(
        label='Tempo trabalhado',
        lookup_expr='exact',
        widget=forms.TimeInput(
            attrs={'class': 'form-control',
                   'type': 'time'}
        )
    )

    descricao_trab_realizado = django_filters.CharFilter(
        label='Descrição',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    tarefa = django_filters.ModelChoiceFilter(
        label='Tarefa',
        queryset=TarefasModel.objects.all(),
        lookup_expr='exact',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = TempoDeTrabalhoModel
        fields = [
            'id',
            'data_do_registro',
            'tempo_trabalhado',
            'descricao_trab_realizado',
            'tarefa'
        ]

    def filter_tempo_trabalhado(self, queryset, name, value):
        if value:
            return queryset.filter(tempo_trabalhado__hour=value.hour)
        return queryset

    def filter_data_do_registro(self, queryset, name, value):
        if value:
            return queryset.filter(data_do_registro__date=value)
        return queryset

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['tempo_trabalhado'].method = self.filter_tempo_trabalhado
        self.filters['data_do_registro'].method = self.filter_data_do_registro

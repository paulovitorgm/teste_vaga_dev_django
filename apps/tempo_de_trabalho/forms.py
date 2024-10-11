from django import forms

from apps.tempo_de_trabalho.models import TempoDeTrabalhoModel


class TempoDeTrabalhoForm(forms.Form):
    tempo_trabalhado = forms.TimeField(

        label='Tempo de trabalho',
        required=True,
        widget=forms.TimeInput(
            format='%H:%M',
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

    descricao = forms.CharField(
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
        fields = '__all__'

    def clean_tempo_trabalhado(self):
        tempo = self.cleaned_data.get('tempo_trabalhado')
        tempo = tempo[0](tempo.split())
        return tempo

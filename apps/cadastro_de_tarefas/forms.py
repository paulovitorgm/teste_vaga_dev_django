import re

from django import forms

from apps.tempo_de_trabalho.models import TarefasModel


class TarefasForm(forms.ModelForm):
    responsavel = forms.CharField(
        label='Responsável',
        max_length=75,
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={'autocomplete': 'off', 'class': 'form-control'}
        ),
        error_messages={'required': 'O campo é obrigatório'},
    )

    descricao = forms.CharField(
        label='Descrição',
        required=True,
        max_length=360,
        widget=forms.Textarea(
            attrs={'rows': 4, 'autocomplete': 'off', 'class': 'form-control'}
        ),
        error_messages={'required': 'O campo é obrigatório'},
    )

    class Meta:
        model = TarefasModel
        fields = ['responsavel', 'descricao']

    def clean_responsavel(self):
        responsavel = self.cleaned_data.get('responsavel').strip()
        if not re.match(r'^[A-Za-z\s]+$', responsavel):
            raise forms.ValidationError(
                'O nome do responsável deve conter apenas letras e espaços.'
            )
        return responsavel

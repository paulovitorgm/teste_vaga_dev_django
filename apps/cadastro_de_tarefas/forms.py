import re

from django import forms

from .models import TarefasModel


class TarefasForm(forms.Form):
    responsavel = forms.CharField(
        label='Responsável',
        max_length=75,
        strip=True,
        widget=forms.TextInput(
            attrs={'autocomplete': 'off', 'class': 'form-control'}
        ),
    )

    descricao = forms.CharField(
        label='Descrição',
        max_length=360,
        widget=forms.Textarea(
            attrs={'rows': 4, 'autocomplete': 'off', 'class': 'form-control'}
        ),
    )

    class Meta:
        model = TarefasModel
        fields = '__all__'

    def clean_responsavel(self):
        responsavel = self.cleaned_data.get('responsavel').strip()
        if not re.match(r'^[A-Za-z\s]+$', responsavel):
            raise forms.ValidationError(
                'O nome do responsável deve conter apenas letras e espaços.'
            )
        return responsavel

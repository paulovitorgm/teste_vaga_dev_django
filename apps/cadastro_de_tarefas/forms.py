from django import forms

from .models import TarefasModel


class TarefasForm(forms.Form):
    nome_usuario = forms.CharField()
    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = TarefasModel
        fields = '__all__'



from django import forms
from .models import Profissional


class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = [
            'nome',
            'telefone',
            'orgao_regulador',
            'registro',
            'especialidade',
            'endereco',
            'cpf',
            'ativo',
        ]

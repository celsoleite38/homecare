from django import forms
from .models import Paciente, Responsavel


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nome',
            'idade',
            'cpf',
            'data_nascimento',
            'endereco',
            'telefone',
            'quadro_medico',
            'plano_saude',
            'profissionais_autorizados',
        ]
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'profissionais_autorizados': forms.CheckboxSelectMultiple(),
        }

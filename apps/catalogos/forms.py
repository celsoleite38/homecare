from django import forms

from .models import Exame, Especialidade, PlanoSaude, ProcedimentoClinico


class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome', 'descricao']


class PlanoSaudeForm(forms.ModelForm):
    class Meta:
        model = PlanoSaude
        fields = ['nome', 'operadora', 'descricao']


class ProcedimentoClinicoForm(forms.ModelForm):
    class Meta:
        model = ProcedimentoClinico
        fields = ['nome', 'descricao', 'duracao_padrao_minutos']


class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['nome', 'descricao']

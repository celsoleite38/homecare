from django import forms
from .models import Agendamento, ReceitaMedica, PedidoExame, IntervaloRepeticao


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = [
            'paciente',
            'profissional',
            'procedimento',
            'tipo_plantao',
            'data_hora_inicio',
            'duracao_minutos',
            'repetir',
            'intervalo_repeticao',
            'data_fim_repeticao',
            'observacoes',
        ]
        widgets = {
            'data_hora_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_fim_repeticao': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None and user.homecare is not None:
            self.fields['intervalo_repeticao'].queryset = IntervaloRepeticao.objects.filter(homecare=user.homecare)
        else:
            self.fields['intervalo_repeticao'].queryset = IntervaloRepeticao.objects.none()


class ReceitaMedicaForm(forms.ModelForm):
    class Meta:
        model = ReceitaMedica
        fields = [
            'paciente',
            'profissional',
            'descricao',
            'validade',
        ]
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }


class PedidoExameForm(forms.ModelForm):
    class Meta:
        model = PedidoExame
        fields = [
            'paciente',
            'profissional',
            'exame',
            'observacoes',
        ]

from django.contrib import admin
from .models import Agendamento, ReceitaMedica, PedidoExame, IntervaloRepeticao


@admin.register(IntervaloRepeticao)
class IntervaloRepeticaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dias', 'homecare')
    list_filter = ('homecare',)
    search_fields = ('nome',)


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'profissional', 'procedimento', 'tipo_plantao', 'data_hora_inicio', 'repetir', 'intervalo_repeticao']
    search_fields = ['paciente__nome', 'profissional__nome', 'procedimento__nome']
    list_filter = ['tipo_plantao', 'procedimento', 'repetir']


@admin.register(ReceitaMedica)
class ReceitaMedicaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'profissional', 'data_emissao', 'validade']
    search_fields = ['paciente__nome', 'profissional__nome']


@admin.register(PedidoExame)
class PedidoExameAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'profissional', 'exame', 'data_solicitacao']
    search_fields = ['paciente__nome', 'profissional__nome', 'exame__nome']

from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta


class IntervaloRepeticao(models.Model):
    homecare = models.ForeignKey(
        'accounts.HomeCare',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='intervalos_repeticao'
    )
    nome = models.CharField('Nome do Intervalo', max_length=100)
    dias = models.PositiveIntegerField('Intervalo em dias', default=1)
    descricao = models.TextField('Descrição', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Intervalo de Repetição'
        verbose_name_plural = 'Intervalos de Repetição'
        ordering = ['dias', 'nome']

    def __str__(self):
        return f"{self.nome} ({self.dias} dia(s))"


class Agendamento(models.Model):
    PLANTAO_CHOICES = [
        ('1h', 'Plantão 1 hora'),
        ('3h', 'Plantão 3 horas'),
        ('6h', 'Plantão 6 horas'),
        ('12h', 'Plantão 12 horas'),
        ('procedimento', 'Procedimento Clínico'),
    ]

    homecare = models.ForeignKey(
        'accounts.HomeCare',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='agendamentos'
    )
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.PROTECT,
        related_name='agendamentos'
    )
    procedimento = models.ForeignKey(
        'catalogos.ProcedimentoClinico',
        on_delete=models.PROTECT,
        related_name='agendamentos'
    )
    tipo_plantao = models.CharField('Tipo de Plantão', max_length=20, choices=PLANTAO_CHOICES, default='procedimento')
    data_hora_inicio = models.DateTimeField('Data e hora de início')
    duracao_minutos = models.PositiveIntegerField('Duração (minutos)', default=60)
    repetir = models.BooleanField('Repetir plantão', default=False)
    intervalo_repeticao = models.ForeignKey(
        IntervaloRepeticao,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Intervalo de repetição'
    )
    data_fim_repeticao = models.DateField('Data fim da repetição', null=True, blank=True,
                                            help_text='Deixe em branco para repetição sem tempo determinado.')
    observacoes = models.TextField('Observações', blank=True)
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='agendamentos_criados'
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['-data_hora_inicio']

    def __str__(self):
        return f"{self.paciente.nome} - {self.profissional.nome} - {self.data_hora_inicio.strftime('%d/%m/%Y %H:%M')}"

    def data_hora_fim(self):
        return self.data_hora_inicio + timedelta(minutes=self.duracao_minutos)

    def clean(self):
        if self.repetir and self.intervalo_repeticao is None:
            raise ValidationError({'intervalo_repeticao': 'É necessário informar o intervalo de repetição.'})
        if self.data_fim_repeticao and self.data_fim_repeticao < self.data_hora_inicio.date():
            raise ValidationError({'data_fim_repeticao': 'A data final deve ser igual ou posterior ao início.'})


class ReceitaMedica(models.Model):
    homecare = models.ForeignKey(
        'accounts.HomeCare',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='receitas'
    )
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='receitas'
    )
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.PROTECT,
        related_name='receitas'
    )
    descricao = models.TextField('Receita Médica')
    data_emissao = models.DateField('Data de Emissão', auto_now_add=True)
    validade = models.DateField('Validade', null=True, blank=True)

    class Meta:
        verbose_name = 'Receita Médica'
        verbose_name_plural = 'Receitas Médicas'

    def __str__(self):
        return f"Receita - {self.paciente.nome} ({self.data_emissao})"


class PedidoExame(models.Model):
    homecare = models.ForeignKey(
        'accounts.HomeCare',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='pedidos_exames'
    )
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='pedidos_exames'
    )
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.PROTECT,
        related_name='pedidos_exames'
    )
    exame = models.ForeignKey(
        'catalogos.Exame',
        on_delete=models.PROTECT,
        related_name='pedidos_exames'
    )
    observacoes = models.TextField('Observações', blank=True)
    data_solicitacao = models.DateField('Data de Solicitação', auto_now_add=True)

    class Meta:
        verbose_name = 'Pedido de Exame'
        verbose_name_plural = 'Pedidos de Exames'

    def __str__(self):
        return f"Exame {self.exame.nome} - {self.paciente.nome}"

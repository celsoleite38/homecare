from django.db import models


class Paciente(models.Model):
    homecare = models.ForeignKey(
        'accounts.HomeCare',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='pacientes'
    )
    nome = models.CharField('Nome', max_length=200)
    idade = models.PositiveIntegerField('Idade')
    cpf = models.CharField('CPF', max_length=14, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    endereco = models.TextField('Endereço')
    telefone = models.CharField('Telefone', max_length=20)
    quadro_medico = models.TextField('Quadro Médico', blank=True)
    plano_saude = models.ForeignKey(
        'catalogos.PlanoSaude',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Plano de Saúde'
    )
    profissionais_autorizados = models.ManyToManyField(
        'profissionais.Profissional',
        blank=True,
        related_name='pacientes_autorizados'
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.nome


class Responsavel(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='responsaveis'
    )
    nome = models.CharField('Nome do Responsável', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)
    recebe_mensagem = models.BooleanField('Recebe mensagem WhatsApp', default=True)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def __str__(self):
        return f"{self.nome} ({self.telefone})"

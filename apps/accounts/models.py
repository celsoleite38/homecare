from django.contrib.auth.models import AbstractUser
from django.db import models


class HomeCare(models.Model):
    nome = models.CharField('Nome do HomeCare', max_length=200, unique=True)
    cnpj = models.CharField('CNPJ', max_length=20, blank=True)
    endereco = models.TextField('Endereço', blank=True)
    telefone_fixo = models.CharField('Telefone fixo', max_length=20, blank=True)
    telefone_celular = models.CharField('Telefone celular', max_length=20, blank=True)
    whatsapp_celular = models.BooleanField('WhatsApp no celular', default=False)
    logo = models.ImageField('Logo', upload_to='homecare_logos/', blank=True, null=True)
    descricao = models.TextField('Descrição', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'HomeCare'
        verbose_name_plural = 'HomeCares'

    def __str__(self):
        return self.nome


class CustomUser(AbstractUser):
    ADMIN_GERAL = 'admin_geral'
    ADMIN_PLANTOES = 'admin_plantao'
    PROFISSIONAL = 'profissional'

    ROLE_CHOICES = [
        (ADMIN_GERAL, 'Administrador Geral'),
        (ADMIN_PLANTOES, 'Administrador de Plantões'),
        (PROFISSIONAL, 'Profissional'),
    ]

    role = models.CharField('Função', max_length=20, choices=ROLE_CHOICES, default=PROFISSIONAL)
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True)
    endereco = models.TextField('Endereço', blank=True)
    orgao_regulador = models.ForeignKey(
        'catalogos.OrgaoRegulador',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Órgão Regulador'
    )
    registro = models.CharField('Registro', max_length=50, blank=True)
    especialidade = models.ForeignKey(
        'catalogos.Especialidade',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    homecare = models.ForeignKey(
        HomeCare,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='usuarios'
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.get_full_name() or self.username

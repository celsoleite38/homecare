from django.conf import settings
from django.db import models


class Profissional(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='profissional_profile'
    )
    homecare = models.ForeignKey(
        'accounts.HomeCare',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='profissionais'
    )
    nome = models.CharField('Nome', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)
    orgao_regulador = models.ForeignKey(
        'catalogos.OrgaoRegulador',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    registro = models.CharField('Registro', max_length=50, blank=True)
    especialidade = models.ForeignKey(
        'catalogos.Especialidade',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    endereco = models.TextField('Endereço', blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

    def __str__(self):
        return self.nome

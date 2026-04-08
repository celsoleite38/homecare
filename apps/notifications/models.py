from django.db import models


class ConfiguracaoSistema(models.Model):
    antecedencia_horas = models.PositiveIntegerField('Antecedência (horas)', default=2)
    antecedencia_minutos = models.PositiveIntegerField('Antecedência (minutos)', default=0)
    enviar_whatsapp = models.BooleanField('Enviar WhatsApp', default=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Configuração de Sistema'
        verbose_name_plural = 'Configurações de Sistema'

    def __str__(self):
        return 'Configuração de Notificações'

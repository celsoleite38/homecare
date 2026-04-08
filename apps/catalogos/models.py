from django.db import models


class OrgaoRegulador(models.Model):
    nome = models.CharField('Órgão Regulador', max_length=150)
    sigla = models.CharField('Sigla', max_length=20, blank=True)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Órgão Regulador'
        verbose_name_plural = 'Órgãos Reguladores'

    def __str__(self):
        return f"{self.nome} ({self.sigla})" if self.sigla else self.nome


class Especialidade(models.Model):
    nome = models.CharField('Especialidade', max_length=150)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nome


class PlanoSaude(models.Model):
    nome = models.CharField('Plano de Saúde', max_length=200)
    operadora = models.CharField('Operadora', max_length=150, blank=True)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Plano de Saúde'
        verbose_name_plural = 'Planos de Saúde'

    def __str__(self):
        return self.nome


class Medicamento(models.Model):
    nome = models.CharField('Medicamento', max_length=200)
    principio_ativo = models.CharField('Princípio Ativo', max_length=200, blank=True)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def __str__(self):
        return self.nome


class ProcedimentoClinico(models.Model):
    nome = models.CharField('Procedimento', max_length=200)
    descricao = models.TextField('Descrição', blank=True)
    duracao_padrao_minutos = models.PositiveIntegerField('Duração padrão (minutos)', default=60)

    class Meta:
        verbose_name = 'Procedimento Clínico'
        verbose_name_plural = 'Procedimentos Clínicos'

    def __str__(self):
        return self.nome


class Exame(models.Model):
    nome = models.CharField('Exame', max_length=200)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return self.nome

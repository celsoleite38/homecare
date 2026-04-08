from django.contrib import admin

from .models import Exame, Especialidade, OrgaoRegulador, PlanoSaude, ProcedimentoClinico, Medicamento


admin.site.register([OrgaoRegulador, Especialidade, PlanoSaude, Medicamento, ProcedimentoClinico, Exame])

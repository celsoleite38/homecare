from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from apps.accounts.models import CustomUser
from .forms import ExameForm, EspecialidadeForm, PlanoSaudeForm, ProcedimentoClinicoForm
from .models import Exame, Especialidade, PlanoSaude, ProcedimentoClinico


class AdministradorCatalogoMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role in (CustomUser.ADMIN_GERAL, CustomUser.ADMIN_PLANTOES)


class CatalogoIndexView(AdministradorCatalogoMixin, TemplateView):
    template_name = 'catalogos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'total_especialidades': Especialidade.objects.count(),
            'total_planos_saude': PlanoSaude.objects.count(),
            'total_procedimentos': ProcedimentoClinico.objects.count(),
            'total_exames': Exame.objects.count(),
        })
        return context


class EspecialidadeListView(AdministradorCatalogoMixin, ListView):
    model = Especialidade
    template_name = 'catalogos/especialidade_list.html'
    context_object_name = 'especialidades'


class EspecialidadeCreateView(AdministradorCatalogoMixin, CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'catalogos/form.html'
    success_url = reverse_lazy('catalogo_especialidade_list')
    extra_context = {
        'titulo': 'Cadastrar Especialidade',
        'descricao': 'Defina especialidades para profissionais e agendamentos.',
        'voltar_url': reverse_lazy('catalogo_especialidade_list'),
    }


class EspecialidadeUpdateView(AdministradorCatalogoMixin, UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = 'catalogos/form.html'
    success_url = reverse_lazy('catalogo_especialidade_list')
    extra_context = {
        'titulo': 'Editar Especialidade',
        'descricao': 'Atualize o nome ou descrição da especialidade.',
        'voltar_url': reverse_lazy('catalogo_especialidade_list'),
    }


class PlanoSaudeListView(AdministradorCatalogoMixin, ListView):
    model = PlanoSaude
    template_name = 'catalogos/plano_saude_list.html'
    context_object_name = 'planos_saude'


class PlanoSaudeCreateView(AdministradorCatalogoMixin, CreateView):
    model = PlanoSaude
    form_class = PlanoSaudeForm
    template_name = 'catalogos/form.html'
    success_url = reverse_lazy('catalogo_plano_saude_list')
    extra_context = {
        'titulo': 'Cadastrar Plano de Saúde',
        'descricao': 'Registre planos de saúde aceitos pela sua HomeCare.',
        'voltar_url': reverse_lazy('catalogo_plano_saude_list'),
    }


class PlanoSaudeUpdateView(AdministradorCatalogoMixin, UpdateView):
    model = PlanoSaude
    form_class = PlanoSaudeForm
    template_name = 'catalogos/form.html'
    success_url = reverse_lazy('catalogo_plano_saude_list')
    extra_context = {
        'titulo': 'Editar Plano de Saúde',
        'descricao': 'Atualize dados do plano de saúde ou operadora.',
        'voltar_url': reverse_lazy('catalogo_plano_saude_list'),
    }


class ProcedimentoClinicoListView(AdministradorCatalogoMixin, ListView):
    model = ProcedimentoClinico
    template_name = 'catalogos/procedimento_list.html'
    context_object_name = 'procedimentos'


class ProcedimentoClinicoCreateView(AdministradorCatalogoMixin, CreateView):
    model = ProcedimentoClinico
    form_class = ProcedimentoClinicoForm
    template_name = 'catalogos/form.html'
    success_url = reverse_lazy('catalogo_procedimento_list')
    extra_context = {
        'titulo': 'Cadastrar Procedimento',
        'descricao': 'Crie procedimentos clínicos usados em agendamentos.',
        'voltar_url': reverse_lazy('catalogo_procedimento_list'),
    }


class ProcedimentoClinicoUpdateView(AdministradorCatalogoMixin, UpdateView):
    model = ProcedimentoClinico
    form_class = ProcedimentoClinicoForm
    template_name = 'catalogos/form.html'
    success_url = reverse_lazy('catalogo_procedimento_list')
    extra_context = {
        'titulo': 'Editar Procedimento',
        'descricao': 'Atualize nome, descrição ou duração padrão do procedimento.',
        'voltar_url': reverse_lazy('catalogo_procedimento_list'),
    }


class ExameListView(AdministradorCatalogoMixin, ListView):
    model = Exame
    template_name = 'catalogos/exame_list.html'
    context_object_name = 'exames'


class ExameCreateView(AdministradorCatalogoMixin, CreateView):
    model = Exame
    form_class = ExameForm
    template_name = 'catalogos/form.html'
    success_url = reverse_lazy('catalogo_exame_list')
    extra_context = {
        'titulo': 'Cadastrar Exame',
        'descricao': 'Registre exames que poderão ser solicitados nos pedidos de exame.',
        'voltar_url': reverse_lazy('catalogo_exame_list'),
    }


class ExameUpdateView(AdministradorCatalogoMixin, UpdateView):
    model = Exame
    form_class = ExameForm
    template_name = 'catalogos/form.html'
    success_url = reverse_lazy('catalogo_exame_list')
    extra_context = {
        'titulo': 'Editar Exame',
        'descricao': 'Atualize dados e descrição do exame.',
        'voltar_url': reverse_lazy('catalogo_exame_list'),
    }

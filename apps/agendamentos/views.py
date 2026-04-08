from datetime import date, timedelta

from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Agendamento, ReceitaMedica, PedidoExame
from .forms import AgendamentoForm, ReceitaMedicaForm, PedidoExameForm
from apps.notifications.tasks import enviar_whatsapp_agendamento
from apps.pacientes.models import Paciente
from apps.profissionais.models import Profissional


@login_required(login_url='/accounts/login/')
def dashboard(request):
    homecare = request.user.homecare
    agora = timezone.now()
    limite_48h = agora + timedelta(hours=48)

    agendamentos_hoje = Agendamento.objects.filter(data_hora_inicio__date=date.today(), homecare=homecare)
    agendamentos_48h = Agendamento.objects.filter(homecare=homecare, data_hora_inicio__lte=limite_48h)
    proximos_agendamentos = [a for a in agendamentos_48h if a.data_hora_fim() >= agora]
    proximos_agendamentos = sorted(proximos_agendamentos, key=lambda a: a.data_hora_inicio)[:8]
    proximo_agendamento = proximos_agendamentos[0] if proximos_agendamentos else None

    context = {
        'total_pacientes': Paciente.objects.filter(homecare=homecare).count(),
        'total_profissionais': Profissional.objects.filter(ativo=True, homecare=homecare).count(),
        'total_agendamentos_hoje': agendamentos_hoje.count(),
        'total_agendamentos_48h': len(proximos_agendamentos),
        'proximo_agendamento': proximo_agendamento,
        'proximos_agendamentos': proximos_agendamentos,
    }
    return render(request, 'index.html', context)


class AgendamentoListView(LoginRequiredMixin, ListView):
    model = Agendamento
    template_name = 'agendamentos/list.html'
    context_object_name = 'agendamentos'
    paginate_by = 20

    def get_queryset(self):
        return Agendamento.objects.filter(homecare=self.request.user.homecare)


class AgendamentoCreateView(LoginRequiredMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'agendamentos/novo.html'
    success_url = '/agendamentos/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        agendamento = form.save(commit=False)
        agendamento.criado_por = self.request.user
        agendamento.homecare = self.request.user.homecare
        agendamento.save()
        enviar_whatsapp_agendamento.delay(agendamento.id)
        return super().form_valid(form)


class ReceitaMedicaListView(LoginRequiredMixin, ListView):
    model = ReceitaMedica
    template_name = 'agendamentos/receitas_list.html'
    context_object_name = 'receitas'
    paginate_by = 20

    def get_queryset(self):
        return ReceitaMedica.objects.filter(homecare=self.request.user.homecare)


class ReceitaMedicaCreateView(LoginRequiredMixin, CreateView):
    model = ReceitaMedica
    form_class = ReceitaMedicaForm
    template_name = 'agendamentos/receita_form.html'
    success_url = '/agendamentos/receitas/'

    def form_valid(self, form):
        receita = form.save(commit=False)
        receita.homecare = self.request.user.homecare
        receita.save()
        return super().form_valid(form)


class PedidoExameListView(LoginRequiredMixin, ListView):
    model = PedidoExame
    template_name = 'agendamentos/pedidos_list.html'
    context_object_name = 'pedidos'
    paginate_by = 20

    def get_queryset(self):
        return PedidoExame.objects.filter(homecare=self.request.user.homecare)


class PedidoExameCreateView(LoginRequiredMixin, CreateView):
    model = PedidoExame
    form_class = PedidoExameForm
    template_name = 'agendamentos/pedido_form.html'
    success_url = '/agendamentos/pedidos/'

    def form_valid(self, form):
        pedido = form.save(commit=False)
        pedido.homecare = self.request.user.homecare
        pedido.save()
        return super().form_valid(form)

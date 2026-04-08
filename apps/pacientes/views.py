from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView
from apps.accounts.models import CustomUser
from .models import Paciente
from .forms import PacienteForm


class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'pacientes/list.html'
    context_object_name = 'pacientes'
    paginate_by = 20

    def get_queryset(self):
        return Paciente.objects.filter(homecare=self.request.user.homecare)


class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/form.html'
    success_url = '/pacientes/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.role == CustomUser.PROFISSIONAL:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        paciente = form.save(commit=False)
        paciente.homecare = self.request.user.homecare
        paciente.save()
        form.save_m2m()
        return super().form_valid(form)

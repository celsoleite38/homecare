from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView
from apps.accounts.models import CustomUser
from .models import Profissional
from .forms import ProfissionalForm


class ProfissionalListView(LoginRequiredMixin, ListView):
    model = Profissional
    template_name = 'profissionais/list.html'
    context_object_name = 'profissionais'
    paginate_by = 20

    def get_queryset(self):
        return Profissional.objects.filter(homecare=self.request.user.homecare)


class ProfissionalCreateView(LoginRequiredMixin, CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'profissionais/form.html'
    success_url = '/profissionais/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.role == CustomUser.PROFISSIONAL:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        profissional = form.save(commit=False)
        profissional.homecare = self.request.user.homecare
        profissional.save()
        return super().form_valid(form)

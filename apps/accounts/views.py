from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from .forms import HomeCareForm, HomeCareSignupForm
from .models import HomeCare, CustomUser


def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if not CustomUser.objects.exists():
        return redirect('signup')
    return redirect('login')


class HomeCareSignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = HomeCareSignupForm
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if CustomUser.objects.exists():
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        homecare = HomeCare.objects.create(
            nome=form.cleaned_data['nome'],
            cnpj=form.cleaned_data.get('cnpj', ''),
            endereco=form.cleaned_data.get('endereco', ''),
            telefone_fixo=form.cleaned_data.get('telefone_fixo', ''),
            telefone_celular=form.cleaned_data.get('telefone_celular', ''),
            whatsapp_celular=form.cleaned_data.get('whatsapp_celular', False),
            descricao=form.cleaned_data.get('descricao', ''),
            logo=form.cleaned_data.get('logo'),
        )

        user = CustomUser.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
            first_name=form.cleaned_data.get('first_name', ''),
            last_name=form.cleaned_data.get('last_name', ''),
            role=CustomUser.ADMIN_GERAL,
            telefone=form.cleaned_data.get('telefone', ''),
            cpf=form.cleaned_data.get('cpf', ''),
            endereco=form.cleaned_data.get('endereco_usuario', ''),
            homecare=homecare,
        )
        login(self.request, user)
        return super().form_valid(form)


class HomeCareProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = HomeCare
    form_class = HomeCareForm
    template_name = 'accounts/homecare_form.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return self.request.user.homecare

    def test_func(self):
        return self.request.user.role == CustomUser.ADMIN_GERAL

def sair(request):
    logout(request)
    return redirect('login')
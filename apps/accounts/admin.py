from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, HomeCare


@admin.register(HomeCare)
class HomeCareAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone_celular', 'whatsapp_celular')
    search_fields = ('nome', 'cnpj')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'homecare', 'is_staff')
    list_filter = ('role', 'homecare', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações extras', {
            'fields': ('role', 'homecare', 'telefone', 'cpf', 'endereco', 'orgao_regulador', 'registro', 'especialidade'),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser and request.user.role in (CustomUser.ADMIN_GERAL, CustomUser.ADMIN_PLANTOES):
            if 'homecare' in form.base_fields and request.user.homecare_id is not None:
                form.base_fields['homecare'].queryset = HomeCare.objects.filter(pk=request.user.homecare_id)
                form.base_fields['homecare'].initial = request.user.homecare
                form.base_fields['homecare'].disabled = True
            if request.user.role == CustomUser.ADMIN_PLANTOES:
                form.base_fields['role'].choices = [(CustomUser.PROFISSIONAL, 'Profissional')]
        return form

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and request.user.role in (CustomUser.ADMIN_GERAL, CustomUser.ADMIN_PLANTOES):
            obj.homecare = request.user.homecare
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(homecare=request.user.homecare)

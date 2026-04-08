from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.accounts.views import home_redirect
from apps.agendamentos.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('agendamentos/', include('apps.agendamentos.urls')),
    path('profissionais/', include('apps.profissionais.urls')),
    path('pacientes/', include('apps.pacientes.urls')),
    path('catalogos/', include('apps.catalogos.urls')),
    path('accounts/', include('apps.accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

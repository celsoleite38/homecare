from django.urls import path
from .views import PacienteListView, PacienteCreateView

urlpatterns = [
    path('', PacienteListView.as_view(), name='paciente_list'),
    path('novo/', PacienteCreateView.as_view(), name='paciente_novo'),
]

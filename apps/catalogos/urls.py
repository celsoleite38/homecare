from django.urls import path

from .views import (
    CatalogoIndexView,
    EspecialidadeCreateView,
    EspecialidadeListView,
    EspecialidadeUpdateView,
    ExameCreateView,
    ExameListView,
    ExameUpdateView,
    PlanoSaudeCreateView,
    PlanoSaudeListView,
    PlanoSaudeUpdateView,
    ProcedimentoClinicoCreateView,
    ProcedimentoClinicoListView,
    ProcedimentoClinicoUpdateView,
)

urlpatterns = [
    path('', CatalogoIndexView.as_view(), name='catalogo_index'),
    path('especialidades/', EspecialidadeListView.as_view(), name='catalogo_especialidade_list'),
    path('especialidades/novo/', EspecialidadeCreateView.as_view(), name='catalogo_especialidade_novo'),
    path('especialidades/<int:pk>/editar/', EspecialidadeUpdateView.as_view(), name='catalogo_especialidade_editar'),
    path('planos-saude/', PlanoSaudeListView.as_view(), name='catalogo_plano_saude_list'),
    path('planos-saude/novo/', PlanoSaudeCreateView.as_view(), name='catalogo_plano_saude_novo'),
    path('planos-saude/<int:pk>/editar/', PlanoSaudeUpdateView.as_view(), name='catalogo_plano_saude_editar'),
    path('procedimentos/', ProcedimentoClinicoListView.as_view(), name='catalogo_procedimento_list'),
    path('procedimentos/novo/', ProcedimentoClinicoCreateView.as_view(), name='catalogo_procedimento_novo'),
    path('procedimentos/<int:pk>/editar/', ProcedimentoClinicoUpdateView.as_view(), name='catalogo_procedimento_editar'),
    path('exames/', ExameListView.as_view(), name='catalogo_exame_list'),
    path('exames/novo/', ExameCreateView.as_view(), name='catalogo_exame_novo'),
    path('exames/<int:pk>/editar/', ExameUpdateView.as_view(), name='catalogo_exame_editar'),
]

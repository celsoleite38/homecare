from django.urls import path
from .views import (
    AgendamentoListView,
    AgendamentoCreateView,
    AgendamentoEvolucaoUpdateView,
    ReceitaMedicaListView,
    ReceitaMedicaCreateView,
    PedidoExameListView,
    PedidoExameCreateView,
)

urlpatterns = [
    path('', AgendamentoListView.as_view(), name='agendamento_list'),
    path('novo/', AgendamentoCreateView.as_view(), name='agendamento_novo'),
    path('evolucao/<int:pk>/', AgendamentoEvolucaoUpdateView.as_view(), name='agendamento_evolucao'),
    path('receitas/', ReceitaMedicaListView.as_view(), name='receitas_list'),
    path('receitas/novo/', ReceitaMedicaCreateView.as_view(), name='receita_nova'),
    path('pedidos/', PedidoExameListView.as_view(), name='pedidos_list'),
    path('pedidos/novo/', PedidoExameCreateView.as_view(), name='pedido_novo'),
]

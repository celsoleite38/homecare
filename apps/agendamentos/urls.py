from django.urls import path
from .views import (
    AgendamentoListView,
    AgendamentoCreateView,
    ReceitaMedicaListView,
    ReceitaMedicaCreateView,
    PedidoExameListView,
    PedidoExameCreateView,
)

urlpatterns = [
    path('', AgendamentoListView.as_view(), name='agendamento_list'),
    path('novo/', AgendamentoCreateView.as_view(), name='agendamento_novo'),
    path('receitas/', ReceitaMedicaListView.as_view(), name='receitas_list'),
    path('receitas/novo/', ReceitaMedicaCreateView.as_view(), name='receita_nova'),
    path('pedidos/', PedidoExameListView.as_view(), name='pedidos_list'),
    path('pedidos/novo/', PedidoExameCreateView.as_view(), name='pedido_novo'),
]

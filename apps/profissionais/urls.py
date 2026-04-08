from django.urls import path
from .views import ProfissionalListView, ProfissionalCreateView

urlpatterns = [
    path('', ProfissionalListView.as_view(), name='profissional_list'),
    path('novo/', ProfissionalCreateView.as_view(), name='profissional_novo'),
]

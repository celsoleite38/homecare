from celery import shared_task
import requests
from django.conf import settings
from apps.agendamentos.models import Agendamento
from apps.pacientes.models import Responsavel

@shared_task
def enviar_whatsapp_agendamento(agendamento_id):
    try:
        agendamento = Agendamento.objects.get(id=agendamento_id)
        config = ConfiguracaoSistema.objects.first() or ConfiguracaoSistema.objects.create()
        
        # Calcula horário de envio com antecedência
        # (pode usar django-celery-beat para agendar exatamente X horas antes)
        
        mensagem_profissional = f"Olá {agendamento.profissional.nome}!\n\n" \
                                f"Você foi escalado para:\n" \
                                f"Paciente: {agendamento.paciente.nome}\n" \
                                f"Procedimento: {agendamento.procedimento.nome}\n" \
                                f"Horário: {agendamento.data_hora_inicio.strftime('%d/%m/%Y %H:%M')}"
        
        # Enviar para profissional
        send_whatsapp_message(agendamento.profissional.telefone, mensagem_profissional)
        
        # Enviar para responsáveis que aceitam mensagem
        for resp in agendamento.paciente.responsaveis.filter(recebe_mensagem=True):
            mensagem_resp = f"Olá!\nPlantão de {agendamento.paciente.nome} iniciado em breve.\nProfissional: {agendamento.profissional.nome}\nHorário: {agendamento.data_hora_inicio.strftime('%H:%M')}"
            send_whatsapp_message(resp.telefone, mensagem_resp)
            
    except Exception as e:
        print(f"Erro ao enviar WhatsApp: {e}")

def send_whatsapp_message(to_phone, message):
    """Meta Cloud API"""
    url = f"https://graph.facebook.com/{settings.WHATSAPP_API_VERSION}/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_phone.replace("+", "").replace(" ", ""),
        "type": "text",
        "text": {"body": message}
    }
    requests.post(url, json=payload, headers=headers)
# 🏠 HomeCare - Sistema de Gestão para Home Care

Sistema completo de gestão para serviços de **Home Care** desenvolvido em **Django 5.1** com frontend moderno e responsivo usando **Tailwind CSS**.

Ideal para empresas que prestam atendimento domiciliar com **cuidadores de idosos, enfermeiros, técnicos de enfermagem e médicos**.

---

## ✨ Funcionalidades Principais

### 👨‍⚕️ Para Administrador Geral
- Cadastro de **Profissionais** (nome, telefone, CPF, endereço, órgão regulamentador, registro e especialidade)
- Gerenciamento de **Órgãos Regulamentadores** (CRM, COREN, CREFITO, etc.)
- Cadastro de **Especialidades**, **Planos de Saúde**, **Medicamentos** e **Procedimentos Clínicos**
- Criação de **Administrador de Plantões**

### 📅 Para Administrador de Plantões
- Direcionamento de profissionais para pacientes e procedimentos
- Agendamento de **plantões** (1h, 3h, 6h, 12h) e procedimentos (banho, aplicação de injeção, troca de sonda, etc.)
- Autorização de um ou mais profissionais por paciente
- Configuração de **antecedência de notificação** via WhatsApp (horas/minutos)

### 👤 Para Profissionais
- Visualização dos próprios plantões
- Preenchimento de registro de atendimento por plantão/procedimento
- Cadastro de **Receitas Médicas** e **Pedidos de Exames**

### 👴 Para Pacientes
- Cadastro completo (nome, idade, CPF, data de nascimento, endereço, telefone, quadro médico, plano de saúde)
- Cadastro de **responsáveis** com opção de receber notificações

### 📲 Notificações via WhatsApp (automático)
- Notificação para o **profissional** com antecedência configurável
- Notificação para os **responsáveis** do paciente no início do plantão/procedimento

### 🎨 Frontend
- Interface **elegante, moderna e totalmente responsiva** (otimizada para celular e tablet)
- Design clean com Tailwind CSS
- Dashboard intuitivo com status de plantões

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.1 + Python 3.12
- **Frontend**: Tailwind CSS + Font Awesome
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Tarefas assíncronas**: Celery + Redis
- **Notificações**: WhatsApp Cloud API (Meta) ou Evolution API
- **Autenticação**: CustomUser com perfis (Admin Geral, Admin de Plantões, Profissional)

---

## 📋 Como Rodar o Projeto Localmente

### Pré-requisitos
- Python 3.10 ou superior
- Git
- Redis (para Celery - opcional no início)

### Passos

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/homecare.git
   cd homecare

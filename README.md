 Helpdesk API

API RESTful para gestão de chamados técnicos, desenvolvida com Django, Django Rest Framework, PostgreSQL, Docker e CI/CD.

> **Repositório:** https://github.com/AlexRodrigues2004/helpdesk-api

---

## 📋 Tecnologias

- Python 3.12
- Django 5.0
- Django Rest Framework 3.15
- PostgreSQL 15
- Docker & Docker Compose
- GitHub Actions (CI)
- Render (CD)

---

## ✅ Etapas concluídas

- [x] **Etapa 1 — Estrutura base do projeto** (`feat/project-structure`)
  - Criação do projeto Django com configuração via variáveis de ambiente
  - Apps separados: `users`, `customers`, `tickets`, `categories`, `interactions`
  - Settings com DRF, TokenAuthentication, paginação e filtros configurados
  - `.env`, `.gitignore` e `requirements.txt`

---

## 🔜 Próximas etapas

- [ ] **Etapa 2 — Docker** (`feat/docker-setup`): Dockerfile + docker-compose.yml
- [ ] **Etapa 3 — Models** (`feat/models-and-migrations`): Models e migrations de todos os apps
- [ ] **Etapa 4 — Serializers** (`feat/serializers`): Serializers com validações
- [ ] **Etapa 5 — Auth e Permissões** (`feat/auth-and-permissions`): Token auth, perfis, permissões
- [ ] **Etapa 6 — ViewSets e Rotas** (`feat/viewsets-and-routes`): Endpoints, filtros, paginação
- [ ] **Etapa 7 — Testes** (`feat/tests`): pytest-django cobrindo todos os requisitos
- [ ] **Etapa 8 — CI** (`feat/ci-pipeline`): GitHub Actions
- [ ] **Etapa 9 — CD** (`feat/cd-strategy`): Deploy no Render
- [ ] **Etapa 10 — Documentação** (`feat/documentation`): README completo + Swagger

---

## 📁 Estrutura do projeto
helpdesk-api/
├── apps/
│   ├── users/          # Usuários e autenticação
│   ├── customers/      # Gestão de clientes
│   ├── tickets/        # Chamados técnicos
│   ├── categories/     # Categorias de chamados
│   └── interactions/   # Histórico de interações
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md

---

## 🔑 Perfis de usuário

| Perfil | Permissões |
|--------|-----------|
| **Cliente** | Abre e acompanha apenas os próprios chamados |
| **Atendente** | Visualiza todos os chamados, altera status e prioridade |
| **Administrador** | Acesso total, pode remover registros |

---

## 📡 Endpoints (resumo)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/auth/login/` | Login e obtenção de token |
| GET/POST | `/api/customers/` | Listar/criar clientes |
| GET/POST | `/api/categories/` | Listar/criar categorias |
| GET/POST | `/api/tickets/` | Listar/criar chamados |
| GET/PUT/PATCH | `/api/tickets/{id}/` | Detalhes/atualizar chamado |
| GET/POST | `/api/tickets/{id}/interactions/` | Histórico de interações |
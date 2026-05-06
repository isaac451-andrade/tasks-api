# Tasks API

Uma API de gerenciamento de tarefas desenvolvida para oferecer uma experiência segura e organizada. O sistema permite que cada usuário gerencie suas próprias tarefas de forma isolada, garantindo total privacidade e integridade dos dados através de autenticação via **JSON Web Tokens (JWT)**.

## Tecnologias
- **Python 3.13+**
- **Django & Django REST Framework (DRF)**
- **Simple JWT** (Autenticação)
- **SQLite** (Desenvolvimento) / **PostgreSQL** (Produção)

## Funcionalidades Core
- **Autenticação Segura:** Registro e login de usuários com validação JWT.
- **Isolamento de Dados:** Um usuário só pode visualizar, editar ou deletar suas próprias tarefas.
- **Gestão de Tarefas (CRUD):** 
  - Criação com validação de campos obrigatórios.
  - Atualização parcial (PATCH) ou total (PUT).
  - Listagem filtrada automaticamente pelo usuário logado.
  - Exclusão lógica ou física.
- **Controle de Status:** Fluxo de estados da tarefa (`pendente`, `em_andamento`, `concluido`, `aguardando_dependencia`).
- **Validação de Datas:** Suporte nativo ao padrão ISO 8601 para `data_conclusao`.

## Estrutura do Modelo Task
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `titulo` | String | Título da tarefa (Obrigatório) |
| `descricao` | Text | Detalhamento da atividade |
| `status` | Choice | Estado atual da tarefa |
| `data_criacao`| DateTime | Gerado automaticamente no cadastro |
| `data_conclusao`| DateTime | Prazo definido pelo usuário (ISO format) |
| `observacao` | Text | Notas adicionais |
| `usuario` | ForeignKey| Vínculo direto com o dono da tarefa |

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/tasks-api.git](https://github.com/seu-usuario/tasks-api.git)

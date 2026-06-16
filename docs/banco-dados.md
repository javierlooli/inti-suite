# Banco de Dados - Inti Suite

## Tabela: usuarios

Responsável pelos acessos ao sistema.

| Campo      | Tipo      |
| ---------- | --------- |
| id         | UUID      |
| nome       | VARCHAR   |
| email      | VARCHAR   |
| senha_hash | VARCHAR   |
| perfil     | VARCHAR   |
| ativo      | BOOLEAN   |
| criado_em  | TIMESTAMP |

Perfis iniciais:

* Administrador
* Engenheiro
* Comercial
* Financeiro
* Visualização

---

## Tabela: clientes

Cadastro único de clientes.

| Campo             | Tipo      |
| ----------------- | --------- |
| id                | UUID      |
| tipo              | VARCHAR   |
| nome_razao_social | VARCHAR   |
| cpf_cnpj          | VARCHAR   |
| responsavel       | VARCHAR   |
| telefone          | VARCHAR   |
| email             | VARCHAR   |
| endereco          | TEXT      |
| observacoes       | TEXT      |
| criado_em         | TIMESTAMP |

Tipos:

* Pessoa Física
* Pessoa Jurídica
* Órgão Público

---

## Tabela: contatos

Histórico de contatos com clientes.

| Campo        | Tipo      |
| ------------ | --------- |
| id           | UUID      |
| cliente_id   | UUID      |
| data_contato | TIMESTAMP |
| meio_contato | VARCHAR   |
| descricao    | TEXT      |
| usuario_id   | UUID      |

Meios:

* WhatsApp
* Telefone
* E-mail
* Presencial

---

## Tabela: demandas

Oportunidades ou serviços solicitados.

| Campo          | Tipo      |
| -------------- | --------- |
| id             | UUID      |
| cliente_id     | UUID      |
| titulo         | VARCHAR   |
| tipo_servico   | VARCHAR   |
| descricao      | TEXT      |
| prioridade     | VARCHAR   |
| status         | VARCHAR   |
| valor_estimado | DECIMAL   |
| prazo_previsto | DATE      |
| criado_em      | TIMESTAMP |

Tipos de Serviço:

* Energia Solar
* Projeto Elétrico
* SPDA
* Laudo Técnico
* Subestação
* Automação
* Consultoria
* Treinamento
* Outros

Status:

* Lead
* Em análise
* Proposta
* Negociação
* Contratado
* Cancelado
* Concluído

---

## Tabela: propostas

Controle de propostas comerciais.

| Campo           | Tipo      |
| --------------- | --------- |
| id              | UUID      |
| demanda_id      | UUID      |
| numero_proposta | VARCHAR   |
| valor_total     | DECIMAL   |
| prazo_execucao  | VARCHAR   |
| validade        | DATE      |
| status          | VARCHAR   |
| arquivo_pdf     | VARCHAR   |
| criado_em       | TIMESTAMP |

Status:

* Em elaboração
* Enviada
* Em negociação
* Aprovada
* Rejeitada

---

## Relacionamentos

clientes
↓
demandas
↓
propostas

Um cliente pode possuir várias demandas.

Uma demanda pode possuir várias propostas ao longo da negociação.

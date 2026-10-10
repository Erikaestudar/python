# 💬 AI Assistant

Projeto do Lab da DIO **"Construa Seu Assistente Virtual Com Inteligência Artificial"**.

O AI Assistant é um guia financeiro para iniciantes, que conduz a pessoa em 3 etapas:

1. **Entender** — para onde o dinheiro está indo, com base nas transações;
2. **Planejar** — quanto guardar por mês para chegar nas metas do perfil;
3. **Aprender** — explica e compara produtos financeiros, sem indicar um específico.

Ele roda 100% local com [Ollama](https://ollama.com), sem custo e sem enviar dados para fora do computador.

## Estrutura do Repositório

```
AI-assistant/
  README.md
  data/                      # Base de conhecimento (dados fictícios)
  docs/                      # Documentação do desafio (6 passos)
  src/                       # Código da aplicação (Streamlit)
```

## Documentação

| Passo | Arquivo |
|---|---|
| 1. Documentação do Agente | [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md) |
| 2. Base de Conhecimento | [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md) |
| 3. Prompts do Agente | [`docs/03-prompts.md`](./docs/03-prompts.md) |
| 4. Aplicação Funcional | [`src/app.py`](./src/app.py) |
| 5. Avaliação e Métricas | [`docs/04-metricas.md`](./docs/04-metricas.md) |
| 6. Pitch | [`docs/05-pitch.md`](./docs/05-pitch.md) |

## Como Rodar

```bash
# 1. Instalar o Ollama: https://ollama.com
# 2. Baixar o modelo (uma vez só)
ollama pull gpt-oss

# 3. Instalar as dependências do projeto
cd src
pip install -r requirements.txt

# 4. Rodar
streamlit run app.py
```

## Base neste projeto

Baseado no [Repositório Base do Lab BIA do Futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro) e no [repositório de exemplo "Edu, Educador Financeiro Inteligente"](https://github.com/falvojr/dio-lab-bia-do-futuro), da Digital Innovation One.

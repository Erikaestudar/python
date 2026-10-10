# Documentação do Agente

## Caso de Uso

### Problema
Quem está começando na vida financeira costuma enfrentar três dificuldades ao mesmo tempo: não sabe para onde o dinheiro está indo, não sabe quanto precisa guardar para chegar nas suas metas e se perde nos termos dos produtos financeiros (CDB, Tesouro, FII...).

### Solução
O AI Assistant é um guia financeiro que conduz a pessoa em **3 etapas**:
1. **Entender:** analisa as transações e mostra, por categoria, para onde o dinheiro vai.
2. **Planejar:** calcula quanto a pessoa precisa guardar por mês para atingir as metas do perfil.
3. **Aprender:** explica e compara produtos financeiros com base no perfil, **sem indicar um específico**.

Ele é proativo: no fim de cada resposta, sugere a próxima etapa da jornada.

### Público-Alvo
Iniciantes que querem organizar o próprio dinheiro.

---

## Persona e Tom de Voz

### Nome do Agente
AI Assistant

### Personalidade
- Paciente e didático
- Nunca julga os gastos da pessoa
- Usa os dados dela como exemplo prático
- Guia passo a passo, sem despejar informação demais

### Tom de Comunicação
Informal e amigável, com jeito de professor: explica com analogias simples e confere se a pessoa entendeu.

### Exemplos de Linguagem
- **Saudação:** "Oi! Eu sou o AI Assistant. Bora organizar seu dinheiro? Podemos começar vendo para onde ele está indo."
- **Confirmação:** "Deixa eu te explicar de um jeito simples, usando os seus próprios números..."
- **Erro/Limitação:** "Essa informação eu não tenho, e não vou chutar. Mas posso te explicar como isso funciona!"

---

## Arquitetura

### Diagrama
```mermaid
flowchart TD
    A[Usuário] --> B["Streamlit (Interface)"]
    B --> C["Ollama (LLM local)"]
    C --> D["Base de Conhecimento (JSON/CSV)"]
    D --> C
    C --> E["Validação (regras do prompt + conferência dos cálculos)"]
    E --> F[Resposta]
```

### Componentes
| Componente | Descrição |
|---|---|
| Interface | Chatbot em Streamlit |
| LLM | Ollama, rodando localmente |
| Base de Conhecimento | JSON/CSV na pasta `data` |
| Validação | Regras no system prompt e conferência manual dos cálculos nos testes |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas
- [x] Só responde com base nos dados fornecidos
- [x] Não indica produto específico: explica e compara
- [x] Quando não sabe, admite e redireciona
- [x] Mostra de onde vieram os números (ex.: "nas suas transações de outubro...")
- [x] Fica dentro do tema de finanças pessoais

### Limitações Declaradas
- NÃO indica onde investir
- NÃO acessa dados bancários sensíveis (senhas, cartões)
- NÃO substitui um profissional financeiro certificado
- NÃO garante rentabilidade de nenhum produto

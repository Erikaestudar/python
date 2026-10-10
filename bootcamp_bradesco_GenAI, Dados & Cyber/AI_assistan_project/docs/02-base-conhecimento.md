# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no AI Assistant |
|---|---|---|
| `transacoes.csv` | CSV | **Etapa Entender:** agrupar gastos por categoria e mostrar para onde o dinheiro vai |
| `perfil_investidor.json` | JSON | **Etapa Planejar:** usar renda, reserva atual e metas para calcular quanto guardar por mês |
| `produtos_financeiros.json` | JSON | **Etapa Aprender:** explicar e comparar produtos de acordo com o perfil |
| `historico_atendimento.csv` | CSV | Dar continuidade à conversa com base em atendimentos anteriores |

## Adaptações nos Dados

Os dados mockados do repositório base foram ampliados para dar suporte às 3 etapas do assistente:

- **`transacoes.csv`**: passou de 10 para 43 linhas, cobrindo julho, agosto e setembro de 2026. Foram adicionadas as categorias educação, vestuário, outros e poupança (aporte mensal na reserva de emergência), além de uma receita extra (freelance) em agosto.
- **`perfil_investidor.json`**: os prazos das metas foram atualizados para datas futuras (reserva de emergência para 2027-06, entrada do apartamento para 2029-12), já que os prazos originais estavam vencidos.
- **`produtos_financeiros.json`**: foi adicionado o campo `liquidez` (quando dá para sacar) em cada produto, e o Fundo Multimercado foi substituído por Fundo Imobiliário (FII).

Todos os valores são fictícios e foram conferidos manualmente com pandas, servindo de gabarito para os testes do Passo 5.

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON e CSV são lidos no início da sessão com Python (`json` e `pandas`).

### Como os dados são usados no prompt?
Os dados são inseridos no contexto enviado ao Ollama, junto do system prompt, incluindo resumos já calculados (gastos por categoria/mês e o valor mensal necessário para cada meta), para reduzir erros de cálculo do modelo. Isso funciona bem porque a base é pequena; em uma solução maior, a consulta seria dinâmica.

## Exemplo de Contexto Montado

```
CLIENTE: João Silva, 32 anos, perfil moderado
OBJETIVO: Construir reserva de emergência
RESERVA: R$ 10.000 de R$ 15.000 | RENDA: R$ 5.000

METAS (já calculadas):
- Completar reserva de emergência: faltam R$ 5.000,00 em 9 meses (prazo 2027-06) ≈ R$ 555,56/mês

GASTOS POR CATEGORIA (setembro): moradia R$ 1.480,00, alimentação R$ 655,00, ...
PRODUTOS: Tesouro Selic (risco baixo, aporte mín. R$ 30, D+1), CDB Liquidez Diária, ...
```

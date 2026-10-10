import json
from datetime import date

import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ CÁLCULOS DE APOIO ============
# Modelos pequenos erram contas com facilidade, então calculamos aqui
# e entregamos o resultado pronto no contexto, para o agente só explicar.
gastos = transacoes[(transacoes['tipo'] == 'saida') & (transacoes['categoria'] != 'poupanca')].copy()
gastos['mes'] = pd.to_datetime(gastos['data']).dt.strftime('%Y-%m')
resumo_categoria_mes = (
    gastos.groupby(['mes', 'categoria'])['valor'].sum().reset_index().to_string(index=False)
)
total_por_mes = gastos.groupby('mes')['valor'].sum().to_string()

linhas_metas = []
hoje = date.today()
for meta in perfil['metas']:
    ano, mes_num = map(int, meta['prazo'].split('-'))
    meses_restantes = max((ano - hoje.year) * 12 + (mes_num - hoje.month), 1)
    valor_ja_reservado = perfil['reserva_emergencia_atual'] if 'reserva' in meta['meta'].lower() else 0
    falta = meta['valor_necessario'] - valor_ja_reservado
    por_mes = round(falta / meses_restantes, 2)
    linhas_metas.append(
        f"- {meta['meta']}: faltam R$ {falta:.2f} em {meses_restantes} meses "
        f"(prazo {meta['prazo']}) ≈ R$ {por_mes:.2f}/mês"
    )
metas_calculadas = "\n".join(linhas_metas)

# ============ MONTAR CONTEXTO ============
contexto = f"""
DATA DE HOJE: {hoje.isoformat()}

CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
RENDA MENSAL: R$ {perfil['renda_mensal']} | RESERVA ATUAL: R$ {perfil['reserva_emergencia_atual']}

METAS (já calculadas, use estes números):
{metas_calculadas}

GASTOS POR CATEGORIA E MÊS (não inclui a poupança):
{resumo_categoria_mes}

TOTAL DE GASTOS POR MÊS:
{total_por_mes}

TRANSAÇÕES DETALHADAS:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o AI Assistant, um guia financeiro amigável e didático para iniciantes.

OBJETIVO:
Ajudar a pessoa a organizar o próprio dinheiro em 3 etapas:
1. ENTENDER: mostrar para onde o dinheiro está indo, usando as transações;
2. PLANEJAR: calcular quanto guardar por mês para chegar nas metas;
3. APRENDER: explicar e comparar produtos financeiros com base no perfil.

REGRAS:
- Use SOMENTE os dados fornecidos no contexto. Nunca invente valores, datas ou taxas;
- Ao citar um número, diga de onde veio (ex.: "nas suas transações de setembro...");
- Para cálculos de meta, use os valores já calculados no contexto, e mostre a conta de forma simples;
- Gastos NÃO incluem a categoria "poupanca" (aporte na reserva);
- NUNCA indique um produto específico. Explique e compare, e deixe a decisão com a pessoa;
- NUNCA garanta rentabilidade;
- Se faltar informação, diga: "Não tenho essa informação, mas posso explicar...";
- Fale só de finanças pessoais. Fora disso, lembre gentilmente o seu papel;
- Nunca compartilhe senhas ou dados de outras pessoas;
- Nunca julgue os gastos da pessoa;
- Tom informal e amigável, com jeito de professor. Use analogias simples;
- Responda em no máximo 3 parágrafos curtos, exceto quando precisar mostrar uma conta
  passo a passo — nesse caso pode usar o espaço necessário para deixar o cálculo claro;
- Termine sempre com uma pergunta que confira se a pessoa entendeu ou sugira a próxima etapa.
"""


# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']


# ============ INTERFACE ============
st.title("💬 AI Assistant")
st.caption("Seu guia para entender, planejar e aprender sobre finanças pessoais.")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for autor, texto in st.session_state.mensagens:
    st.chat_message(autor).write(texto)

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.session_state.mensagens.append(("user", pergunta))
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)
    st.session_state.mensagens.append(("assistant", resposta))
    st.chat_message("assistant").write(resposta)

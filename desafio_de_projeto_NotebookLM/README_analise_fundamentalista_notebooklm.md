# 📊 Análise Fundamentalista de Ações e Fundos Imobiliários

> Projeto desenvolvido para o desafio da DIO sobre **uso da Inteligência Artificial como ferramenta de aprendizagem ativa**, utilizando o NotebookLM para pesquisa, organização e consolidação de conhecimentos.

---

## 🎯 Contexto e Objetivos

Este projeto nasceu do interesse em compreender melhor como analisar investimentos de longo prazo utilizando fundamentos financeiros e uma visão mais consciente sobre risco, preço e qualidade dos ativos.

O tema escolhido para o Caderno Temático no NotebookLM foi:

**📈 Análise Fundamentalista de Ações e Fundos Imobiliários**

O objetivo principal foi utilizar a Inteligência Artificial não apenas para obter respostas prontas, mas como uma ferramenta de aprendizagem ativa, permitindo:

- organizar informações de diferentes fontes;
- comparar conceitos;
- elaborar perguntas estratégicas;
- identificar os principais indicadores utilizados na análise de empresas e FIIs;
- construir um material de consulta para estudos futuros;
- desenvolver uma visão mais crítica sobre as informações apresentadas pela IA;
- transformar as pesquisas em um miniguia estruturado.

O estudo também buscou relacionar a análise quantitativa dos indicadores com aspectos qualitativos, como governança, vantagens competitivas, qualidade da gestão e disciplina do investidor.

---

## 🤖 Como o NotebookLM foi utilizado

O NotebookLM foi utilizado como um ambiente para reunir fontes, fazer perguntas sobre o conteúdo disponibilizado e transformar diferentes materiais em conhecimento organizado.

O processo seguido foi:

1. **Definição do tema** → análise fundamentalista de ações e FIIs.
2. **Curadoria das fontes** → seleção de materiais relacionados ao assunto.
3. **Importação das fontes no NotebookLM**.
4. **Formulação de perguntas estratégicas** sobre os conceitos estudados.
5. **Comparação e organização das respostas**.
6. **Identificação de pontos que precisavam de maior investigação**.
7. **Criação de um miniguia final** com conceitos, glossário e prompts reutilizáveis.
8. **Documentação do processo no GitHub**.

A ideia foi utilizar a IA como uma espécie de assistente de pesquisa, mantendo a responsabilidade de analisar criticamente as respostas.

## 🤖 NotebookLM

O Caderno Temático utilizado neste projeto foi desenvolvido no NotebookLM.

**Acessar o Caderno Temático:**

[NotebookLM — Análise Fundamentalista de Ações e Fundos Imobiliários](https://notebook.google.com/notebook/8bb99b44-bd5f-4677-b32b-e455fdf8023c)

---

# 📚 Curadoria de Fontes

O desafio da DIO solicita a seleção de **3 a 5 fontes abertas em texto ou PDF que tenham sido selecionadas e enviadas ao NotebookLM**.

Para evitar confundir materiais efetivamente utilizados como fontes principais do Caderno Temático com plataformas consultadas durante os estudos, este README separa as referências em duas categorias.

## Fontes principais selecionadas para o Caderno Temático

### 1. 📘 O Investidor Inteligente — Benjamin Graham

Utilizado como referência para a mentalidade de investimento de longo prazo, principalmente nos conceitos de:

- diferença entre investimento e especulação;
- margem de segurança;
- relação entre preço e valor;
- disciplina na tomada de decisão.

### 2. 📘 A Chave Mestra — Napoleon Hill

Material utilizado como apoio à construção da mentalidade e dos princípios pessoais relacionados ao desenvolvimento e à disciplina.

### 3. 📘 Mais Esperto que o Diabo — Napoleon Hill

Utilizado como material complementar para reflexão sobre comportamento, disciplina e fatores psicológicos relacionados à tomada de decisões.

### 4. 📘 O Homem Mais Rico da Babilônia

Utilizado como referência complementar para princípios de educação financeira e construção de hábitos relacionados à gestão do dinheiro.

### 5. 📘 Pense e Enriqueça — Napoleon Hill

Utilizado como apoio para os aspectos de mentalidade, objetivos e disciplina presentes no estudo.

> **Observação:** estas são as fontes principais destacadas no material original do projeto. A relação acima representa a curadoria apresentada no material fornecido; o README não afirma que todos os cinco títulos foram necessariamente enviados ao NotebookLM em formato de arquivo.

## Fontes complementares

Além das fontes principais, foram utilizados sites e conteúdos em vídeo como apoio para consulta, comparação e aprofundamento.

### Status Invest

Plataforma utilizada como fonte de consulta para indicadores financeiros e informações relacionadas a empresas e investimentos.

[Status Invest](https://statusinvest.com.br/)

### Investidor10

Plataforma utilizada como apoio para consulta e organização de informações e indicadores de investimentos.

[Investidor10](https://investidor10.com.br/)

### Daycoval — Análise de FIIs

Material utilizado como apoio para compreender critérios relacionados à análise de Fundos Imobiliários.

[Como analisar um FII — Daycoval](https://blog.daycoval.com.br/como-analisar-um-fii/)

### Conteúdos educacionais em vídeo

Foram utilizados diversos conteúdos em vídeo como material complementar durante a construção do Caderno Temático.

Os links dos vídeos utilizados durante os estudos estão registrados no material original do projeto. Eles funcionaram como materiais complementares e não são apresentados aqui como fontes principais do Caderno Temático.

---

# 🧠 Engenharia de Prompts

Uma das partes importantes deste projeto foi perceber que **a qualidade da resposta da IA depende diretamente da qualidade da pergunta feita**.

Como o projeto foi construído a partir de um caderno com diversas fontes, os prompts foram organizados em etapas progressivas.

## Etapa 1 — Exploração

O primeiro objetivo foi compreender o que as fontes apresentavam sobre o tema.

### Prompt de exploração

```text
Analise as fontes disponíveis e explique o que elas apresentam sobre
Análise Fundamentalista de Ações, considerando o contexto dos principais
indicadores de investimento.

Organize a resposta por categorias de indicadores e explique a finalidade
de cada indicador de forma clara.
```

### Objetivo

Identificar os conceitos recorrentes nas fontes e construir uma primeira visão geral do assunto.

---

## Etapa 2 — Organização dos indicadores

Depois da visão inicial, o próximo passo foi separar os indicadores por finalidade.

### Prompt

```text
Organize os principais indicadores de análise fundamentalista mencionados
nas fontes nas seguintes categorias:

1. Valuation
2. Rentabilidade e eficiência
3. Endividamento e saúde financeira
4. Crescimento
5. Proventos

Para cada indicador, explique:
- o que significa;
- o que ele mede;
- como deve ser interpretado;
- quais cuidados o investidor deve ter.
```

### Resultado esperado

Essa abordagem permite transformar uma grande quantidade de informação em uma estrutura de estudo mais fácil de revisar.

---

## Etapa 3 — Análise qualitativa

Os números sozinhos não representam toda a qualidade de uma empresa.

### Prompt

```text
Além dos indicadores financeiros, quais aspectos qualitativos as fontes
consideram importantes na análise de uma empresa?

Explique a importância de:
- governança;
- vantagens competitivas;
- qualidade da gestão;
- setor de atuação;
- alinhamento entre gestores e acionistas;
- margem de segurança.
```

### Aprendizado

A análise fundamentalista não deve ser reduzida a encontrar um indicador "bom". É necessário analisar o negócio como um todo.

---

## Etapa 4 — Análise de FIIs

Para os Fundos Imobiliários, foram consideradas características específicas.

### Prompt

```text
Com base nas fontes, organize os principais critérios utilizados para
avaliar Fundos Imobiliários.

Explique:
- vacância física;
- vacância financeira;
- P/VP;
- Dividend Yield;
- liquidez;
- qualidade dos ativos;
- qualidade da gestão;
- concentração de inquilinos;
- riscos de alavancagem.

Destaque também os principais sinais de alerta.
```

---

# 🩹 "Cicatrizes" — Troubleshooting durante o uso da IA

Um dos aprendizados deste projeto foi perceber que uma resposta aparentemente completa pode não ser suficiente para uma análise adequada.

### Problema 1 — Excesso de informação

Quando existem muitas fontes, uma pergunta muito ampla pode gerar uma resposta extensa e difícil de estudar.

**Solução:** dividir a pesquisa em categorias e fazer perguntas específicas.

---

### Problema 2 — Indicadores apresentados isoladamente

Um indicador pode parecer excelente sem que a empresa seja necessariamente um bom investimento.

**Solução:** pedir à IA para relacionar os indicadores entre si e também considerar fatores qualitativos.

---

### Problema 3 — Risco de interpretar números fora de contexto

Um P/L baixo, por exemplo, pode significar que uma ação está descontada, mas também pode estar associado a problemas de rentabilidade, crescimento ou expectativas do mercado.

**Solução:** utilizar prompts que peçam explicitamente **interpretação + contexto + possíveis armadilhas**.

---

### Problema 4 — Dividend Yield elevado

Um DY elevado pode parecer automaticamente positivo, mas as fontes destacam que um yield muito alto pode esconder problemas, quedas na cotação ou distribuições não recorrentes.

**Solução:** analisar o indicador juntamente com os demais fundamentos.

---

# 📖 Miniguia de Estudos

## 1. 📈 Análise Fundamentalista

A análise fundamentalista busca estimar o valor de uma empresa considerando seus fundamentos econômicos, financeiros e setoriais.

O foco principal é compreender a **saúde do negócio**, e não apenas observar oscilações de preço.

A análise pode ser dividida em:

- valuation;
- rentabilidade;
- endividamento;
- crescimento;
- proventos;
- análise qualitativa.

---

# 💰 2. Indicadores de Valuation

## P/L — Preço/Lucro

Compara o preço da ação com o lucro da empresa.

Um P/L menor pode indicar que o mercado está pagando menos por unidade de lucro, mas isso não significa automaticamente que a ação seja barata.

Um P/L elevado pode refletir expectativas maiores de crescimento.

**Principal cuidado:** nunca analisar o P/L isoladamente.

---

## P/VP — Preço/Valor Patrimonial

Compara o valor de mercado da empresa com seu patrimônio líquido.

Um P/VP abaixo de 1 pode indicar que o mercado está negociando a empresa abaixo do seu valor patrimonial.

Por outro lado, isso também pode indicar problemas de rentabilidade ou expectativas negativas.

---

## EV/EBITDA

Relaciona o valor da empresa com sua geração operacional de resultado.

É especialmente útil porque considera a estrutura de capital da empresa de maneira diferente do P/L.

---

## PSR — Price to Sales Ratio

Relaciona o valor de mercado com a receita da empresa.

Pode ser útil principalmente em empresas de crescimento que ainda não apresentam lucro líquido consistente.

---

# 📊 3. Rentabilidade e Eficiência

## ROE — Return on Equity

Mede a rentabilidade obtida sobre o patrimônio líquido.

Ajuda a entender como a empresa utiliza o capital dos acionistas para gerar resultados.

---

## ROIC — Return on Invested Capital

Avalia o retorno produzido sobre o capital investido na operação.

É importante para avaliar a capacidade do negócio de gerar retorno utilizando o capital necessário para suas atividades.

---

## Margem Líquida

Indica quanto da receita da empresa permanece como lucro líquido depois das despesas e impostos.

A interpretação precisa considerar o setor.

Uma margem considerada baixa em determinado setor pode ser normal em outro.

---

# 🏦 4. Endividamento e Saúde Financeira

## Dívida Líquida/EBITDA

Relaciona a dívida líquida da empresa com sua capacidade operacional de geração de resultado.

Quanto maior o indicador, maior tende a ser a preocupação com o peso da dívida.

As fontes destacam valores acima de aproximadamente 3 a 4 vezes como um sinal de alerta.

---

## Resultado Financeiro/EBIT

Ajuda a avaliar quanto do resultado operacional está sendo consumido pelos efeitos financeiros, especialmente juros.

O material aponta um patamar de até aproximadamente 25% como referência saudável.

---

# 📈 5. Crescimento

## CAGR — Compound Annual Growth Rate

Representa a taxa de crescimento anual composta.

Pode ser utilizado para analisar o crescimento histórico de:

- receita;
- lucro;
- outros indicadores relevantes.

O objetivo não é apenas encontrar crescimento, mas observar se ele é **consistente e sustentável**.

---

# 💵 6. Proventos

## Dividend Yield — DY

Representa o rendimento dos dividendos em relação ao preço do ativo.

Um DY elevado não deve ser interpretado automaticamente como uma vantagem.

É necessário investigar:

- origem dos dividendos;
- recorrência;
- qualidade do negócio;
- evolução dos resultados;
- preço do ativo.

---

## Payout

Representa a parcela do lucro líquido distribuída aos acionistas.

Um payout elevado pode ser interessante em empresas maduras, mas precisa ser analisado de acordo com o setor, crescimento e capacidade de geração de caixa.

---

# 🏢 7. Análise Qualitativa

Além dos indicadores, o estudo destacou três grandes dimensões.

### 🛡️ Governança Corporativa

Avaliar:

- transparência;
- alinhamento dos executivos;
- proteção aos acionistas minoritários;
- Tag Along;
- nível de governança.

---

### 🏰 Vantagens Competitivas

Também chamadas de "fossos", são características que dificultam a entrada de concorrentes.

Exemplos:

- marcas fortes;
- escala;
- patentes;
- relacionamento com clientes;
- vantagens estruturais.

---

### 🧭 Qualidade do Negócio

É importante compreender:

- como a empresa ganha dinheiro;
- em qual setor atua;
- quais são seus principais riscos;
- se possui capacidade de atravessar períodos difíceis;
- se possui crescimento sustentável.

---

# 🏠 8. Análise de Fundos Imobiliários

A análise de FIIs possui particularidades próprias.

## Vacância Física

Representa o espaço físico que está desocupado.

---

## Vacância Financeira

Indica quanto de receita o fundo deixa de receber por causa das áreas ou contratos que não estão gerando renda.

O material destaca a importância de observar a vacância financeira, além da física.

---

## P/VP

Ajuda a comparar o preço de mercado das cotas com o valor patrimonial.

Um P/VP abaixo de 1 pode indicar desconto.

Entretanto, um valor muito baixo também pode ser um sinal de problemas estruturais.

O material cita valores abaixo de aproximadamente 0,70 como possível sinal de alerta.

---

## Liquidez

A liquidez diária é importante porque influencia a facilidade de comprar ou vender cotas.

O material utiliza aproximadamente **R$ 2 milhões por dia** como referência de liquidez desejável.

---

## Qualidade da Gestão

Avaliar:

- histórico da gestão;
- decisões anteriores;
- qualidade das aquisições;
- transparência;
- alinhamento com os cotistas.

---

## 🏢 Qualidade dos Ativos

É importante observar:

- localização;
- qualidade dos imóveis;
- diversificação;
- perfil dos inquilinos;
- concentração;
- contratos;
- vacância.

---

# ⚠️ 9. Principais Armadilhas

### ❌ Olhar somente para o DY

Um DY elevado pode ser consequência de uma queda forte no preço da cota ou de distribuições não recorrentes.

### ❌ Procurar apenas P/VP abaixo de 1

Desconto patrimonial não significa necessariamente oportunidade.

### ❌ Analisar apenas um indicador

Uma empresa pode apresentar P/L baixo e, ao mesmo tempo, ter problemas de crescimento ou endividamento.

### ❌ Ignorar a qualidade da gestão

Números passados não substituem a avaliação da capacidade de gestão.

### ❌ Confundir preço baixo com ativo barato

Preço é o que o mercado está cobrando.

Valor depende dos fundamentos e das expectativas relacionadas ao negócio.

---

# 🧠 10. O Triângulo do Holder

O material apresenta uma visão baseada no equilíbrio entre:

**Crescimento + Qualidade + Preço**

Um ativo pode apresentar excelente qualidade, mas estar caro.

Outro pode estar barato, mas apresentar baixa qualidade.

Outro pode crescer muito, mas possuir riscos elevados.

Por isso, o objetivo é buscar equilíbrio entre os três elementos.

---

# 📚 Glossário

| Conceito | Significado |
|---|---|
| **P/L** | Relação entre preço da ação e lucro |
| **P/VP** | Relação entre preço e valor patrimonial |
| **EV** | Enterprise Value, ou valor da empresa |
| **EBITDA** | Resultado operacional antes de juros, impostos, depreciação e amortização |
| **EBIT** | Resultado antes de juros e impostos |
| **PSR** | Relação entre valor de mercado e receita |
| **ROE** | Retorno sobre o patrimônio líquido |
| **ROIC** | Retorno sobre o capital investido |
| **Margem Líquida** | Percentual da receita convertido em lucro líquido |
| **CAGR** | Taxa de crescimento anual composta |
| **DY** | Dividend Yield |
| **Payout** | Percentual do lucro distribuído aos acionistas |
| **Vacância Física** | Espaço físico desocupado em um FII |
| **Vacância Financeira** | Receita que deixa de ser recebida devido à vacância |
| **Liquidez** | Facilidade de comprar ou vender um ativo |
| **Tag Along** | Mecanismo de proteção ao acionista minoritário |
| **Governança** | Práticas de administração, transparência e relacionamento com acionistas |
| **Margem de Segurança** | Diferença entre o valor considerado adequado e o preço pago |

---

# ♻️ Prompts Reutilizáveis

## 🔎 Prompt para estudar um indicador

```text
Explique o indicador [NOME DO INDICADOR] de forma simples.

Apresente:
1. O que ele mede;
2. Como é calculado;
3. Como interpretar;
4. O que pode ser considerado positivo ou negativo;
5. Quais são as principais armadilhas;
6. Como ele deve ser analisado junto com outros indicadores.

Sempre considere o contexto do setor e evite conclusões baseadas
em um único indicador.
```

---

## 📊 Prompt para analisar uma empresa

```text
Analise a empresa [NOME] utilizando uma abordagem de análise
fundamentalista.

Organize a análise em:

1. Valuation;
2. Rentabilidade;
3. Endividamento;
4. Crescimento;
5. Proventos;
6. Governança;
7. Vantagens competitivas;
8. Principais riscos.

Não conclua que a empresa é boa ou ruim com base em apenas um indicador.
Mostre os pontos positivos, negativos e as informações que precisam
de investigação adicional.
```

---

## 🏢 Prompt para analisar um FII

```text
Analise o FII [TICKER] considerando:

- P/VP;
- Dividend Yield;
- vacância física;
- vacância financeira;
- liquidez;
- qualidade dos imóveis;
- concentração de inquilinos;
- contratos;
- qualidade da gestão;
- endividamento;
- principais riscos.

Separe a análise entre pontos positivos, pontos de atenção e riscos.

Não considere um Dividend Yield elevado como evidência suficiente
de qualidade.
```

---

## 🧩 Prompt para comparação

```text
Compare [ATIVO A] e [ATIVO B] utilizando os mesmos critérios.

Crie uma análise organizada por:
- valuation;
- rentabilidade;
- crescimento;
- endividamento;
- proventos;
- qualidade;
- riscos.

Explique em quais critérios cada ativo se destaca e quais informações
seriam necessárias para uma conclusão mais segura.
```

---

## 🧠 Prompt para revisão

```text
Quero revisar análise fundamentalista.

Faça 10 perguntas progressivas sobre:
- valuation;
- rentabilidade;
- endividamento;
- crescimento;
- dividendos;
- FIIs;
- análise qualitativa.

Comece com perguntas fáceis e aumente gradualmente a dificuldade.

Não mostre as respostas imediatamente. Aguarde minha resposta,
avalie meu raciocínio e explique meus erros.
```

---

# 💡 Principais Aprendizados

Este projeto mostrou que utilizar Inteligência Artificial para estudar não significa simplesmente pedir uma resposta e copiá-la.

O processo mais importante foi aprender a:

- fazer perguntas melhores;
- dividir problemas complexos em partes menores;
- comparar informações;
- questionar respostas;
- identificar possíveis limitações;
- organizar conhecimento;
- transformar pesquisa em material reutilizável.

No contexto da análise de investimentos, um dos principais aprendizados foi que **nenhum indicador deve ser utilizado isoladamente**.

A análise precisa combinar números com contexto, qualidade do negócio, riscos, gestão e preço.

A filosofia apresentada no material também reforça a importância da disciplina e da margem de segurança, especialmente para quem busca uma estratégia de longo prazo.

---

# 🚀 Conclusão

O NotebookLM foi utilizado neste projeto como uma ferramenta de aprendizagem ativa para transformar diversas fontes em um material organizado de estudo.

O resultado foi um miniguia que reúne conceitos de análise fundamentalista, indicadores financeiros, critérios de avaliação de FIIs, análise qualitativa, glossário e prompts reutilizáveis.

Mais do que criar uma lista de indicadores, o objetivo foi desenvolver um **processo de análise**, no qual cada informação é questionada e colocada em contexto.

> 📌 **Importante:** este projeto possui finalidade educacional. As informações apresentadas não constituem recomendação de compra ou venda de ativos. Rentabilidade passada não garante resultados futuros.

---

# 🔗 Referências Complementares

- [Status Invest](https://statusinvest.com.br/)
- [Investidor10](https://investidor10.com.br/)
- [Daycoval — Como analisar um FII](https://blog.daycoval.com.br/como-analisar-um-fii/)

---

## 📌 Estrutura do Projeto

```text
📁 projeto-notebooklm
│
├── 📄 README.md
└── 📚 fontes/
```

O `README.md` concentra a documentação do desafio e o resultado final do Caderno Temático.

---

### 😎 Desafio DIO

Projeto desenvolvido como parte do desafio de aprendizagem ativa com Inteligência Artificial da **DIO**, utilizando o **NotebookLM** para curadoria, exploração e organização do conhecimento.
[DIO](https://www.dio.me)
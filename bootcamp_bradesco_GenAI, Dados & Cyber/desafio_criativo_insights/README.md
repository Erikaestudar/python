# 🎯 Kit de Prompts — Análise de Feedbacks de Clientes Bancários

## Sobre este documento

Este documento reúne o **prompt principal** de análise de feedbacks de clientes bancários e um conjunto de **prompts auxiliares** de apoio, construídos ao longo do Desafio de Feedback de Clientes Bancários (avaliação de dataset → definição de intenção → contexto e restrições → construção e auditoria do prompt).

Os prompts auxiliares não substituem o prompt principal — eles servem para **verificar, revisar e reutilizar** o trabalho em diferentes momentos, seja rodando este mesmo prompt em outra IA, checando os resultados obtidos, ou aplicando o processo a um novo dataset no futuro.

---

## 📌 Sumário

1. [Prompt Principal — Análise de Feedbacks](#1-🧩-prompt-principal--análise-de-feedbacks)
2. Prompts Auxiliares
   - [2.1 Verificar possíveis alucinações](#21-verificar-possíveis-alucinações)
   - [2.2 Avaliar se uma conclusão possui evidência nos dados](#22-avaliar-se-uma-conclusão-possui-evidência-nos-dados)
   - [2.3 Encontrar ambiguidades em um prompt](#23-encontrar-ambiguidades-em-um-prompt)
   - [2.4 Analisar um dataset (versão genérica)](#24-analisar-um-dataset-versão-genérica)
3. [Como usar este kit — fluxo sugerido](#3-🔄-como-usar-este-kit--fluxo-sugerido)
4. [Por que este prompt foi construído assim](#4-💡-por-que-este-prompt-foi-construído-assim)

---

## 1. 🧩 Prompt Principal — Análise de Feedbacks

**Dataset de referência:** `cfpb_complaints_preparado.csv` — 230 reclamações de produtos bancários tradicionais (excluindo credit reporting), extraídas de uma amostra da base pública do CFPB (Consumer Financial Protection Bureau), com colunas sensíveis/desnecessárias removidas (zip_code, complaint_id, date_sent_to_company, consumer_consent).

### 📋 Prompt

```text
Atue como um analista de produto/operações especializado em experiência do cliente bancário.

Sua tarefa é analisar reclamações de clientes sobre produtos bancários tradicionais (cobrança de dívidas, contas correntes/poupança, cartão de crédito, hipoteca, transferência de dinheiro, empréstimo estudantil, entre outros) para identificar temas recorrentes, avaliar a qualidade da resposta da empresa e priorizar quais problemas merecem atenção primeiro.

Contexto: As reclamações foram registradas junto ao CFPB (Consumer Financial Protection Bureau) entre 2012 e 2026. O resultado será usado por um time de produto/operações para decidir onde investir esforço de melhoria de processo ou produto.

Dados disponíveis: Você receberá um arquivo com 230 reclamações, contendo: produto, subproduto, problema relatado (issue/sub_issue), narrativa do cliente (texto livre, disponível em ~45% dos registros), resposta da empresa, se a resposta foi dentro do prazo, canal de envio, data, estado e marcadores especiais (ex: militar, idoso).

Instruções de análise:

- Classifique as reclamações por produto e por tema/problema (issue).
- Identifique os padrões mais recorrentes, com base na frequência real de ocorrência nos dados.
- Avalie a qualidade da resposta da empresa combinando o tipo de resolução (company_response) e o cumprimento de prazo (timely_response).
- Quando avaliar sentimento ou urgência, deixe claro que isso é uma inferência sua a partir do texto, não um dado direto do dataset — pois essas colunas não existem na base.
- Aponte evidências reais nos dados, usando trechos curtos das narrativas disponíveis, quando existirem.
- Se um tema tiver poucas narrativas de evidência (menos de 5), sinalize isso explicitamente como limitação de amostra.
- Quando um campo estiver ausente para um registro (ex: sub_issue, company_public_response), não presuma o valor nem ignore silenciosamente — trate como "não informado" e, se isso afetar uma conclusão, mencione a limitação.
- Ao priorizar problemas, use como critério explícito a combinação de: (1) volume de ocorrências, (2) qualidade da resposta da empresa (resolução + prazo), e (3) concentração recente de casos (últimos anos da base) — deixando claro qual peso cada fator teve na priorização.
- Considere a distribuição temporal das reclamações (2012–2026): dê mais peso a padrões que aparecem de forma concentrada em anos recentes, e sinalize quando um padrão relevante for baseado majoritariamente em registros antigos.
- Sugira ações práticas e realistas para o time de produto/operações, apoiadas nos padrões encontrados.
- Não trate a coluna consumer_disputed como indicador confiável — está ausente em 95% dos registros.

Formato da resposta:

1. Resumo executivo (3 a 5 linhas) com a visão geral dos achados.
2. Tabela com: produto/tema, evidência (trecho de narrativa quando disponível), tipo de resposta da empresa, e ação sugerida.
3. Lista final com as 3 a 5 prioridades mais importantes, cada uma com uma justificativa curta baseada nos dados (ex: volume + qualidade de resposta + recência).
4. Um parágrafo final de "Limitações da análise", resumindo o que os dados não permitem concluir com segurança (ex: ausência de nota de satisfação, cobertura parcial de narrativas, período temporal amplo).

Restrições:

- Use apenas os dados fornecidos no arquivo. Não use conhecimento externo sobre bancos ou sobre as empresas citadas.
- Não invente números, causas, sentimentos ou conclusões que não estejam sustentados pelos dados.
- Diferencie claramente o que é fato extraído diretamente dos dados do que é inferência sua.
- Não exponha nem tente reconstruir informações que possam identificar um cliente específico, mesmo que o texto já tenha nomes e dados removidos pelo CFPB (marcados como XXXX).
- Se a informação disponível for insuficiente para responder algum ponto, diga isso explicitamente em vez de preencher a lacuna.
- Use linguagem direta, objetiva e orientada à ação, adequada a um time de produto/operações.
```

### 🧠 Como este prompt foi construído

- **Etapa 0:** avaliação do dataset original (1.000 registros) e preparação de um recorte de 230 registros focado em produtos bancários tradicionais, com colunas sensíveis removidas.
- **Etapa 1:** intenção definida — foco combinado (temas + qualidade de resposta + priorização), público = time de produto/operações, entrega em 3 camadas.
- **Etapa 2:** contexto, dados disponíveis, critérios de análise viáveis e restrições contra alucinação e exposição de dados sensíveis.
- **Etapa 3:** montagem do prompt no papel de "analista de produto/operações", seguida de auditoria que resultou em 4 melhorias: tratamento de dados ausentes, critério objetivo de priorização, consideração de recência temporal e seção final de limitações.

---

## 2. 🛠️ Prompts Auxiliares

### 2.1 Verificar possíveis alucinações

**🎯 Objetivo:** Conferir se a resposta gerada pela IA (ao aplicar o prompt principal nos dados reais) contém alguma afirmação que não esteja de fato sustentada pelos dados fornecidos.

**🕐 Quando utilizar:** Depois de rodar o prompt principal em uma IA com os dados reais, antes de usar o resultado para tomar qualquer decisão.

**📋 Prompt:**
```text
Você vai revisar uma análise gerada por outra IA a partir de um conjunto de dados de reclamações de clientes.

Vou te fornecer:
1. Os dados originais que foram analisados;
2. A análise/resposta gerada pela IA.

Sua tarefa é conferir, afirmação por afirmação, se cada uma está de fato sustentada pelos dados fornecidos.

Para cada afirmação da análise, classifique como:
- CONFIRMADA: o dado existe e sustenta diretamente a afirmação;
- INFERIDA: a afirmação é uma interpretação razoável, mas não um dado literal (ex: sentimento, urgência);
- NÃO SUSTENTADA: não há como confirmar essa afirmação nos dados fornecidos — pode ser uma alucinação.

Liste as afirmações problemáticas separadamente, explicando por que não encontraram respaldo nos dados.

Não corrija a análise original — apenas aponte os problemas encontrados.
```

**🔍 O que esperar da IA:** Uma lista organizada por afirmação, com a classificação de cada uma e a justificativa. Se a análise estiver limpa, a IA deve dizer isso claramente, não inventar problemas para parecer útil.

**⚠️ Cuidados:** Essa verificação também pode errar — trate como uma segunda opinião, não como verdade absoluta. Vale conferir manualmente pelo menos as afirmações marcadas como "NÃO SUSTENTADA" antes de descartar algo da análise original.

---

### 2.2 Avaliar se uma conclusão possui evidência nos dados

**🎯 Objetivo:** Testar uma conclusão específica (não a análise toda) para saber se ela é defensável com os dados que você tem.

**🕐 Quando utilizar:** Quando você (ou alguém do time) quiser usar uma conclusão específica em uma apresentação, decisão ou documento, e quiser ter certeza de que ela se sustenta.

**📋 Prompt:**
```text
Vou te apresentar uma conclusão específica extraída de uma análise de dados, e o conjunto de dados original.

Conclusão a verificar: [cole aqui a frase/conclusão exata]

Dados disponíveis: [cole aqui os dados relevantes ou a amostra]

Sua tarefa:
1. Diga se essa conclusão é totalmente sustentada, parcialmente sustentada, ou não sustentada pelos dados.
2. Aponte exatamente quais registros/evidências sustentam (ou não) essa conclusão.
3. Se a conclusão for parcial, reescreva uma versão mais precisa que reflita exatamente o que os dados mostram, sem exagerar nem generalizar além do que é possível.
4. Se a base de evidência for pequena, diga isso explicitamente.

Não invente evidências que não estejam nos dados fornecidos.
```

**🔍 O que esperar da IA:** Um veredito claro (sustentada/parcial/não sustentada), com a evidência apontada diretamente, e uma versão corrigida da conclusão quando necessário.

**⚠️ Cuidados:** Essa verificação é tão boa quanto os dados que você cola no prompt — se você colar só uma amostra parcial, a resposta pode ficar incompleta. Sempre que possível, forneça o conjunto de dados completo relevante à conclusão.

---

### 2.3 Encontrar ambiguidades em um prompt

**🎯 Objetivo:** Revisar um prompt (como o prompt principal deste kit) para identificar instruções pouco claras, contraditórias ou que podem ser interpretadas de formas diferentes por IAs diferentes.

**🕐 Quando utilizar:** Antes de reutilizar esse prompt em outro dataset, outra IA, ou outro contexto de negócio — ou sempre que perceber que respostas de execuções diferentes do mesmo prompt variam muito entre si.

**📋 Prompt:**
```text
Você vai revisar o prompt abaixo, que será usado para orientar uma IA a analisar dados.

Prompt a revisar:
[cole aqui o prompt completo]

Sua tarefa é encontrar:
1. Instruções que podem ser interpretadas de mais de uma forma;
2. Termos vagos que não têm uma definição clara dentro do próprio prompt (ex: "problemas importantes", "impacto relevante");
3. Instruções que podem entrar em conflito entre si;
4. Pontos em que o prompt presume um dado ou contexto que talvez não exista.

Para cada ambiguidade encontrada, explique:
- Qual é o problema;
- Como duas IAs diferentes poderiam interpretar aquele trecho de formas diferentes;
- Uma sugestão de como tornar a instrução mais específica.

Não reescreva o prompt inteiro — apenas aponte os problemas e sugestões pontuais.
```

**🔍 O que esperar da IA:** Uma lista de pontos ambíguos, cada um com explicação e sugestão de ajuste. Nem todo prompt terá muitos problemas — se o prompt já estiver bem específico, a IA deve indicar isso.

**⚠️ Cuidados:** Nem toda "ambiguidade" apontada precisa virar uma mudança — use seu julgamento sobre quais realmente importam para o seu caso de uso antes de reescrever o prompt.

---

### 2.4 Analisar um dataset (versão genérica)

**🎯 Objetivo:** Servir como ponto de partida para avaliar qualquer novo dataset de feedback/reclamações antes de construir um prompt de análise em cima dele — reproduzindo o tipo de avaliação feita na Etapa 0 deste desafio, mas de forma genérica e reutilizável.

**🕐 Quando utilizar:** No início de um novo desafio ou projeto, antes de decidir se um dataset é adequado para análise com IA.

**📋 Prompt:**
```text
Você vai me ajudar a avaliar um dataset antes de eu usá-lo em uma análise com IA.

Vou te fornecer uma amostra ou a estrutura do dataset.

Sua tarefa:
1. Identifique quantidade de registros, colunas e o tipo de informação em cada uma (categórica, texto livre, numérica, data).
2. Aponte quais colunas têm dados ausentes e em que proporção.
3. Identifique se há texto livre disponível e em que proporção dos registros.
4. Identifique se há dados pessoais ou potencialmente sensíveis (nomes, documentos, contato, localização detalhada, informações financeiras identificáveis).
5. Avalie se o dataset é adequado para o objetivo que eu descrever, explicando por quê.
6. Aponte limitações reais — não hipotéticas — que encontrar nos dados.

Regras:
- Use apenas informações que você pode verificar diretamente na amostra/estrutura fornecida.
- Se não conseguir determinar algo, diga "não é possível determinar isso com os dados disponíveis" em vez de supor.

Objetivo da análise que pretendo fazer: [descreva aqui]
```

**🔍 O que esperar da IA:** Um raio-x do dataset (estrutura, ausências, sensibilidade, adequação), parecido com o que foi feito na Etapa 0 deste desafio — mas você precisa fornecer a amostra ou estrutura real, não só o nome do arquivo.

**⚠️ Cuidados:** Esse prompt só funciona bem se a IA tiver acesso real aos dados (upload de arquivo, amostra colada no texto, etc.). Se a IA não tiver acesso e mesmo assim responder com números específicos, isso é sinal de alucinação — desconfie.

---

## 3. 🔄 Como usar este kit — fluxo sugerido

1. Rode o **Prompt Principal** (seção 1) na IA com os dados reais.
2. Use o prompt **2.1 (alucinações)** para checar a resposta gerada.
3. Se alguma conclusão específica for usada em decisão, valide com **2.2**.
4. Antes de reutilizar o Prompt Principal em outro dataset/contexto, rode **2.3** para revisar ambiguidades.
5. Ao encontrar um novo dataset no futuro, comece por **2.4** antes de tudo.

---

## 4. 💡 Por que este prompt foi construído assim

Este prompt foi construído a partir dos dados reais disponíveis, não de suposições genéricas: o dataset foi primeiro avaliado e recortado (excluindo "Credit reporting", que dominava 77% da base e mascarava os demais produtos, e removendo colunas sensíveis ou irrelevantes, como zip_code e metadados técnicos) para refletir de fato o escopo de "feedback bancário" do desafio. Como o dataset não possui nota de satisfação nem sentimento pré-classificado, o prompt instrui a IA a tratar sentimento e urgência explicitamente como inferências, nunca como fatos diretos, e a não usar colunas com alta ausência de dados (como consumer_disputed, 95% vazia) como critério confiável. Essas restrições não são genéricas — nasceram de limitações reais encontradas na análise da Etapa 0. Por fim, o prompt principal é complementado por prompts auxiliares de verificação (como o de checagem de alucinações), que atuam depois da análise para confirmar se cada afirmação tem respaldo real nos dados antes de qualquer decisão ser tomada. No conjunto, isso ajuda a IA a produzir uma análise mais confiável porque força a separação clara entre fato, inferência e limitação, em vez de gerar conclusões genéricas, infladas ou não sustentáveis.

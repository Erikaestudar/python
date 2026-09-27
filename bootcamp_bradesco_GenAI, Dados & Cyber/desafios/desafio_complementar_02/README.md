# Desafio 2 — Histórico de transações únicas

## 🎯 Objetivo

Reforçar o conhecimento de:

- `input()`
- `split()`
- listas
- `for`
- `if`
- `in` / `not in`
- `append()`
- `join()`

E acrescentar um pequeno nível de dificuldade: além de remover transações duplicadas, você deverá **classificar as transações únicas de acordo com uma regra definida pelo enunciado**.

---

## 🧩 Enunciado

O Banco ByteSafe possui um sistema que registra identificadores de operações realizadas durante o dia.

Por causa de uma falha no sistema, uma mesma operação pode aparecer várias vezes no histórico.

Sua tarefa é criar um programa que:

1. leia os identificadores das operações;
2. remova as repetições, mantendo somente a primeira ocorrência;
3. conte quantas operações diferentes foram encontradas;
4. imprima primeiro a lista de operações únicas;
5. na segunda linha, informe a quantidade de operações diferentes.

---

## 📥 Entrada

Uma única linha contendo identificadores de operações separados por espaços.

Cada identificador é uma sequência de caracteres sem espaços.

---

## 📤 Saída

A primeira linha deve conter os identificadores sem repetição, separados por espaço e na ordem da primeira ocorrência.

A segunda linha deve conter a quantidade de identificadores diferentes.

---

## 🧪 Exemplos

### Exemplo 1

Entrada:

```text
TX01 TX02 TX01 TX03 TX02 TX04
```

Saída:

```text
TX01 TX02 TX03 TX04
4
```

### Exemplo 2

Entrada:

```text
A1 A1 A1 B2 B2 C3
```

Saída:

```text
A1 B2 C3
3
```

### Exemplo 3

Entrada:

```text
Q1 W2 E3
```

Saída:

```text
Q1 W2 E3
3
```

---

## 🚫 Restrições

- Não use bibliotecas externas.
- Não use `set()`.
- Não use funções prontas para eliminar duplicatas.
- Mantenha a ordem da primeira ocorrência.
- Use uma lista para controlar os itens que já foram encontrados.

---

## 💡 Dicas graduais

### Dica 1

Você já resolveu a parte de remover duplicatas no desafio anterior.

Comece pensando:

> "Como posso guardar apenas uma ocorrência de cada identificador?"

### Dica 2

Você pode ter uma lista contendo as transações únicas.

A cada transação:

> "Ela já está nessa lista?"

Se não estiver, adicione.

### Dica 3

Depois que a lista estiver pronta, pense:

> "Quantos elementos existem nessa lista?"

Existe uma função do Python que permite descobrir o tamanho de uma lista.

### ⚠️ Atenção

Não tente resolver tudo de uma vez.

Primeiro faça a remoção das duplicatas.

Depois faça a contagem.

---

## 🏆 Critério de conclusão

Seu programa deverá:

- ler a entrada;
- remover duplicatas;
- preservar a ordem da primeira ocorrência;
- imprimir as operações únicas;
- imprimir a quantidade de operações diferentes.

---

## 🆘 Espaço para instruções caso você não consiga completar

> **Instruções de ajuda:**  
> 
> _Escreva aqui as instruções/dicas adicionais que deverão ser fornecidas caso eu não consiga resolver o desafio._

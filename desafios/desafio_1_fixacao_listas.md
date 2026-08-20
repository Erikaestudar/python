# Desafio 1 — Limpando registros de clientes

## 🎯 Objetivo

Fixar os conhecimentos praticados nos desafios anteriores:

- `input()`
- `split()`
- listas
- `for`
- `if`
- `in` / `not in`
- `append()`
- `join()`

Você deverá remover itens duplicados **mantendo a ordem da primeira ocorrência**.

---

## 🧩 Enunciado

Uma empresa possui uma lista de códigos de clientes que participaram de uma campanha. Por causa de um problema no sistema, alguns códigos foram registrados mais de uma vez.

Você precisa criar um programa que receba uma única linha contendo os códigos separados por espaço e produza uma nova linha contendo cada código **apenas uma vez**, mantendo a ordem em que apareceu pela primeira vez.

### Exemplo

Entrada:

```text
CLI01 CLI02 CLI01 CLI03 CLI02 CLI04
```

Saída:

```text
CLI01 CLI02 CLI03 CLI04
```

---

## 📥 Entrada

Uma única linha contendo identificadores de clientes separados por espaços.

Os identificadores não possuem espaços dentro deles.

---

## 📤 Saída

Uma única linha contendo os identificadores sem repetições, separados por espaço, mantendo a ordem da primeira ocorrência.

---

## 🧪 Exemplos

### Exemplo 1

Entrada:

```text
CLI01 CLI02 CLI01 CLI03 CLI02
```

Saída:

```text
CLI01 CLI02 CLI03
```

### Exemplo 2

Entrada:

```text
A10 B20 C30
```

Saída:

```text
A10 B20 C30
```

### Exemplo 3

Entrada:

```text
X X X Y Y Z X
```

Saída:

```text
X Y Z
```

---

## 🚫 Restrições

- Não use bibliotecas externas.
- Não use `set()` para resolver o problema.
- Mantenha a ordem da primeira ocorrência.
- Tente resolver usando as estruturas que você acabou de estudar.

---

## 💡 Dica inicial

Pense em duas listas:

1. uma lista com todos os códigos recebidos;
2. outra lista para guardar somente os códigos que ainda não apareceram.

Antes de pedir ajuda, tente construir a solução sozinha.

**Importante:** não procure uma solução pronta. O objetivo é praticar o raciocínio.

---

## 🏆 Critério de conclusão

Você terá resolvido o desafio quando o programa:

- receber a entrada;
- identificar os códigos repetidos;
- manter somente a primeira ocorrência;
- preservar a ordem;
- imprimir o resultado no formato solicitado.

---

## 🆘 Espaço para instruções caso você não consiga completar

> **Instruções de ajuda:**  
> 
> _Escreva aqui as instruções/dicas adicionais que deverão ser fornecidas caso eu não consiga resolver o desafio._

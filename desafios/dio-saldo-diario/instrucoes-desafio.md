# Calculando o Saldo Diário

## Desafio

Você faz parte da equipe de tecnologia de um grande banco e recebeu uma missão importante: ajudar o setor financeiro a organizar rapidamente os lançamentos diários de despesas e receitas.

Cada lançamento é registrado como uma string contendo o tipo (`D` para despesa ou `R` para receita), seguido do valor em reais e separados por espaço. Sua tarefa é criar uma função que, ao receber uma lista desses lançamentos em uma única linha, calcule o saldo final do dia.

O saldo é a soma de todas as receitas menos a soma de todas as despesas. O resultado deve ser apresentado com duas casas decimais, mesmo que o valor seja inteiro.

> **Restrição:** não utilize bibliotecas externas.

## Tarefa

Implemente uma função que leia uma linha contendo lançamentos separados por vírgula, processe cada um conforme o tipo e valor, e imprima o saldo final do dia no formato especificado.

Considere que todos os valores são números positivos e que pode haver tanto receitas quanto despesas, ou apenas um dos tipos.

## Entrada

Uma única linha contendo lançamentos separados por vírgula. Cada lançamento é composto por uma letra (`D` ou `R`), seguida de um espaço e um valor decimal positivo.

## Saída

Uma única linha contendo o saldo final do dia, com duas casas decimais.

## Exemplos

| Entrada                    |     Saída |
| -------------------------- | --------: |
| `R 100.00,D 50.00,R 20.00` |   `70.00` |
| `R 10.00,R 25.50,R 14.50`  |   `50.00` |
| `R 200.00`                 |  `200.00` |
| `D 100.00,D 50.00`         | `-150.00` |

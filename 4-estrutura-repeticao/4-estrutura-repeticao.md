# 4 - Estruturas de Decisão
[🔙 Voltar](../README.md)
## O que é?
As estruturas de decisão são elementos da programação que permitem que o código execute diferentes ações com base em condições que retornam `True` ou `False`. Por exemplo, uma condição como `valor > 10` determina o fluxo do programa, permitindo a execução de blocos de código conforme a veracidade da condição.

---


## Estruturas de Decisão: `if`

Sintaxe:
```python
if (expressao_logica):
    # Bloco de instrução
```

O comando `if` executa um bloco de instruções apenas se a expressão for verdadeira (`True`).

> O bloco deve ser precedido por um recuo, ou indentação, que define quais partes do código pertencem à condição, garantindo a correta associação da execução.

---

## Estruturas de Decisão: `else`

Sintaxe:
```python
if (expressao_logica):
    # Primeiro bloco de instrução
else:
    # Segundo bloco de instrução.
```

O comando `else` complementa o `if`, executando um bloco de instruções apenas quando a condição do `if` é false (`False`).

---

## Estruturas de Decisão: `elif`

Sintaxe:
```python
if (expressao_logica_1):
    # Primeiro bloco de instrução
if (expressao_logica_2):
    # Segundo bloco de instrução.
else:
    # Terceiro bloco de instrução.
```

O comando `elif` permite verificar condições intermediárias após um `if`, executando seu bloco apenas se a condição anterior for falsa (`False`). Isso é útil para testar várias expressões em sequência.

> **Observação**: O uso excessivo de `elif` pode tornar o código menos legível e mais difícil de manter.
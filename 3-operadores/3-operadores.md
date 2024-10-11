# 3 - Operadores

## O que são comentários?

Comentários não afetam a execução do código e não influenciam seu funcionamento.

> Em Python, os comentários são inseridos usando o símbolo `#`.

Exemplo:

```python
# x = 10
x = 20
```

No entanto, são uma ferramenta valiosa para explicar o código e torná-lo mais compreensível para outros programadores.

---

## Operadores Aritméticos

Operadores aritméticos são símbolos que representam operações matemáticas básicas, como soma, subtração, multiplicação e divisão.

| Operação         | Símbolos | Exemplo de código           |
| ---------------- | -------- | --------------------------- |
| Adição           | `+`      | `soma = 5 + 3`              |
| Subtração        | `-`      | `menos = 10 - 4`            |
| Multiplicação    | `*`      | `produto = 7 * 2`           |
| Divisão          | `/`      | `divisao = 9 / 3`           |
| Resto da divisão | `%`      | `resto = 10 % 4`            |
| Divisão inteira  | `//`     | `divisao_inteira = 10 // 4` |
| Exponenciação    | `**`     | `exponencial = 2 ** 3`      |

---

## Operadores Relacionais

Operadores de comparação, ou relacionais, são usados para comparar valores e gerar expressões lógicas que resultam em dois possíveis valores: `True` ou `False`.

| Operação         | Símbolos | Exemplo de código       |
| ---------------- | -------- | ----------------------- |
| Igual a          | `==`     | `3 == "3" # False`      |
| Diferente de     | `!=`     | `10 != 10.0 # False`    |
| Maior que        | `>`      | `100 > 99 # True`       |
| Menor que        | `<`      | `1 < 100 # True`        |
| Maior ou igual a | `>=`     | `100 >= (10*10) # True` |
| Menor ou igual a | `<=`     | `10 <= 9 # False`       |

---

## Operadores lógicos

Os operadores lógicos são utilizados para realizar operações entre valores booleanos (ou lógicos). 

Os principais operadores lógicos em programação são: `and` (e), `or` (ou) e `not` (não).

Tabela verdade para `a and b`:

| Valor a | Valor b | Resultado |
| ------- | ------- | --------- |
| `True`  | `True`  | `True`    |
| `True`  | `False` | `False`   |
| `False` | `True`  | `False`   |
| `False` | `False` | `False`   |

Tabela verdade para `a or b`:

| Valor a | Valor b | Resultado |
| ------- | ------- | --------- |
| `True`  | `True`  | `True`    |
| `True`  | `False` | `True`    |
| `False` | `True`  |           |
| `False` | `False` | `False`   |

Tabela verdade para `not a`:

| Valor a | Resultado |
| ------- | --------- |
| `True`  | `False`   |
| `False` | `True`    |

## Expressões

As expressões podem ser compostas por variáveis, operadores relacionais e operadores lógicos.
- Se a expressão contiver apenas operadores aritméticos, o resultado será um número.
- Se a expressão inclui operadores lógicos, o resultado será do tipo lógico ou booleano.

Exemplo:
- Expressão aritmética: `(x + y) * z`
- Expressão lógica: `(x < y) and (y < z)`

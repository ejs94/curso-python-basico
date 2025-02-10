# 11 - Funções Lambda: map, filter e reduce
[🔙 Voltar](../README.md)

## O que são?

As funções lambda são funções anônimas, pequenas e definidas sem um nome, que permitem a criação de funções em apenas uma linha. Uma função lambda pode receber múltiplos argumentos, mas deve conter apenas uma expressão. Enquanto funções tradicionais são definidas com a palavra-chave `def`, as funções anônimas em Python utilizam a palavra-chave `lambda`.

### Sintaxe:
```python
lambda argumento: expressão
```

As funções lambda são frequentemente empregadas quando uma função simples é necessária apenas uma vez ou por um curto período no código. Seu uso mais comum é como argumento para funções de ordem superior, que são aquelas que aceitam outras funções como parâmetros. Elas também são amplamente utilizadas em conjunto com funções embutidas como `map()`, `filter()` e `reduce()`.

### Exemplo:

```python
# Função lambda que adiciona 5 ao argumento de entrada
f = lambda x: x + 5
val1 = f(3)    # Resultado: 8
val2 = f(20)   # Resultado: 25
print(val1, val2)

# Função lambda que calcula o quíntuplo de dois argumentos de entrada e retorna o resultado
f = lambda x, y: x * y
val3 = f(3, 5)  # Resultado: 15
val4 = f(2, 10)  # Resultado: 20
print(val3, val4)
```

### Observações:
As funções lambda são úteis para simplificar o código em situações em que uma função completa seria excessiva. Elas permitem expressar operações simples de forma concisa, especialmente quando utilizadas com funções como `map()`, `filter()` e `reduce()`, que aplicam operações a sequências de elementos.

## Ordenação Personalizada Usando a Função sorted

A função `sorted()` é utilizada para ordenar iteráveis, como listas, de forma flexível. Você pode especificar a ordem de classificação e, opcionalmente, fornecer uma função de chave para determinar como os elementos devem ser ordenados.

### Sintaxe:
```python
sorted(iterável, key=None, reverse=False)
```

- **iterável:** O objeto que você deseja classificar (ex: lista, tupla).
- **key:** Uma função que extrai um valor para comparação. Pode ser uma função lambda.
- **reverse:** Se `True`, a lista será classificada em ordem decrescente.

### Exemplo de Uso do sorted:

```python
# Lista de pontos 2D
pontos2D = [(2, 4), (1, 10), (3, -1), (5, 0)]
ordenados_por_y = sorted(pontos2D, key=lambda x: x[1])
print("Ordenados por Y:", ordenados_por_y)
```

```python
# Lista com números negativos e positivos
minha_lista = [3, -2, 1, -4, 2, 0]
ordenados_por_absoluto = sorted(minha_lista, key=lambda x: abs(x))
print("Ordenados por valor absoluto:", ordenados_por_absoluto)
```

**Saídas:**
```
Ordenados por Y: [(3, -1), (5, 0), (2, 4), (1, 10)]
Ordenados por valor absoluto: [-2, 0, 1, 2, 3, -4]
```

### Usando Lambda para a Função map

`map(func, seq)` transforma cada elemento de acordo com a função fornecida.

```python
a = [2, 4, 6, 8, 10]
b = list(map(lambda x: x + 3, a))

# Contudo, prefira a compreensão de listas
# Use map se já tiver uma função definida
c = [x + 3 for x in a]
print(b)
print(c)
```

**Saídas:**
```
[5, 7, 9, 11, 13]
[5, 7, 9, 11, 13]
```

### Usando Lambda para a Função filter

`filter(func, seq)` retorna todos os elementos para os quais a função avalia como True.

```python
a = [1, 3, 5, 7, 9, 2, 4, 6, 8]
b = list(filter(lambda x: (x > 5), a))

# Entretanto, o mesmo pode ser alcançado com compreensão de listas
c = [x for x in a if x > 5]
print(b)
print(c)
```

**Saídas:**
```
[7, 9, 6, 8]
[7, 9, 6, 8]
```

### Função reduce

`reduce(func, seq)` aplica repetidamente a função aos elementos e retorna um único valor. A função recebe 2 argumentos.

```python
from functools import reduce

a = [2, 3, 4, 5]
produto_a = reduce(lambda x, y: x * y, a)
print(produto_a)

soma_a = reduce(lambda x, y: x + y, a)
print(soma_a)
```

**Saídas:**
```
120
14
``` 

## Conclusão:

Esse capitulos mostramos como as funções `lambda` podem ser úteis para simplificar operações em listas e trabalhar com funções de ordem superior em Python, além de ilustrar como essa função possibilita expandir o uso da função `sorted()` para realizar ordenações personalizadas.
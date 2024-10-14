# 5 - Estruturas de Repetição
[🔙 Voltar](../README.md)
## O que é?

As estruturas de repetição são mecanismos que possibilitam a execução contínua de um bloco de código enquanto uma determinada condição for verdadeira. Elas são fundamentais para automatizar tarefas e manipular conjuntos de dados de forma eficiente, evitando a necessidade de escrever o mesmo código múltiplas vezes.

---

## Estruturas de Repetição: `while`

A estrutura de repetição `while` em Python permite a execução de um bloco de código enquanto uma condição específica for verdadeira. Essa estrutura é útil quando o número de iterações não é conhecido antecipadamente e depende de uma condição que pode mudar durante a execução do programa.

### Sintaxe
A sintaxe básica do `while` é a seguinte:

```python
while condição:
    # Bloco de instruções
```

- **`condição`**: Uma expressão que é avaliada antes de cada iteração. Se for verdadeira, o bloco de instruções dentro do `while` é executado.
- **Bloco de instruções**: O conjunto de comandos que será repetido enquanto a condição for verdadeira.

### Exemplo
Abaixo está um exemplo que demonstra como usar o `while` para contar de 1 a 5:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1  # Incrementa o contador em 1
```

**Saída:**
```
1
2
3
4
5
```

### Considerações
- É importante garantir que a condição eventualmente se torne falsa; caso contrário, o programa entrará em um loop infinito, o que pode travar a aplicação.
- O `while` é frequentemente utilizado em situações onde a condição de parada não é conhecida de antemão, como em leituras de entrada do usuário ou em processamentos de dados até que uma condição específica seja atendida. 

Utilizar `while` de forma cuidadosa pode aumentar a flexibilidade do seu código e permitir a implementação de lógicas complexas de repetição.

---

## Estruturas de Repetição: `for`

A estrutura de repetição `for` em Python permite iterar sobre uma sequência (como listas, tuplas, strings ou objetos de um iterável). Essa estrutura é especialmente útil quando se sabe exatamente quantas vezes um bloco de código deve ser executado, tornando o código mais legível e conciso.

### Sintaxe
A sintaxe básica do `for` é a seguinte:

```python
for item in sequência:
    # Bloco de instruções
```

- **`item`**: A variável que assume o valor de cada elemento na sequência a cada iteração.
- **`sequência`**: Qualquer objeto iterável, como listas, tuplas, strings ou intervalos.

### Exemplo
Abaixo está um exemplo que demonstra como usar o `for` para iterar sobre uma lista de números e imprimir cada um deles:

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

**Saída:**
```
1
2
3
4
5
```

### Usando `for` com `range()`
O `for` também é frequentemente usado em conjunto com a função `range()`.

> O comando `range()` cria uma sequência de números inteiros. Ele é usado em loops, permitindo definir o início, o fim e o passo da contagem. É eficiente, pois gera os números conforme necessário.

> `range(start, stop, step)`:
> - `start`: *Opcional*; número inteiro que indica onde começar (padrão é 0).
> - `stop`: **Obrigatório**; número inteiro que indica onde parar (não incluído).
> - `step`: *Opcional*; número inteiro que define o incremento (padrão é 1).


```python
for i in range(6):  # De 0 a 5
    print(i)
```

**Saída:**
```
0
1
2
3
4
5
```

### Considerações
- O `for` é ideal para iterar sobre coleções ou realizar operações em sequência, garantindo que cada elemento seja processado de forma controlada e eficiente.
- É preferido em situações onde o número de iterações é conhecido ou pode ser facilmente determinado, proporcionando uma maneira clara e direta de percorrer elementos.

Utilizar a estrutura de repetição `for` pode simplificar a lógica do seu código e melhorar a legibilidade, especialmente em operações que envolvem iteração sobre dados.
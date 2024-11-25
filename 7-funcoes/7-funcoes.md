# 7 - Funções
[🔙 Voltar](../README.md)
## O que é?

Uma função é um trecho de código projetado para resolver um problema específico, muitas vezes como parte de uma solução maior. Utilizar funções traz várias vantagens:

- **Redução de código duplicado**: Elimina a repetição de trechos de código.
- **Reutilização de código**: Permite usar o mesmo código em diferentes partes de um programa ou em outros programas.
- **Divisão de problemas complexos**: Facilita a decomposição de problemas em partes menores e gerenciáveis.
- **Melhora da legibilidade**: Torna o código mais compreensível, facilitando a colaboração.
- **Encapsulamento de lógica**: Isola a lógica da função, separando-a da implementação do restante do programa.

## Criação e Utilização de Funções

Uma função é composta por:

- **Protótipo**: Define o nome da função e seus parâmetros. Em Python, isso ocorre na linha que começa com `def`.
- **Corpo**: Conjunto de instruções que realizam a tarefa da função.
- **Valores de retorno**: Resultados produzidos pela função, que podem ser usados posteriormente.

**Estrutura básica de uma função em Python:**

```python
def nome_da_funcao(parametros):
    # bloco de código
    return valor_de_retorno
```

O código dentro do corpo da função deve ser corretamente indentado para indicar sua inclusão.

Após criar uma função, ela pode ser chamada no programa principal assim:

```python
resultado = funcao(parametros)
```

Os parâmetros são opcionais; uma função pode ser chamada sem eles, e o retorno também pode ser omitido.

## Exemplo: Função `cubo`

A função `cubo` recebe um valor `x`, calcula seu cubo e o retorna:

```python
def cubo(x):
    return x ** 3

print(cubo(2))  # Saída: 8
```

**Explicação:**

- A função `cubo(x)` recebe `2` como parâmetro, calcula \(2^3\) e retorna `8`, que é exibido pelo comando `print`.

## Reutilização de Código

```python
def cubo(x):
    return x ** 3

x = 2
y = cubo(x)
print(y)  # Saída: 8

x = 4
y = cubo(x)
print(y)  # Saída: 64
```

**Resultado esperado:**

- A função `cubo` pode ser reutilizada para calcular o cubo de diferentes valores.

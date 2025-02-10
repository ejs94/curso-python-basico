# 10 - Compreensões de Listas
[🔙 Voltar](../README.md)

## O que são Compreensões de Listas?

As compreensões de listas são uma maneira concisa e eficiente de criar listas em Python. Elas permitem gerar novas listas aplicando uma expressão a cada item de uma sequência ou iterável, utilizando uma sintaxe mais legível em comparação com loops tradicionais.

### Sintaxe:
```python
nova_lista = [expressão for item in iterável if condição]
```

### Exemplo:

```python
# Solicita ao usuário que insira valores separados por espaço
entrada = input("Digite os números inteiros, separados por espaço: ")
# Cria uma lista de inteiros a partir da entrada
lista_inteiros = [int(num) for num in entrada.split()]
# Exibe a lista de inteiros
print("Lista de inteiros:", lista_inteiros)
```

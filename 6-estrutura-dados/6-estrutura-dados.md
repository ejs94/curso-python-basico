# 6 - Estrutura de Dados
[🔙 Voltar](../README.md)
## O que é?

Estruturas de dados são formas de organizar e manipular dados de maneira eficiente, permitindo operações como inserção, exclusão, busca e atualização.

Exemplos comuns de estruturas de dados incluem **listas**, **tuplas** e **dicionários** em Python, cada uma com suas características e usos específicos.

---

## Estrutura de Dados: `list`

Listas são estruturas que agrupam elementos em sequência. Podem ser criadas com colchetes, e os elementos, separados por vírgula, não precisam ser do mesmo tipo.

```python
minha_lista = ["nome", 10, 0.005]
print(minha_lista)
```

Os elementos são acessados pela posição (índice). Por exemplo, para acessar o primeiro e o quinto elemento:

```python
minha_lista = ["cadeira", "tesoura", "martelo", "alicate", "caixa"]
print(minha_lista[0])  # Primeiro elemento
print(minha_lista[4])  # Quinto elemento
```

É possível selecionar partes da lista indicando índices inicial e final:

```python
minha_lista = ["uma", "cadeira", 3, "cm", 0.25, "desconto"]
print(minha_lista[1:4])  # Seleciona do índice 1 ao 3
```

A nova lista inclui o elemento inicial e exclui o final. Além disso, listas podem ser unidas com o símbolo `+`:

```python
lista_1 = ["qual a quantidade do pedido?"]
lista_2 = ["pode", "ser", "4", "pregos"]
print(lista_1 + lista_2)
```

### Adicionando Elementos com `append()`

O método `append()` permite adicionar um novo elemento ao final da lista. Isso é útil para expandir uma lista dinamicamente.

```python
minha_lista = ["maçã", "banana"]
minha_lista.append("laranja")
print(minha_lista)  # Saída: ['maçã', 'banana', 'laranja']
```

Com `append()`, você pode facilmente adicionar elementos sem precisar criar uma nova lista.

---

## Estrutura de Dados: `tuple`

Tuplas são estruturas de dados que permitem agrupar elementos em uma sequência, semelhante às listas. Em Python, uma tupla é criada utilizando parênteses para delimitar os elementos, que devem ser separados por vírgula. 

Assim como nas listas, os elementos de uma tupla podem ser de tipos variados; no entanto, ao contrário das listas, os elementos de uma tupla são imutáveis, ou seja, não podem ser alterados após a criação. Isso significa que, uma vez criada, você não pode adicionar, remover ou alterar elementos de uma tupla.

```python
minha_tupla = (1, 1, 3, 5, 8, 13)
print(minha_tupla)
```

Os elementos de uma tupla podem ser acessados por meio de seus índices, assim como um intervalo de elementos. Além disso, é possível criar uma nova tupla a partir da combinação de duas tuplas existentes.

```python
tupla_1 = (1, 1, 3, 5, 8, 13)
tupla_2 = (21, 24)

print(tupla_1[0])      # Acesso ao primeiro elemento da tupla
print(tupla_1[0:4])    # Selecionando os primeiros quatro elementos
print(tupla_1 + tupla_2)  # Combinando tuplas
```

Além disso, as tuplas são geralmente mais rápidas que as listas, pois possuem uma estrutura de dados mais simples. Elas são frequentemente utilizadas para armazenar dados que não precisam ser alterados, como coordenadas geográficas ou valores constantes.

### Exemplo de Código: Tuplas vs. Listas

Abaixo está um exemplo que ilustra a diferença entre listas e tuplas em Python:

```python
# Criando uma lista
minha_lista = [1, 2, 3, 4]
print("Lista antes da modificação:", minha_lista)

# Modificando a lista
minha_lista.append(5)  # Adicionando um elemento
print("Lista após a modificação:", minha_lista)

# Criando uma tupla
minha_tupla = (1, 2, 3, 4)
print("Tupla:", minha_tupla)

# Tentando modificar a tupla (isso gerará um erro)
try:
    minha_tupla[0] = 10  # Tentativa de alteração
except TypeError as e:
    print("Erro ao modificar a tupla:", e)

# Acessando elementos
print("Primeiro elemento da tupla:", minha_tupla[0])
print("Primeiro elemento da lista:", minha_lista[0])
```

### Saída Esperada:

```
Lista antes da modificação: [1, 2, 3, 4]
Lista após a modificação: [1, 2, 3, 4, 5]
Tupla: (1, 2, 3, 4)
Erro ao modificar a tupla: 'tuple' object does not support item assignment
Primeiro elemento da tupla: 1
Primeiro elemento da lista: 1
```

### Resumo:

- **Tuplas**: Estruturas imutáveis, criadas com parênteses, que não podem ser alteradas após a criação.
- **Listas**: Estruturas mutáveis, criadas com colchetes, que permitem modificações como adições e remoções de elementos. 

Essas características fazem com que tuplas sejam ideais para armazenar dados constantes, enquanto listas são mais apropriadas para conjuntos de dados que precisam ser alterados.

---

## Estrutura de Dados: `dict`

Em Python, os dicionários são uma estrutura de dados que permite armazenar um conjunto de elementos de forma organizada. Eles são criados utilizando chaves `{}` para delimitar o conjunto de pares “chave”: “valor”. A sintaxe básica para a criação de um dicionário é a seguinte:

```python
dicionario = {
    "chave_1": valor_1,
    "chave_2": valor_2,
    "chave_3": valor_3,
}
```

Os elementos de um dicionário são compostos por pares, onde cada chave é única e serve como um identificador para o valor associado. Isso permite que você acesse os elementos do dicionário através de suas chaves, em vez de usar índices como nas listas.

```python
meu_dicionario = {
    "nome": "Furadeira_3000",
    "num_operacoes": 30,
    "bateria": 88.5,
}

print(meu_dicionario["nome"])  # Exibe o valor associado à chave "nome"

meu_dicionario["em_uso"] = True  # Adiciona uma nova chave "em_uso"

print(meu_dicionario)  # Exibe todo o conteúdo do dicionário
```

---

Os dicionários são particularmente úteis para armazenar dados que precisam ser acessados rapidamente por uma chave, tornando-os uma escolha ideal para várias aplicações em programação.

Resumo Comparativo: **Listas**, **Tuplas** e **Dicionários**

**Listas**: 

- Estruturas mutáveis que permitem armazenar uma coleção de elementos em uma sequência.
- Criadas com colchetes [].
- Permitem alterações, como adições e remoções de elementos.

**Tuplas**:

- Estruturas imutáveis que agrupam elementos em uma sequência.
- Criadas com parênteses ().
- Os elementos não podem ser alterados após a criação, tornando-as mais rápidas e seguras para dados constantes.

**Dicionários**:

- Estruturas que armazenam pares “chave”: “valor” de forma organizada.
- Criados com chaves {}.
- Permitem acesso rápido aos valores através de suas chaves, em vez de índices.

Essas três estruturas de dados têm suas características e usos específicos, permitindo que os desenvolvedores escolham a mais adequada para cada situação.
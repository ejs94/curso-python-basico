# Capitulo 2 - Variáveis

## O que são variáveis

As variáveis são recursos fundamentais na programação, permitindo que um programa armazene e acesse informações na memória do computador por meio de nomes definidos. Em Python, as variáveis podem manipular diferentes tipos de dados, como strings (cadeias de caracteres), números inteiros e números reais. Para criar uma variável, basta atribuir um valor a um nome utilizando o símbolo "=". 

```python
nome_maquina = "Fresadora 3000"
peca_produzidas = 150
eficiencia_maquina = 75.7
```

> O comando `print` é utilizado para exibir informações armazenadas na memória, permitindo que esses dados sejam acessados e visualizados a qualquer momento.

---

## Tipos de variáveis

Criar uma variável em Python é como reservar uma prateleira em um almoxarifado, onde o tipo de variável define o espaço e a organização. Um "tipo" refere-se à categoria de dados que uma variável pode armazenar, como números, texto ou listas, e determina como esses dados podem ser utilizados e manipulados. 

Aqui estão os principais tipos de variáveis em Python:

- **`int` (inteiros)**: é como uma prateleira que guarda números inteiros como 2, 453 ou -12 (sem partes decimais).
- **`float` (pontos flutuantes)**: aqui você armazena números com vírgula (ou pontos decimais), como 2.34 ou -12.9. Pense nisso como medir algo com mais precisão.
- **`complex` (números complexos)**: para guardar números mais complexos, como aqueles usados em eletrônica ou física, que têm uma parte real e uma parte imaginária (a + jb).
- **`str` (cadeia de caracteres)**: é onde você guarda textos, como nomes, palavras ou frases. Tudo o que for uma sequência de letras ou símbolos.
- **`bool` (booleano)**: armazena respostas simples, como sim ou não (ou seja, `True` ou `False`).

> O comando `type` funciona como uma ferramenta de inspeção dizendo se a "prateleira" que você criou na memória está armazenando um número, um texto, ou outro tipo de dado.

---

## Lendo valores de entrada

As variáveis em Python podem ser definidas no código ou recebidas através do comando `input`.

> O `input` exibe uma caixa de texto para o usuário inserir dados, que são armazenados como `str` na variável correspondente.

```python
numero = input("Digite um número: ")
```

É possível alterar o tipo da variável recebida através do comando `input`, para isso, utiliza-se as funções que levam o nome do tipo de variável desejado.

```python
numero_inteiro = int(input("Digite um número inteiro (int): "))
numero_quebrado = float(input("Digite um número quebrado (float): "))
```


# 9 - Módulos
[🔙 Voltar](../README.md)

### O que é um Módulo?

Um módulo em Python é um arquivo que contém definições e implementações de funções, classes e variáveis que podem ser reutilizadas em outros programas. Criar módulos permite organizar o código de forma mais eficiente e promover a reutilização.

### Criando um Módulo

Para criar um módulo, basta criar um arquivo Python (.py) com as funções e classes desejadas. Por exemplo, vamos criar um módulo chamado `operacoes.py` que contém algumas funções para operações de texto:

```python
# operacoes.py

def maiusculas(texto):
    """Retorna o texto em letras maiúsculas."""
    return texto.upper()

def minusculas(texto):
    """Retorna o texto em letras minúsculas."""
    return texto.lower()

def contar_caracteres(texto):
    """Retorna a contagem de caracteres no texto."""
    return len(texto)
```

### Importando o Módulo na Main

Uma vez que o módulo `operacoes.py` foi criado, ele pode ser importado em um arquivo principal (main) para utilização. Vamos criar um arquivo chamado `main.py` que importa o módulo e utiliza suas funções:

```python
# main.py

import operacoes

def main():
    texto = "Python é incrível!"

    print(f"Texto original: {texto}")
    print(f"Em maiúsculas: {operacoes.maiusculas(texto)}")
    print(f"Em minúsculas: {operacoes.minusculas(texto)}")
    print(f"Contagem de caracteres: {operacoes.contar_caracteres(texto)}")

if __name__ == "__main__":
    main()
```

### Resultado Esperado

Ao executar o arquivo `main.py`, a saída será:

```
Texto original: Python é incrível!
Em maiúsculas: PYTHON É INCRÍVEL!
Em minúsculas: python é incrível!
Contagem de caracteres: 21
```

Essa abordagem demonstra como criar um módulo em Python e importá-lo em um arquivo principal, facilitando a organização do código e a reutilização de funcionalidades em diferentes partes do projeto. Módulos são uma maneira eficaz de estruturar programas maiores e mais complexos, promovendo clareza e manutenção do código.

### Módulo vs Bibliotecas

- **Módulo:** Um único arquivo Python que contém código reutilizável.
- **Biblioteca:** Um conjunto de módulos que oferece uma coleção de funcionalidades relacionadas.

## Utilização de Bibliotecas em Python

Python oferece uma vasta gama de bibliotecas que podem ser facilmente integradas aos projetos, proporcionando funcionalidades como cálculos matemáticos, manipulação de dados e muito mais.

### Exemplos de Bibliotecas

- **math:** Esta biblioteca fornece funções matemáticas básicas, como `sqrt` (raiz quadrada), `sin` (seno) e `cos` (cosseno). É útil para realizar operações matemáticas comuns de forma rápida e eficiente.

```python
import math

# Exemplos de uso da biblioteca math
raiz_quadrada = math.sqrt(16)  # Calcula a raiz quadrada de 16
seno = math.sin(math.radians(30))  # Calcula o seno de 30 graus

print(f"Raiz quadrada de 16: {raiz_quadrada}")
print(f"Seno de 30 graus: {seno}")
```

- **numpy:** Uma biblioteca poderosa para manipulação de arrays e operações matemáticas avançadas. É amplamente utilizada em ciência de dados e aplicações que exigem cálculos numéricos intensivos.

```python
import numpy as np

# Criando um array e realizando operações
array = np.array([1, 2, 3, 4])
soma = np.sum(array)  # Soma todos os elementos do array

print(f"Array: {array}")
print(f"Soma dos elementos: {soma}")
```

A utilização das bibliotecas demonstra como as funções predefinidas podem simplificar operações complexas. Por exemplo, o uso da biblioteca `math` permite realizar cálculos matemáticos com facilidade, enquanto `numpy` facilita a manipulação de dados em larga escala.

---

### Observação sobre `if __name__ == "__main__":`

A linha `if __name__ == "__main__":` é uma construção comum em Python que permite que um arquivo seja executado como um script ou importado como um módulo sem executar o código que se encontra dentro deste bloco. 

- **Significado:** Quando um arquivo Python é executado, a variável especial `__name__` é atribuída com o valor `"__main__"` se o arquivo estiver sendo executado diretamente. Se o arquivo for importado como um módulo em outro arquivo, a variável `__name__` recebe o nome do módulo.

- **Utilidade:** Isso permite que você defina uma função principal (como `main()`) que será chamada apenas quando o script for executado diretamente, evitando a execução de código indesejado durante a importação. Isso é especialmente útil para testes e para organizar a estrutura do código, tornando-o mais modular e reutilizável.

### Exemplo

Considere o seguinte código:

```python
def main():
    print("Executando a função principal.")

if __name__ == "__main__":
    main()
```

- Se você executar este arquivo diretamente, ele imprimirá "Executando a função principal."
- Se você importar este arquivo em outro script, a função `main()` não será chamada automaticamente, permitindo que você use as funções e classes definidas sem acionar o código de execução.

Essa prática é considerada uma boa prática em Python, contribuindo para a clareza e a manutenção do código.
# 9 - Bibliotecas
[🔙 Voltar](../README.md)
### O que são Bibliotecas?

Bibliotecas são coleções de funções e métodos que realizam tarefas específicas, facilitando o desenvolvimento de software. Elas permitem que os programadores reutilizem código, economizando tempo e esforço na criação de funcionalidades comuns.

### Utilização de Bibliotecas em Python

Python oferece uma vasta gama de bibliotecas que podem ser facilmente integradas aos projetos, proporcionando funcionalidades como cálculos matemáticos, manipulação de dados e muito mais.

**Exemplos de Bibliotecas:**

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

### Resultado esperado:

- A utilização das bibliotecas demonstra como as funções predefinidas podem simplificar operações complexas. Por exemplo, o uso da biblioteca `math` permite realizar cálculos matemáticos com facilidade, enquanto `numpy` facilita a manipulação de dados em larga escala.

Esses exemplos ilustram a importância e a praticidade das bibliotecas em Python, proporcionando aos desenvolvedores ferramentas para acelerar o desenvolvimento e melhorar a eficiência dos projetos.
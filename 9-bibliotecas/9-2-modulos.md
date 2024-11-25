# 9.2 - Módulo

### O que é um Módulo?

Um módulo em Python é um arquivo que contém definições e implementações de funções, classes e variáveis que podem ser reutilizadas em outros programas. Criar módulos permite organizar o código de forma mais eficiente e promover a reutilização.

### Módulo vs Bibliotecas

- **Módulo:** Um único arquivo Python que contém código reutilizável.
- **Biblioteca:** Um conjunto de módulos que oferece uma coleção de funcionalidades relacionadas.

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

Agora que criamos o módulo `operacoes.py`, podemos importá-lo em um arquivo principal (main) para utilizá-lo. Vamos criar um arquivo chamado `main.py` que importa o módulo e utiliza suas funções:

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

### Resultado Esperado:

Ao executar o arquivo `main.py`, a saída será:

```
Texto original: Python é incrível!
Em maiúsculas: PYTHON É INCRÍVEL!
Em minúsculas: python é incrível!
Contagem de caracteres: 21
```

### Conclusão

Essa abordagem demonstra como criar um módulo em Python e importá-lo em um arquivo principal. Isso facilita a organização do código e a reutilização de funcionalidades em diferentes partes do seu projeto. Módulos são uma maneira eficaz de estruturar programas maiores e mais complexos, promovendo a clareza e a manutenção do código.
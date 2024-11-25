# 8 - Classes e Objetos

### O que é?

Uma classe define características e comportamentos, enquanto um objeto é uma instância concreta dessa classe, com atributos e comportamentos específicos.

### Criação e utilização de Classes e Objetos

Nesta seção, veremos como Python, como uma linguagem orientada a objetos, permite a criação e uso de classes e objetos para organizar o código.

**Exemplo: Classe Pokémon**

Vamos ilustrar isso com uma classe `Pokemon`, que simula uma batalha entre dois Pokémon.

```python
class Pokemon:
    def __init__(self, nome: str, vida: int):
        self.nome = nome
        self.vida = vida

    def atacar(self, outro: Pokemon):
        dano = 10
        outro.vida -= dano
        print(f"{self.nome} ataca {outro.nome} e causa {dano} de dano!")

# Criando objetos da classe Pokemon
pikachu = Pokemon("Pikachu", 100)
charizard = Pokemon("Charizard", 120)

# Simulando uma batalha
pikachu.atacar(charizard)
charizard.atacar(pikachu)

print(f"{charizard.nome} tem {charizard.vida} de vida restante.")
print(f"{pikachu.nome} tem {pikachu.vida} de vida restante.")
```

**Resultado esperado:**

- O programa simula ataques entre Pikachu e Charizard, mostrando a quantidade de dano causado e a vida restante de cada Pokémon.

Essa abordagem ilustra como as classes e objetos podem ser usados para modelar comportamentos e interações em um programa.

---

# 8 - Classes e Objetos: Herança


## O que é Herança?

A herança é um princípio da programação orientada a objetos que permite que uma nova classe (classe filha) derive de uma classe existente (classe pai), herdando suas propriedades e métodos. Isso promove a reutilização de código e facilita a extensão de funcionalidades.

### Exemplo de Herança

Vamos criar subclasses `Pikachu` e `Charizard` que herdam da classe `Pokemon` e têm suas próprias implementações do método `atacar`.

```python
class Pikachu(Pokemon):
    def atacar(self, outro: Pokemon):
        dano = 15  # Pikachu causa mais dano
        outro.vida -= dano
        print(f"{self.nome} usa Choque do Trovão em {outro.nome} e causa {dano} de dano!")

class Charizard(Pokemon):
    def atacar(self, outro: Pokemon):
        dano = 20  # Charizard causa ainda mais dano
        outro.vida -= dano
        print(f"{self.nome} usa Lança-Chamas em {outro.nome} e causa {dano} de dano!")
```

---
# 8 - Classes e Objetos: Polimorfismo

## O que é Polimorfismo?

Polimorfismo permite que métodos com o mesmo nome se comportem de maneira diferente em classes diferentes. Isso é alcançado através da sobreposição de métodos, onde subclasses podem fornecer implementações específicas para um método herdado.

### Exemplo de Polimorfismo

Agora vamos simular uma batalha entre um `Pikachu` e um `Charizard`, demonstrando o polimorfismo:

```python
# Criando objetos das subclasses
pikachu = Pikachu("Pikachu", 100)
charizard = Charizard("Charizard", 120)

# Simulando uma batalha
pikachu.atacar(charizard)
charizard.atacar(pikachu)

print(f"{charizard.nome} tem {charizard.vida} de vida restante.")
print(f"{pikachu.nome} tem {pikachu.vida} de vida restante.")
```

### Resultado esperado:

- O programa simula ataques entre Pikachu e Charizard, mostrando como cada um utiliza seu próprio método `atacar`, com diferentes danos.

Esse exemplo ilustra como a herança e o polimorfismo podem ser usados para criar um sistema mais flexível e organizado em programação orientada a objetos.
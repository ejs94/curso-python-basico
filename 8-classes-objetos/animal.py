class Animal:
    def __init__(self, nome):
        self.nome = nome
class Cachorro(Animal):
    def latir(self):
        return "Au au!"
class Gato(Animal):
    def miar(self):
        return "Miau!"


# Criando instâncias
bicho1 = Cachorro("Rex")
bicho2 = Gato("Mia")

# Verificando tipos
if isinstance(bicho1, Animal):
    print(f"{bicho1.nome} é um Animal.")
if isinstance(bicho2, Gato):
    print(f"{bicho2.nome} é um Gato.")
if isinstance(bicho1, Cachorro):
    print(f"{bicho1.nome} é um Cachorro.")


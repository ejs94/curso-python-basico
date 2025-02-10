# veiculos.py

class Veiculo:
    def tipo(self):
        return "Veículo genérico"

class Carro(Veiculo):
    def tipo(self):
        return "Carro"

class Bicicleta(Veiculo):
    def tipo(self):
        return "Bicicleta"

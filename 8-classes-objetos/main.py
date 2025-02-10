from veiculos import Carro, Bicicleta, Veiculo

def filtrar_palavras():
    # Solicita ao usuário que insira palavras separadas por espaço
    entrada = input("Digite as palavras separadas por espaço: ")
    # Cria uma lista com palavras que têm mais de 3 letras
    lista_palavras = [palavra for palavra in entrada.split() if len(palavra) > 3]
    # Exibe a lista resultante
    print("Lista de palavras com mais de 3 letras:", lista_palavras)

def verificar_tipos():
    # Cria instâncias de Carro e Bicicleta
    carro = Carro()
    bicicleta = Bicicleta()

    # Verifica se cada instância é um Veiculo
    for veiculo in [carro, bicicleta]:
        if isinstance(veiculo, Veiculo):
            print(f"O {veiculo.tipo()} é um Veículo.")

if __name__ == "__main__":
    filtrar_palavras()
    verificar_tipos()
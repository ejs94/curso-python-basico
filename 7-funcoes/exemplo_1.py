def calcular_soma(lista_numeros):
    """
    Calcula a soma dos números em uma lista.

    Args:
        lista_numeros (list): Uma lista de números.

    Returns:
        float: A soma dos números na lista.
    """
    soma = 0  # Inicializa a variável soma
    for numero in lista_numeros:
        soma += numero  # Adiciona cada número à soma
    return soma  # Retorna o resultado

# Exemplo de uso da função
numeros = [1, 2, 3, 4, 5]
resultado = calcular_soma(numeros)

print(f"A soma dos números {numeros} é: {resultado}")

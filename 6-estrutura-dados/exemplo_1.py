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
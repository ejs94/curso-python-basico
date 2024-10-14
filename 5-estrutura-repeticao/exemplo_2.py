# Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Usando um loop for para imprimir cada fruta
for fruta in frutas:
    print("Fruta:", fruta)

# Usando for com range() para imprimir os índices
print("\nFrutas com seus índices:")
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}")

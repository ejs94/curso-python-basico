# O código verifica se uma peça de manufatura atende aos padrões de qualidade com base em suas dimensões. 
# 1. Inicialmente, as medidas de comprimento são armazenadas. 
# 2. O comando `if` verifica se o comprimento está dentro dos limites especificados.
# 3. Se todas as condições forem verdadeiras, o programa indica que a peça está em conformidade. 
# 4. Caso contrário, informa que a peça deve ser reprocessada.

COMPRIMENTO_OTIMO = 50.0

comprimento = float(input("Digite o comprimento da peça: "))

if (comprimento <= COMPRIMENTO_OTIMO):
    print("✅ A peça atende a qualidade.")
else:    
    print("❌ A peça não atende a qualidade.")
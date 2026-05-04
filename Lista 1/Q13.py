#13 - Ler 3 valores e calcular a média ponderada. Pesos: 5, 3 e 2. Fórmula = (n1*5 + n2*3 + n3*2) / (5+3+2).#
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
media_ponderada = (n1*5 + n2*3 + n3*2) / (5+3+2)
print("A média ponderada é:", media_ponderada)
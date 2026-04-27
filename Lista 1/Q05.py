#5 - Escreva um programa para determinar o consumo médio de um automóvel sendo fornecido a distância total percorrida e o total de combustível gasto. #
distancia = float(input("Digite a distância total percorrida (em km): "))
combustivel = float(input("Digite o total de combustível gasto (em litros): "))
consumo_medio = distancia / combustivel
print("O consumo médio do automóvel é de", consumo_medio, "km/l")
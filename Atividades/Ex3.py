#Escreva um algoritmo que calcule e mostre o valor do somatório:
#S = 1/1 + 3/2 + 5/3 + 7/4 + .... + 99/50
#O resultado do somatório deve ser formatado para apresentar 2 casas decimais.

s = 0.0
for i in range(1, 100, 2):
    s += i / ((i + 1) // 2)
print(f"{s:.2f}")

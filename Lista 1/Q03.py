#Escreva um algoritmo para calcular o IMC de uma pessoa. Fórmula IMC = peso / altura2#

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)

print("O IMC é: ", imc)
#Faça um algoritmo que leia o saldo de um cliente e calcule o valor do crédito de acordo com a tabela abaixo. Mostre uma mensagem informando o saldo e o valor do crédito que o banco concederá ao cliente.
saldo = float(input())
if saldo <= 200:
    credito = 0
elif saldo <= 600:
    credito = saldo * 0.2
elif saldo <= 1000:
    credito = saldo * 0.3
else:
    credito = saldo * 0.4
print(f"Crédito: R$ {credito:.2f}")
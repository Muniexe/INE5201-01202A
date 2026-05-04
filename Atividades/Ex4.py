#Sequência de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores.
# um programa para gerar os 10 primeiros termos desta sequência.
#Saída do programa:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34

a, b = 0, 1
for _ in range(10):
    print(a, end=", " if _ < 9 else "\n")
    a, b = b, a + b
    
#Realizou-se uma pesquisa e os seguintes dados foram solicitados para os entrevistados: idade, sexo, quantidade de livros que leu no ano de 2023. Escreva um programa que leia os dados informados pelo usuário. Os dados devem ser solicitados até que a idade digitada seja um valor negativo. Calcular e imprimir as seguintes informações: 
#a) Total de livros lidos pelos entrevistados menores de 12 anos;
#b) Quantidade de mulheres que leram 5 livros ou mais;
#c) Total de pessoas que leram 0 livros;
#d) Média de idade dos homens que leram menos de 5 livros.

total_livros_menores_12 = 0
quantidade_mulheres_5_ou_mais = 0
total_pessoas_0_livros = 0
soma_idade_homens_menos_5_livros = 0
quantidade_homens_menos_5_livros = 0

while True:
    idade = int(input())
    if idade < 0:
        break

    sexo = input().strip().upper()
    livros_lidos = int(input())

    if idade < 12:
        total_livros_menores_12 += livros_lidos

    if sexo == 'F' and livros_lidos >= 5:
        quantidade_mulheres_5_ou_mais += 1

    if livros_lidos == 0:
        total_pessoas_0_livros += 1

    if sexo == 'M' and livros_lidos < 5:
        soma_idade_homens_menos_5_livros += idade
        quantidade_homens_menos_5_livros += 1

# cálculo da média (SEM mensagem extra)
if quantidade_homens_menos_5_livros > 0:
    media = soma_idade_homens_menos_5_livros / quantidade_homens_menos_5_livros
else:
    media = 0.0

# saídas no formato esperado
print(f"Total de livros lidos por menores de 12 anos: {total_livros_menores_12}")
print(f"Quantidade de mulheres que leram 5 ou mais livros: {quantidade_mulheres_5_ou_mais}")
print(f"Total de pessoas que leram 0 livros: {total_pessoas_0_livros}")
print(f"Média de idade dos homens que leram menos de 5 livros: {media:.2f}")
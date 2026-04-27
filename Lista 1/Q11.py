#11 - Faça um programa que leia o salário fixo e o total de vendas efetuadas por um  vendedor  no  mês.  Sabendo  que  este  vendedor  ganha  15%  de  comissão sobre suas vendas efetuadas, informar o seu salário fixo e salário total no final do mês.#
salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
total_vendas = float(input("Digite o total de vendas efetuadas no mês: R$ "))
comissao = 0.15 * total_vendas
salario_total = salario_fixo + comissao
print(f"Salário Fixo: R$ {salario_fixo:.2f}")
print(f"Salário Total no final do mês: R$ {salario_total:.2f}")

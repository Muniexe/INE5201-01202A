#9 - Elaborar um algoritmo que efetue a conversão de uma determina quantia de Dólares (US$) informada pelo usuário para o respectivo valor em Reais (R$). O algoritmo deverá solicitar o valor da cotação do Dólar.#
import requests
import json

# URL da API para o par Dólar Comercial (USD) para Real (BRL)
url = "https://economia.awesomeapi.com.br/last/USD-BRL"

# Realiza a requisição GET
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Extrai a cotação de compra
    dolar_compra = data['USDBRL']['bid']
    print(f"Cotação do Dólar (Compra): R$ {dolar_compra}")
else:
    print("Erro ao obter a cotação")


dolar = float(input("Digite a quantia em Dólares (US$): "))
reais = dolar * float(response.json()['USDBRL']['bid'])
print(f"O valor em Reais (R$) é: {reais:.2f}")
2
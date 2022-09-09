import requests
res = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
print(res)
res_json = res.json()

cotacao_dolar = float(res_json["USDBRL"]["bid"])
cotacao_euro = float(res_json["EURBRL"]["bid"])

print(f"1EUR = {cotacao_euro}R$")
print(f"1USD = {cotacao_dolar}R$")
# FAÇA UM PROGRAMA QUE: recebe do usuário uma quantidade X de reais
# e informe quanto isso vale em DOLAR (além de informar as cotações)

usuario_reais = float(input("Digite quantos reais você deseja converter: "))

usuario_dolar = usuario_reais/cotacao_dolar
usuario_euro = usuario_reais/cotacao_euro


print(f"{usuario_reais}R$ = {usuario_dolar:.4f} EUR") 
print(f"{usuario_reais}R$ = {usuario_euro:.4f} USD")





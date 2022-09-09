from datetime import date

#data_atual = date.today()
#ano_atual = data_atual.year
#mes_atual = data_atual.month
#dia_atual = data_atual.day

ano = int(input("Digite o ano atual: "))
mes = int(input("Digite o mes atual: "))
dia = int(input("Digite o dia atual: "))

data_atual = date(ano, mes, dia)

# Quando começam as aulas 22/08/2022 (2022.4)

fim_ferias_20222 = date(2022, 8, 22)

tempo_faltante = fim_ferias_20222 - data_atual
#print(tempo_faltante.days)

# Caso de teste
#volta_as_aulas = date(2022, 8, 22)
#tempo_faltante = fim_ferias_20222 - volta_as_aulas
if tempo_faltante.days > 0:
    print(f"Ainda faltam {tempo_faltante.days} dias para as Férias")
elif tempo_faltante.days == 0:
    print(f"Começa hoje as aulas!!!")
else:
    print("Já acabou as férias... ")
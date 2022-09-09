from datetime import date
# Quando começam as aulas: 22/08/2022 2022.4
data_atual = date.today()
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day
#caso teste
data_atual = date(2022, 8, 30)
termino_ferias = date(2022, 8, 22)

tempo_faltante = termino_ferias - data_atual
tempo_faltante = tempo_faltante.days

if tempo_faltante > 0:
    print(f"Faltam {tempo_faltante} dias para as férias acabarem")
elif tempo_faltante == 0:
    print("Hoje é o dia do volta as aulas!!! Acabaram as férias :(")
else:
    print("As férias já acabaram !!! :( ")



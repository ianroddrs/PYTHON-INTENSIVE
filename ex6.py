print("Difite C para converter de Fahrenheit para Celcius.")
print("Difite F para converter de Celcius para Fahrenheit.")

operacao = input("Sua escolha:")

if operacao == "C":
    tempF = input("temperatura Fahrenheit:")
    if tempF.isnumeric():
        tempC = (float(tempF) - 32) * 5 / 9
        print(f"A temperatura em C é {tempC:.2f} ")
    else:
        print("Digite apenas numeros!!")
if operacao == "F":
    tempC = input("temperatura Celcius:")
    if tempC.isnumeric():
        tempF = (float(tempC) * 9 / 5) + 32
        print(f"A temperatura em F é {tempF:.2f} ")
    else:
        print("Digite apenas numeros!!")
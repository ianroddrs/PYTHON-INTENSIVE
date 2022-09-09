from random import *
from math import ceil

novaTentativa = True
tentativas = 0
numeroSorteado = ceil(random() * 10)

while novaTentativa:
    tentativas += 1
    tentativa = int(input("Palpite: "))

    if tentativa > numeroSorteado:
        print("Um pouco mais baixo")
        continue
    elif tentativa < numeroSorteado:
        print("Um pouco mais alto")
        continue
    elif tentativa == numeroSorteado:
        print("Acertaste")
        novaTentativa = False

print(f"Número de tentativas: {tentativas}")

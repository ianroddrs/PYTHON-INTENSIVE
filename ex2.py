numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1
dobro = numero * 2
triplo = numero * 3
quadrado = numero ** 2

print(f'O antecessor de {numero} é: {antecessor}')
print(f'O sucessor de {numero} é: {sucessor}')
print(f'O dobro de {numero} é: {dobro}')
print(f'O triplo de {numero} é: {triplo}')
print(f'O quadrado de {numero} é: {quadrado}')

if numero < 10 and numero > 4:
    print("Esse numero está entre 4 e 10")

if numero > 5 or numero != 10:
    print("esse numero não é igual a 10, mas é maior que 5")
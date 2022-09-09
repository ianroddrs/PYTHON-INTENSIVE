idade = int(input("Digite sua idade: "))
CNH = int(input("(1-Sim| 2-Não)\nVocê possui CNH?"))

if idade >= 18 and CNH == 1:
    print("Você pode participar dos cursos de: Direção Defensiva e Defesa Pessoal")
elif idade >= 18 and CNH == 2:
    print("Você só poderá se inscrever no curso de Defesa Pessoal")
else:
    print("É necessário ser maior de idade para fazer os cursos.")
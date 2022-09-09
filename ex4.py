usuario = input("Nome de Usuário: ")
senha = input("Senha do Usuário: ")

usuario_bd = "Ian Rodrigues"
senha_bd = "qwert22"

if usuario == usuario_bd and senha == senha_bd:
    print("Bem-Vindo(a)!")
else:
    print("Usuário ou senha incorretos.")
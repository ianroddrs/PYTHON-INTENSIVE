from tkinter import *

def funcaoClicaBotao():
    print("hello world!")


janela = Tk()
janela.geometry("720x300")
janela.title("TESTE DE JANELA")
#janela.configure(background="red")


texto1 = Label(
    janela,
    text="OLÁ MUNDO!",
    font=(
        "Helvetica", 18, "bold"
    )
)
texto1.place(
    x=40,
    y=0,
    width=300,
    height=30,
)

entrada = Entry(
    janela,
    font=(
        "Helvetica", 18, "bold"
    )
)
entrada.place(
    x=40,
    y=100,
    width=300,
    height=30,
)

botao = Button(
    janela,
    text="clique em mim",
    font=(
        "Helvetica", 18, "bold"
    ),
    anchor=E,
    command=funcaoClicaBotao
)
botao.place(
    x=40,
    y=150,
    width=300,
    height=30,
)












janela.mainloop()
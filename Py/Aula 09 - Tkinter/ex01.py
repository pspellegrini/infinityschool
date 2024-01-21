from tkinter import *

window = Tk()

title = Label(
    text = 'Bem-vindo ao Sistema de Cadastro de Aluno',
    fg ='#FFFAFA',
    bg='#1C1C1C',
    width = 150
)

nome = Label(text = 'Nome:', fg='#FFFAFA', bg='#1C1C1C')
entrada_aluno = Entry()

idade = Label(text = 'Idade:', fg='#FFFAFA', bg='#1C1C1C')
entrada_idade = Entry()

nota = Label(text = 'Nota:', fg='#FFFAFA', bg='#1C1C1C')
entrada_nota = Entry()


def limpar():
    entrada_aluno.delete(0, END)
    entrada_idade.delete(0, END)
    entrada_nota.delete(0, END)

def imprimir_aluno():
    print(f'''
          Olá, seja bem-vindo
          {entrada_aluno.get()}!
          Sua idade é: {entrada_idade.get()}
          Sua nota é: {entrada_nota.get()}
          ''')
    limpar()

enviar = Button(text='Enviar', fg='#FFFAFA', bg='#1C1C1C', width=50, command=imprimir_aluno)


title.pack(pady=100)
nome.pack(side = 'left', padx = 0, pady = 10)
entrada_aluno.pack(side = 'left', padx = 0, pady = 10)
idade.pack(side = 'left', padx = 0, pady = 10)
entrada_idade.pack(side = 'left', padx = 0, pady = 10)
nota.pack(side = 'left', padx = 0, pady = 10)
entrada_nota.pack(side = 'left', padx = 0, pady = 10)
enviar.pack(side = 'left', padx = 0, pady = 10)

window.mainloop()
from tkinter import *

janela = Tk()

titulo = Label(
    text = 'Minha primeira interface gráfica',
    fg = 'red',
    bg = 'black'
)

nome = Label(text = 'Escreva seu nome')

entrada = Entry(background='red', fg='black')

def limpar():
    entrada.delete(0, END)

def imprimir_saudacao():
    print(f'''
          Olá, seja bem-vindo
          {entrada.get()}!
          ''')
    limpar()

enviar = Button(text='Enviar', fg='red', bg='black', width=50, command=imprimir_saudacao)


titulo.pack(pady=100)
nome.pack(side='left')
entrada.pack(side='right')
enviar.pack(side='bottom')

janela.mainloop()
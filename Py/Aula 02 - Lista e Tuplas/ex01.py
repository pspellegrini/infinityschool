'''
Ex01:
Crie uma lista, com os seus dados de nome, idade e altura, porém, eles precisam estar errados, por exemplo:

dados = ['Filipe', 20, 1.50]
dados[0] = 'Paulo'
dados[1] = 36
dados[2] = 1.74

print(f'Olá {dados[0]}, é bom ter você aqui! Vi que você informou que tem {dados[1]} anos e que tem {dados[2]} de altura, correto?')

Exemplo01:
Crie uma lista, com os seus dados de nome, idade e altura, porém, eles precisam estar errados, por exemplo:

#Entrada
dados = ['Fabricio', 35, 1.80 ]

#Processamento
resp = str(input(f'Olá {dados[0]}, é bom ter você aqui! Vi que você informou que tem {dados[1]} anos e que tem {dados[2]} de altura, correto [S/N]?')).strip().upper()

while resp != 'S':
    dados[0] = str(input('Informe seu nome: '))
    dados[1] = int(input('Informe sua idade: '))
    dados[2] = float(input('Informe sua altura: '))
    resp = str(input(f'Olá {dados[0]}, é bom ter você aqui! Vi que você informou que tem {dados[1]} anos e que tem {dados[2]} de altura, correto [S/N]?')).strip().upper()


Exemplo02:
'''
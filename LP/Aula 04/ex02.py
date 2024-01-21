'''
Ex02.
Peça ao usuário uma quantidade 'n' de números e a cada número, pergunte se o usuário deseja continuar ou não.
Ao final, mostre a soma dos números.

while True:
    n = float(input(f'Insira um valor: '))
    soma_n += n
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break
'''

#Entrada
soma_n = 0

#Processamento
resp = ''
while resp != 'N':
    n = float(input(f'Insira um valor: '))
    soma_n += n
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()

#Saída
print(f'A soma do valores lançados é {soma_n}.')
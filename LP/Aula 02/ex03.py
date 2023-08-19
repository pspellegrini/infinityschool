'''
Ex03:
Faça um programa que receba 3 números e diga qual é o maior número, ou se são iguais.
'''

#Entrada
n1 = float(input('Insira o 1º número: '))
n2 = float(input('Insira o 2º número: '))
n3 = float(input('Insira o 3º número: '))

#Processamento
if n1 == n2  and n2 == n3:
    print('Os valores são iguais.')
else:
    if n1 >= n2 and n1 >= n3:
        print(f'O valor {n1} é o maior número.')
    elif n2 >= n1 and n2 >= n3:
        print(f'O valor {n2} é o maior número.')
    elif n3 >= n1 and n3 >= n2:
        print(f'O valor {n3} é o maior número.')

'''
lista = [n1, n2, n3]

#Saída
print('O maior número encontrado é o {}'.format(max(lista)))
'''
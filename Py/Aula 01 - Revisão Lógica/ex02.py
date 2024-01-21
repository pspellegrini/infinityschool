'''Peça ao usuário 3 números, onde esses 3 serão do tipo float, agora verifique qual dos 3 números é o maior.'''

#Entrada
n1 = float(input(f'Insria o 1º número: '))
n2 = float(input(f'Insira o 2º número: '))
n3 = float(input(f'Insira o 3º número: '))

#Processamento

n1 = round(n1, 2)
n2 = round(n2, 2)
n3 = round(n3, 2)

#Saída
if n1 == n2 and n2 == n3:
    print(f'Os números informados são iguais.')
elif n1 > n2 and n1 > n3:
    print(f'O primeiro número é o maior.')
elif n2 > n1 and n2 > n3:
    print(f'O segundo número é o maior.')
else:
    print(f'o terceiro número é o maior.')
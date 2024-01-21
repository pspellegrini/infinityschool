# Ex02: Peça dois numeros, e mostre a soma entre eles.

# Entrada (Frontend)
numero1 = int(input('Digite o 1º numero: '))
numero2 = int(input('Digite o 2º numero: '))

# Processamento (Backend)
soma = numero1 + numero2

# Saida (Frontend)
print(f'{numero1} + {numero2} = {soma}')
print(str(numero1) + ' + ' + str(numero2) + ' = ' + str(soma))
print(numero1, '+', numero2, '=', soma)
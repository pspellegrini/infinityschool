'''
Ex05:
Faça um programa que recebe um numero e diz se ele é par ou impar

https://dontpad.com/infinity713-1208
'''

#Entrada

n = int(input('Digite um número para verificar se ele é par: '))

#Processamento

if n % 2 == 0:
    print('Esse número é par.')
else:
    print('Esse número é impar.')
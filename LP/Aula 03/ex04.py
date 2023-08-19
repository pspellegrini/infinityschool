'''
Ex04:
Mostre na tela todos os números impares de 1 à 100.
https://dontpad.com/infinity713-1908
'''

#Entrada
ni = 1
nf = 100

#Processamento
for numero in range(1, 100): 
    if numero % 2 == 1:
        print(numero)

'''
for numero in range(ni, nf +1):
    if numero % 2 != 0:
        print(numero, end = " ")
'''

#Saída
print('Fim do programa!')
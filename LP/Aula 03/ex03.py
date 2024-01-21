'''
Ex03:
Faça um programa que receba uma frase/palavra e conte quantas vogais tem. Ao final, mostre na tela essa quantidade.


palavra = 'Pastel'
for letra in palavra:
    print(letra)
'''

#Entrada
qtd_vogais = 0
string = input('Digite uma palavra ou frase para contagem de vogais: ')

#Processamento
for letra in string:
    if letra.lower() in 'aeiou':
        qtd_vogais += 1

#Saída
print(f'A string "{string}" tem {qtd_vogais} vogais.')
'''
Ex02:
Crie uma função que inverte uma string e a retorna de trás para frente.

    def revert(txt1: str) -> str:
        return txt1[::-1]

    print(revert('Olá'))

Crie uma função que recebe uma lista de palavras e retorna a palavra mais longa encontrada.

    def media_numeros(numeros: list) -> float:
        total = sum(numeros)
        media = total / len(numeros)
        return media

    numeros = [10, 20, 30, 40, 50]
    media = media_numeros(numeros)
    print(f'A média dos números é: {media}')

Escreva uma função chamada media_numeros que recebe uma lista de números e retorna a média deles.

    lista = [*range(1, 101)]

    def verificar_media(lista: list) -> str:
        soma = sum(lista)
        qnt_numeros = len(lista)
        return soma / qnt_numeros
    print(verificar_media(lista))





lista = ['Paulo', 'Tiago', 'Danilo', 'Caio', 'Mikhail', 'Bruna', 'Aline', 'Rubens']

txts = []

def verificar_txt(txt: list) -> str:
    for _ in range(10):
        txt = str(input(f'Digite um nome: ')).title()
        txts.append(txt)
    return f'O maior texto é {len(txts.append(txt))}.'
'''

lista = [*range(1, 101)]

def verificar_media(lista: list) -> str:
    soma = sum(lista)
    qnt_numeros = len(lista)
    return soma / qnt_numeros
print(verificar_media(lista))
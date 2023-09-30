'''
Ex01:

def verificar_palavras(txt1, txt2):
    if len(txt1) > len(txt2):
        return f'A palavra {txt1} é maior.'
    elif len(txt1) < len(txt2):
        return f'A palavra {txt2} é maior.'
    
print(verificar_palavras('Infinity', 'sc'))


def verificar_nomes(nome1, nome2):
    if len(nome1) > len(nome2):
        return f'O nome {nome1} é maior.'
    elif len(nome1) < len(nome2):
        return f'O nome {nome2} é maior.'
    else:
        return 'São iguais'

while True:
    nome1 = input('Digite seu nome: ')
    nome2 = input('Digite seu nome: ')
    
print(verificar_nomes(nome1, nome2))

Está dando um loop de nomes
'''

def verificar_palavras(txt1: str, txt2: str):
    if len(txt1) > len(txt2):
        return f'A palavra {Ttxt1} é maior.'
    elif len(txt1) < len(txt2):
        return f'A palavra {txt2} é maior.'
    else:
        return 'São iguais'

while True:
    txt1 = input('Digite uma palavra: ')
    txt2 = input('Digite uma palavra: ')

print(verificar_palavras(txt1, txt2))
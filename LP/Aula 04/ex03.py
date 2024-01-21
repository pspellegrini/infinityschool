'''
Ex03.
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

#Entrada


#Processamento
while True:
    n = input(f'Insira uma nota: ')
    if n.replace('.', '').isnumeric() and float(n) >= 0 and float(n) <= 10:
        break
    print('A nota informada é inválida. Digite novamente.')
    
#Saída
print(f'A nota informada para o aluno é {n}.')
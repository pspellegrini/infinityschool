'''
Ex02:
Faça um programa que possua um laço de repetição, que peça 10 nomes ao usuário.
'''

#Entrada
nomes = []

#Processamento
for _ in range(10):
    nome = str(input(f'Digite um nome: ')).title()
    nomes.append(nome)

#Saída
print(nomes)

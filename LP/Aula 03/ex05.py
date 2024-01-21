'''
Ex05:
Faça um programa que recebe nome, sexo e idade de 5 pessoas e que ao final mostre:

- Quem é a pessoa do sexo masculino mais velha.
- Qual é a idade da pessoa mais nova.
- Qual é a média das idades digitadas.
- Quantas pessoas do sexo feminino foram inseridas.
'''

#Entrada
#1.
nome_mais_velho = ''
idade_mais_velho = 0

#2.
idade_mais_novo = 0

#3.
soma_idades = 0

#4.
qnt_pessoas_feminino = 0

#Processamento
for n_pessoa in range (5):
    nome = str(input(f'Digite o {n_pessoa + 1}º nome: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Digite o sexo (M/F) da {n_pessoa + 1}º: ')).strip().upper()[0]
    idade = int(input(f'Digite a idade da {n_pessoa + 1}º: '))
    
    if sexo == 'M' and idade > idade_mais_velho:
        nome_mais_velho = nome
        idade_mais_velho = idade
    
    if n_pessoa == 0 or idade < idade_mais_novo:
        idade_mais_novo = idade
    
    #soma_idades = soma_idades + idade
    soma_idades += idade

    if sexo == 'F':
        qnt_pessoas_feminino += 1

media = soma_idades / 5

#Saída
print(f'{nome_mais_velho} tem {idade_mais_velho} anos e é a pessoa do sexo masculino mais velha.')
print(f'A idade da pessoa mais nova é de {idade_mais_novo}.')
print(f'A média das idades digitadas é de {media}.')
print(f'Foram cadastradas {qnt_pessoas_feminino} pessoas do sexo feminino.')
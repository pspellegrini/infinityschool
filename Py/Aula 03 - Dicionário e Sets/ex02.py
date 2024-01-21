'''
Ex02:

Leia os dados de um usuário - nome, sobrenome, idade, email - e imprima-os enumerando os mesmos.

Leia 4 notas de um aluno, calcule sua média e armazene em um dicionário as seguintes informações:
a. Nome do aluno
b. As 4 notas obtidas
c. Maior nota
d. Menor nota
e. Média
f. Situação
Agora imprima as informações deste aluno na saída padrão

Refaça o programa anterior e imprima a lista dos alunos aprovados em ordem decrescente da maior média para a menor

'''
import math
import statistics

users = []
notas = []

while True:
    user = {
        'nome': str(input(f'Digite o nome do aluno: ')).title(),
        'sobrenome': str(input(f'Digite o sobrenome do aluno: ')).title(),
        'idade': int(input(f'Digite a idade do aluno: ')),
        'email': str(input(f'Digite o e-mail do aluno: '))
    }
    users.append(user)
    print(user)
    choice = str(input(f'Hora de informar as notas. Você deseja continuar?[S/N] ')).strip().upper()
    if choice == 'Não' or choice == 'N':
        break
    
    nota = {
        'nota 1': input(f'Informe a nota do primeiro trimestre: '),
        'nota 2': input(f'Informe a nota do segundo trimestre: '),
        'nota 3': input(f'Informe a nota do terceiro trimestre: '),
        'nota 4': input(f'Informe a nota do quarto trimestre: ')
    }
    notas.append(nota)
    
    nota_usuario = dict.fromkeys(user, nota)
    print(nota_usuario)
    
    
    
    '''nota_maior = max(nota_usuario)
    nota_menor = min(nota_usuario)
    nota_media = statistics.mean(nota_usuario)

    print(f'A maior nota é {nota_maior}.')
    print(f'A menor nota é {nota_menor}.')
    print(f'A média das notas obtidas é {nota_media}.')

    if nota_media >= 7.0:
        print(f'Sendo assim, o aluno está aprovado.')
    else:
        print(f'Sendo assim, o aluno está reprovado.')'''
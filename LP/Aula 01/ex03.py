# Ex03: Peça o nome e 3 notas de um aluno, calcule a media
# e mostre na tela o boletim (Média e nome do aluno)

# Entrada
aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a 1ª Nota: '))
nota2 = float(input('Digite a 2ª Nota: '))
nota3 = float(input('Digite a 3ª Nota: '))

# Processamento
media =         (    nota1     +     nota2   + nota3) / 3
# media = round(media, 2)


# Saida
print(f'Nome: {aluno}')
print(f'Média: {media:.2f}')
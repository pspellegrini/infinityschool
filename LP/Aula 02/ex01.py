'''
Ex01:
Receba o nome de 3 notas de um aluno, calcule a média e ao final, mostre:
   - o nome
   - a média
   - e se está aprovado ou reprovado (>= 6 == aprovado)

'''
# Entrada

aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Insira a 1a nota: '))
nota2 = float(input('Insira a 2a nota: '))
nota3 = float(input('insira a 3a nota: '))

# Processamento
media = (nota1 + nota2 + nota3)/3
if media >= 6:
    situacao = 'Aprovado'
elif media >= 4:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

#Saída
print(f'O aluno {aluno} foi {situacao} com média {media:.2f}.')
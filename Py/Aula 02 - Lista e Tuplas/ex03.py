'''
Ex03:
Com base na questão anterior, continue o programa, porém, agora não coloque limite nesse programa, o laço só vai parar quando o usuário digitar um N ou um Não, isso ficará a sua escolha (Dicas: Use o while, condicionais e break)
'''

#Entrada
nomes = []

#Processamento
while True:
    nome = str(input(f'Digite um nome: ')).title()
    nomes.append(nome)
    resp = str(input(f'Deseja continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break

#Saída
print(nomes)
'''
Ex04:
Com base, também, na questão anterior, agora pergunte ao usuário se existe algum dado que ele deseja deletar, se sim, delete e mostre novamente a lista para ele.
'''

#Entrada
names = []
kill_names = []

#Processamento
while True:
    name = str(input(f'Digite um nome: ')).title()
    names.append(name)
    choice = str(input(f'Você deseja continuar?[S/N] ')).strip().upper()
    if choice == 'Não' or choice == 'N':
        break
    
    kill = str(input(f'Existe algum dado que deseje deletar? [S/N] ')).strip().upper()
    if kill == 'Sim' or kill == 'S':
        print(name)
        kill_names = int(input(f'Informe o índice que se deseja deletar: '))
        del names[kill_names]
        
print(names)
print(len(names))
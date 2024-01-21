'''Contagem de 0 a 9 com o while
count = 0
while count < 10:
    print(count)
    count += 1
print('Fim do laço!')

resp = ''
while resp != 'N':
    resp = input('Deseja continuar [S/N]? ')

while True:
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break








'''

count = 0
while count <= 10:
    count += 1
    if count % 2 == 1:
        continue
    print(count)  
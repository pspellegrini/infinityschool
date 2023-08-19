'''
Ex02:
Faça um programa que receberá 3 valores:

- Inicio da contagem;
- Final da contagem;
- Passo.

range(inicio, fim, passo)

ao final, utilize o laço "for" e o "range" para executar a contagem.
'''

#Entrada
vi = int(input('Digite o número que iniciará a contagem: '))
vf = int(input('Digite o número que finalizará a contagem: '))
p = int(input('Digite o número que sinalizará o passo: '))

#Processamento
if (vi < vf and p < 0) or (vf < vi and p > 0):
    p = -p

if vi < vf:
    a = 1
else:
    a = -1

'''
a = 1 if vi < vf else -1
#a = (se verdadeiro) if (condição) else (se falso)


'''


#Saída
for n in range(vi, vf + a, p):
    print(n, end=' ')
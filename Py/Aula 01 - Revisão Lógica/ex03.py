'''Peça ao usuário o valor em Fahrenheit, converta para Celsius e faça um bloco de condicionais, informando as seguintes questões, se o valor em Celsius estiver entre 20 e 25 graus, mande o usuário sair de bermuda, se estiver entre 19 e 15, mande ele levar um casaco, se estiver entre 0 e 14 mande ele assistir Netflix e tomar um café. Lembre-se, use sua criatividade, construa um terminal interativo para o usuário, peça o seu nome, por exemplo, faça seu código com qualidade.'''

#Entrada
F = float(input(f'Informe a temperatura em Fahrenheit: '))

#Processamento
C = (5/9)*(F-32)
C = round(C, 2)


#Saída
if C >25:
    print(f'Hoje é dia de praia, com essa temperatura.')
elif 25<= C >=20:
    print(f'A temperatura está boa para sair de bermuda.')
elif 19<= C >=15:
    print(f'É melhor levar um casaco com essa temperatura.')
elif 14<= C >=0:
    print(f'Fique em casa, assitindo um Neflix e tomando um café, pois a temperatura tá barril.')
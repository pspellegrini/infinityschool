'''
Ex02:
Faça um programa que receba uma temperatura em fahrenheit e converta para celcius; Ao final diga se está calor ou não (> 30 == Calor).

Formula: (ºF - 32) * 5/9
'''

#Entrada
temp_f = float(input('Digite a temperatura em fahrenheit: '))

#Processamento
temp_c = (temp_f - 32) * 5/9
if temp_c > 30:
    sensacao = 'calor'
elif temp_c >= 20:
    sensacao = 'agradável'
else:
    sensacao = 'frio'

#Saída
print(f'Hoje o dia está em {temp_c:.2f}ºC.')
print(f'Então está fazendo {sensacao}!')

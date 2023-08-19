'''
Ex04:
Faça um programa que recebe o peso e a altura de uma pesoa,ecalucle o seu IMC.
Ao final, mostre na tela o seu IMC e sua condição segundo a tabela do IMC.

Formula: imc = p / a^2

- 18,5 ou menos = Abaixo do peso
- Entre 18,6 e 24,9 = Peso ideal
- Entre 25,0 e 29,9 = Levemente acima do peso
- Entre 30,0 e 34,9 = Obesidade I
- Entre 35 e 39,9 = Obesidade II
- Acima de 40 = Obesidade III

'''

#Entrada
p = float(input('Informe seu peso: '))
a = float(input('Informe sua altura: '))

#Processamento
imc = p / a ** 2
if imc > 40:
    r = 'Obesidade III'
elif imc > 34.9:
    r = 'Obesidade II'
elif imc > 29.9:
    r = 'Obesidade'
elif imc > 24.9:
    r = 'Levemente acima do peso'
elif imc > 18.5:
    r = 'Peso ideal'
elif imc <= 18.5:
    r = 'Abaixo do peso'

'''
if imc <= 18.5:
    r = 'Abaixo do peso'
elif imc > 18.5 and < 25:
    r = 'Peso ideal'
'''


#Saída
print(f'Com base no seu peso e altura seu IMC é {imc:.2f} e sua condição é de {r}.')
print(f'IMC: {round(imc, 2)}')
print(f'Condição: {r}')
    
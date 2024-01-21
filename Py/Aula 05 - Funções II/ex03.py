'''
Ex03

1. Crie uma função lambda que calcule o quadrado de um número.

2. Crie uma função lambda para verificar se o número é par.

3. Crie uma função lambda para converter strings em maiúsculas.

4. Crie uma função lambda para calcular a área de um retângulo.
'''

soma = lambda x, y: x + y
print(soma(1, 2))

print((lambda x , y: x + y)(10, 10))

quadrado = lambda x: x**2
print(quadrado(2))
print((lambda x: x**2)(2))

par = lambda x: x % 2 == 0
print(par(3))
print((lambda x: x % 2 == 0)(3))

maiu = lambda x: x.upper()
print(maiu('Olá'))
print((lambda x: x.upper())('Olá'))

triangulo = lambda x, y: (x * y) / 2
print(triangulo(7, 5))
print((lambda x, y: (x * y) / 2)(7, 5))
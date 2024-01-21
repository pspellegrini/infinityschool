def somar(num: float, num2: float) -> float:
    return num + num2

def sub(num: float, num2: float) -> float:
    return num - num2

def multi(num: float, num2: float) -> float:
    return num * num2

def div(num: float, num2: float) -> float:
    return num / num2

def div_int(num: float, num2: float) -> float:
    return num // num2

def mod(num: float, num2: float) -> float:
    return num % num2

def potencia(num: float, num2: float) -> float:
    return num ** 2

from calculadora import *
# import calculadora as cls

if __name__ == '__main__':
    print('''
        Bem-vindo ao programa da calculadora
    ''')
    
    while True:
        num = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o primeiro número: '))

        print(somar(num, num2))
        print(sub(num, num2))
        print(multi(num, num2))
        print(div(num, num2))
        print(div_int(num, num2))
        print(mod(num, num2))
        print(potencia(num))

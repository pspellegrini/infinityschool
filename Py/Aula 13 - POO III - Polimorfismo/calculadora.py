class Calculadora:
    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__somar(num1, num2)
        elif op == '-':
            return self.__sub(num1, num2)
        elif op == '/':
            return self.__dividir(num1, num2)
        elif op == '*':
            return self.__mult(num1, num2)
        
    
    def __somar(self, num1, num2):
        return num1 + num2
    
    def __sub(self, num1, num2):
        return num1 - num2
    
    def __dividir(self, num1, num2):
        return num1 / num2
    
    def __mult(self, num1, num2):
        return num1 * num2
    
calculadora = Calculadora()
print(calculadora.calcular('+', 5, 5))
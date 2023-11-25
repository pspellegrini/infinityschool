class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.__salario = salario
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario: float):
        self.__salario = novo_salario

eric = Pessoa('Eric', 43, '12345678910', 6700)
print(eric.nome)
print(eric.idade)
print(eric.cpf)
print(eric.salario)

eric.salario = 10000
print(eric.salario)


    
'''
pessoa1 = Pessoa('Filipe', 23, '12345678910')

print(pessoa1.nome)
print(pessoa1.idade)
'''

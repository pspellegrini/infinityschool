'''class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

p1 = Pessoa('Felipe')
str'''


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.classname = self.__class__.__name__
    
    def falar(self):
        return f'{self.classname} está falando.'

class Aluno(Pessoa):
    def estudar(self):
        return f'{self.nome} está estudando.'

class Cliente(Pessoa):
    def comprar(self):
        return f'{self.nome} está comprando.'
    

'''a1 = Aluno('Eric', 44)
print(a1.__dict__)
print(a1.estudar())
print(a1.falar())'''
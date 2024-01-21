from random import randint


class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.matricula = randint(1000, 5000)

c1 = Cliente('Paulo')
print(c1.__dict__)
'''
Cliente, nome, matricula, saldo

Conta Investimento - Injete

Conta Poupança - Retirar Dinehiro e injetar

'''

class Conta:
    def __init__(self, saldo: float) -> None:
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor


class Poupança(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        return 'Saldo insuficiente'  


class Investimento(Conta):
    ...
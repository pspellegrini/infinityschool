class Animal:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso        
    
    def comer(self) -> str:
        return f'{self.nome} está comendo.'
    
    def locomover(self) -> str:
        return f'{self.nome} está se movendo.'
    
    def emitir_som(self) -> str:
        return f'{self.nome} está emitindo som.'


a1 = Animal('Leao', 8, 10)
print(a1.__dict__)

class Mamifero(Animal):
    def __init__(self, nome: str, idade: int, peso: float, tem_pelo: bool = True) -> None:
        super().__init__(nome, idade, peso)
        self.tem_pelo = tem_pelo
              
class Ave(Animal):
    def __init__(self, nome: str, idade: int, peso: float, voar: bool = True) -> None:
        super().__init__(nome, idade, peso)
        self.voar = voar
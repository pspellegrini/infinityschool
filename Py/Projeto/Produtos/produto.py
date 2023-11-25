class Produto:
    def __init__(self, nome: str, preco: float, categoria: str, descricao: str) -> None:
        self.nome = nome
        self.__preco = preco
        self.__categoria = categoria
        self.descricao = descricao

    @property
    def preco(self):
        return self.__preco
    
    @property
    def categoria(self):
        return self.__categoria
    
    @preco.setter
    def preco(self, novo_preco: float):
        self.__preco = novo_preco
        return f'O preço do {self.nome} foi alterado com sucesso.'


''''
caneta_azul = Produto('Caneta Azul',2.57, 'Caneta e Refis', 'Formato triangular ergonômico, garantia de conforto e melhor escrita, Ponta média de 1, 0mm: escrita macia, sem falhas ou borrões e Código de barras no corpo do produto')

print(caneta_azul.nome)
print(caneta_azul.preco)
print(caneta_azul.categoria)
print(caneta_azul.descricao)

caneta_azul.preco = 3.78
print(caneta_azul.preco)
'''

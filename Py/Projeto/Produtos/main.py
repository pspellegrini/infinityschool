from produto import Produto

lista_produtos = []

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: '))
    categoria = input('Categoria do produto: ')
    descricao = input('Descrição do produto: ')
    produto = Produto(
        nome,
        preco,
        categoria,
        descricao
     )

    lista_produtos.append(produto)
    
    escolha = input('Deseja continuar? (N/S)').upper()
    if escolha == 'N':
        break

for prod in lista_produtos:
    print('#####')
    print(f'Nome: {prod.nome}')
    print(f'Preço: {prod.preco}')
    print(f'Categoria: {prod.categoria}')
    print(f'Descrição: {prod.descricao}')
    
'''
print(lista_produtos[0].__dict__)
produto1 = Produto('Caneta Azul',2.57, 'Caneta e Refis', 'Formato triangular ergonômico, garantia de conforto e melhor escrita, Ponta média de 1, 0mm: escrita macia, sem falhas ou borrões e Código de barras no corpo do produto')
'''
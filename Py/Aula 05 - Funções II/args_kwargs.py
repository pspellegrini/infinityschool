def minha_funcao(*args):
    for i in args:
        return i

print(minha_funcao(('Paulo', 'Tiago', 'Danilo', 'Caio', 'Mikhail', 'Bruna', 'Aline', 'Rubens')))


def minha_funcao_kwargs(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} ----------- {valor}')

print(minha_funcao_kwargs(a=22, b=13, c=11))
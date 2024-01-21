lista = [*range(1,11)]


def numero_par(num: int):
    if num % 2 == 0:
        return num

lista2 = filter(numero_par, lista)
lista2 = list(lista2)
print(lista2)
print(list(filter(lambda x: x % 2 == 0, lista)))
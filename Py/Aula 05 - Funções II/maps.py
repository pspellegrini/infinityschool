def multiplicar(num1: int) -> int:
    return num1 * 2
lista = [*range(1, 101)]
lista2 = map(multiplicar, lista)

lista2 = list(lista2)
print(lista2)


print(list(map(lambda x: x * 2, lista)))

a = 1
b = 1

if a + b <= 2:
    print(True)
else:
    print(False)

a = 2
if a > (14 % 2):
    print(True)
else:
    print(False)

a = 15
if a // (3 ** 2) != 5:
    print(True)
else:
    print(False)

a = 99
if a - 1 >= 3 / 3:
    print(True)
else:
    print(False)

a = 17
if a % (3 + (17 // (2 ** 4))) == 13 + (1 ** 0):
    print(True)
else:
    print(False)


print(True or False and not False)


x = 4
if x == 4:
    print("x é igual a 4")
else:
    print("x é diferente de 4")


x = 4
if x == 4:
    print("x é igual a 4")
elif x != 4:
    print("x é diferente de 4")

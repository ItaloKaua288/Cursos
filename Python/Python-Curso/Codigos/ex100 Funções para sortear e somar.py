from random import randint
from time import sleep


def sorteia():
    numeros.append(randint(1, 5))
    numeros.append(randint(1, 5))
    numeros.append(randint(1, 5))
    numeros.append(randint(1, 5))
    numeros.append(randint(1, 5))
    print(f'Os números sorteados foram:', end=' ')
    for x in range(0, len(numeros)):
        print(numeros[x], end=' ')
        sleep(0.5)


def somaPar():
    soma = 0
    sleep(0.5)
    for x in range(0, len(numeros)):
        if numeros[x] % 2 == 0:
            soma += numeros[x]
    print(f'\nA soma dos valores pares de {numeros} é:', end=' ')
    sleep(0.5)
    print(soma)


numeros = list()

sorteia()
somaPar()

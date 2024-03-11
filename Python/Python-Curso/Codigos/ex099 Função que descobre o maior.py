def maior(*num):
    lista = list()
    if len(num) == 0:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor passado foi 0')
    else:
        lista.append(num)
        maior = 0
        for x in range(0, len(lista[0])):
            if x == 0:
                maior = lista[0][x]
            else:
                if lista[0][x] > maior:
                    maior = lista[0][x]
        print(f'O maior valor passado foi {maior}')
def cabeçalho():
    print('='*50)
    print('Analisando os valores passados...')


cabeçalho()
maior(2, 9, 4, 5, 7, 1)
cabeçalho()
maior(4, 7, 0)
cabeçalho()
maior(1, 2)
cabeçalho()
maior(6)
cabeçalho()
maior()

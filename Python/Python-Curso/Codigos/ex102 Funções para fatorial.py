def fatorial(num=0, show=False):
    """
        Calcula o fatorial de um número
    :param num: Número que vai ser calculado o fatorial
    :param show: True para mostrar o processor e calculo e False para mostrar só o resultado
    :return: Retorna o valor para fat
    """
    fat = num
    cont = num
    if num == 0:
        return 0
    if not show:
        if cont > 0:
            while cont != 1:
                cont -= 1
                fat *= cont
            return fat
    else:
        while cont != 0:
            if cont != 1:
                print(f'{cont} x ', end='')
                cont -= 1
            else:
                print(f'{cont}', end=' = ')
                break
        cont2 = num
        while cont2 != 1:
            cont2 -= 1
            fat *= cont2
        return fat


fat1 = fatorial(3, show=True)

print(fat1)
'''help(fatorial)'''

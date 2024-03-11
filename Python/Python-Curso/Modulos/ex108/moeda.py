def moeda(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def aumentar(n=0, n2=0):
    resul = n + n * (n2 / 100)
    return f'R${resul:.2f}'.replace('.', ',')


def diminuir(n=0, n2=0):
    resul = n - n * (n2 / 100)
    return f'R${resul:.2f}'.replace('.', ',')


def dobro(n=0):
    n *= 2
    return f'R${n:.2f}'.replace('.', ',')


def metade(n=0):
    n /= 2
    return f'R${n:>.2f}'.replace('.', ',')

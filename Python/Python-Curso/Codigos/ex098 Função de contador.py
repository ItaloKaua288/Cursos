from time import sleep


def contador(i, f, p):
    p = p
    if p == 0 or p == '':
        p = 1
    else:
        p = int(p)
    if f > i:
        if p > 0:
            for x in range(i, f+1, p):
                print(f'{x}', end=' ')
                sleep(0.5)
            print('=Fim=')
        else:
            for x in range(i, f+1, p*-1):
                print(f'{x}', end=' ')
                sleep(0.5)
            print('=Fim=')
    elif i == f:
        print(i)
        print('=Fim=')
    if i > f:
        if p > 0:
            for x in range(i, f-1, -p):
                print(f'{x}', end=' ')
                sleep(0.5)
            print('=Fim=')
        else:
            for x in range(i, f-1, p):
                print(f'{x}', end=' ')
                sleep(0.5)
            print('=Fim=')

print('='*30)
print('Contagem de 1 até 10 em 1')
contador(1, 10, 1)
print('='*30)
print('Contagem de 10 até 0 em 2')
contador(10, 0, 2)
print('\nAgora é sua vez')
contador(int(input('Inicio: ')), int(input('Fim: ')), (input('Passos: ')))

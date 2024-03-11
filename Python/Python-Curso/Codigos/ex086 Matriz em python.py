valores = [input('Digite um número: '), input('Digite um número: '), input('Digite um número: '),
           input('Digite um número: '), input('Digite um número: '), input('Digite um número: '),
           input('Digite um número: '), input('Digite um número: '), input('Digite um número: ')]
print('='*36)
for x in range(0, 9):
    if x != 3 and x != 6:
        print(f'({valores[x]: ^10})', end='')
    else:
        print(f'\n({valores[x]: ^10})', end='')
print('\n=', end='')
print('='*35)

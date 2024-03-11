valores = [(input('Digite um número: ')), input('Digite um número: '), input('Digite um número: '),
           input('Digite um número: '), input('Digite um número: '), input('Digite um número: '),
           input('Digite um número: '), input('Digite um número: '), input('Digite um número: ')]
soma = 0
soma3c = 0
maior2l = []
print('='*36)
for x in range(0, 9):
    if x != 3 and x != 6:
        print(f'({valores[x]: ^10})', end='')
    else:
        print(f'\n({valores[x]: ^10})', end='')
    soma += int(valores[x])
    if x == 2 or x == 5 or x == 8:
        soma3c += int(valores[x])
    if x == 0:
        maior2l.append(valores[x])
    else:
        if int(maior2l[0]) < int(valores[x]) and 3 > x:
            maior2l.clear()
            maior2l.append(valores[x])
    '''else:
        if x == 1 or x == 2 and x > maior2l:
            maior2l = valores[x]'''

print('\n=', end='')
print('='*35)
print(f'A soma dos números na matriz é: {soma}')
print(f'A soma dos valores da coluna 3 é: {soma3c}')
print(f'O maior valor da linha 2 é: {maior2l}')
print('='*36)
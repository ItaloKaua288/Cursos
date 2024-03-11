lista = [int(input('Digite o número da posição 0: ')), int(input('Digite o número da posição 1: ')), int(input('Digite o número da posição 2: ')),
         int(input('Digite o número da posição 3: ')), int(input('Digite o número da posição 4: '))]
# maior = lista.count(max(sorted(lista)))
# menor = lista.count(min(sorted(lista)))

print('='*71)
if min(sorted(lista)) == max(sorted(lista)):
    print('Todos são iguais! Portanto não existe um menor e um maior.')
else:
    print(f'O maior número da lista é: {max(sorted(lista))} e está na posição', end=' ')
    while True:
        for x in range(0, len(lista)):
            if lista[x] == max(sorted(lista)):
                print(f'{x}...', end=' ')
        else:
            break
    print(f'\nO menor número da lista é: {min(sorted(lista))} e está na posição', end=' ')
    while True:
        for x in range(0, len(lista)):
            if lista[x] == min(sorted(lista)):
                print(f'{x}...', end=' ')
        else:
            print('\n=', end='')
            break
print('='*70)

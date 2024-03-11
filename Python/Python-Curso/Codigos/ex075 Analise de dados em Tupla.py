lista = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais numero: ')),
       int(input('Digite ultimo numero: ')))
print('='*40)
print(f'Você digitou os valores {lista}')
print(f'O 9 apareceu {lista.count(9)} vezes')
if 3 not in lista:
    print('Você não digitou nenhum 3')
else:
    print(f'O primeiro número 3 aparece na posição {lista.index(3)+1}')

if lista[0] % 2 == 0 or lista[1] % 2 == 0 or lista[2] % 2 == 0 or lista[3] % 2 == 0 or lista[4] % 2 == 0:
    print('Os numeros pares são: ', end=' ')
    for c in range(0, 4):
        if lista[c] % 2 == 0:
            print(lista[c], end=' ')
print('\n=', end='')
print('='*39)

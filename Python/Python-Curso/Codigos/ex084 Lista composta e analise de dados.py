pessoas = []
dado = []
Mapesa = list()
Mepesa = list()
continuar = 'S'
while continuar == 'S':
    dado.append(input('Nome: '))
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    continuar = input('Deseja continuar S/N?').upper().strip()
    while True:
        if continuar not in 'SN':
            continuar = input('Deseja continuar S/N?').upper().strip()
        break
    if continuar == 'N':
        break
for c in range(0, len(pessoas)):
    if c == 0:
        Mapesa.append(pessoas[c])
        Mepesa.append(pessoas[c])
    if c > 0:
        if pessoas[c][1] == Mapesa[0][1]:
            Mapesa.append(pessoas[c])
        elif pessoas[c][1] == Mepesa[0][1]:
            Mepesa.append(pessoas[c])
        else:
            if pessoas[c][1] > Mapesa[0][1]:
                Mapesa.clear()
                Mapesa.append(pessoas[c])
            elif pessoas[c][1] < Mepesa[0][1]:
                Mepesa.clear()
                Mepesa.append(pessoas[c])
print('='*50)
(f'Foram cadastradas {len(pessoas):.0f} pessoas')
if len(Mapesa) > 0:
    print(f'O maior peso foi de {Mapesa[0][1]}kg de: ', end='')
    for x in range(0, len(Mapesa)-1):
        print(f'{Mapesa[x][0]}', end=', ')
    print(f'{Mapesa[-1][0]}')
else:
    print(f'O maior peso foi de {Mapesa[0][1]} de: {Mapesa[0][0]}')
if len(Mepesa) > 0:
    print(f'O menor peso foi de {Mepesa[0][1]}kg de: ', end='')
    for x in range(0, len(Mepesa)-1):
        print(f'{Mepesa[x][0]}', end=', ')
    print(f'{Mepesa[-1][0]}')
else:
    print(f'O menor peso foi de {Mepesa[0][1]} de: {Mepesa[0][0]}')
print('='*50)

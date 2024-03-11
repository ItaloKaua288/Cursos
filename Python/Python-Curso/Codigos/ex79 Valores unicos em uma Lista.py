valores = []
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número: ').strip())
    if num not in valores:
        valores.append(num)
    continuar = input('Deseja continuar S/N?').upper().strip()
    while continuar not in 'SN':
        if continuar not in 'SN':
            print('DIGITE UMA OPÇÂO VÁlIDA!')
            continuar = input('Deseja continuar S/N?').upper().strip()
    if continuar == 'N':
        break
print(f'Os valores únicos digitados em ordem crescente: {sorted(valores)}')

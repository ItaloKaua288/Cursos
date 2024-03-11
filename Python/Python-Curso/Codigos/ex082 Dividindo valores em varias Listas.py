lista = []
listaP = []
listaI = []
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = input('Deseja continuar S/N?').strip().upper()
    while continuar not in 'SN':
        if continuar not in 'SN':
            print('DIGITE UMA OPÇÂO VÁLIDA')
            continuar = input('Deseja continuar S/N?').strip().upper()
for x in range(0, len(lista)):
    if lista[x] % 2 == 0:
        listaP.append(lista[x])
    else:
        listaI.append(lista[x])
print('='*60)
print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram: {listaP}')
print(f'Os números impares digitados foram: {listaI}')
print('=-=FIM=-=')
print('='*60)
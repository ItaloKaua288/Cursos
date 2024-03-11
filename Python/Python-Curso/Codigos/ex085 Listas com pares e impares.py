lista = []
dadoP = []
dadoI = []

for x in range(1, 8):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        dadoP.append(num)
    else:
        dadoI.append(num)
lista.append(dadoP[:])
lista.append(dadoI[:])
print('='*60)
print(f'Os números impares digitados foram: {sorted(lista[1])}')
print(f'Os números pares digitados foram: {sorted(lista[0])}')
print('='*60)

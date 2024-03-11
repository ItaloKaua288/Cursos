lista = ('Pão', 1.00, 'Açucar', 3.50, 'Suco', 200.00, 'Chocolate', 1.50, 'Bolacha Maria', 5.00)

print(f'{"="*33}')
print(f'{"LISTA DE PREÇOS": ^31}')
print(f'{"="*33}')
for x in range(0, len(lista)):
    if x % 2 == 0:
        print(f'{lista[x]:.<25}', end='')
    if x % 2 != 0:
        print(f'R${lista[x]: >6.2f}')
print(f'{"="*33}')

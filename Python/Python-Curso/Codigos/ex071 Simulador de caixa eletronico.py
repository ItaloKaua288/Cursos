valorsac = int(input('Vai sacar quanto? '))
r50 = 0
r20 = 0
r10 = 0
r1 = 0
resto = 0
print('='*30)
if valorsac >= 50:
    r50 = valorsac // 50
    resto = valorsac % 50
    print(f'Total de {r50} notas de R$ 50')
if resto // 20 != 0:
    r20 = resto // 20
    resto = resto % 20
    print(f'Total de {r20} notas de R$ 20')
if resto // 10 != 0:
    r10 = resto // 10
    resto = resto % 10
    print(f'Total de {r10} notas de R$ 10')
r1 = resto
if r1 != 0:
    print(f'Total de {r1} notas de R$ 1')
else:
    print(f'{valorsac} notas de R$ 1')
print('='*30)

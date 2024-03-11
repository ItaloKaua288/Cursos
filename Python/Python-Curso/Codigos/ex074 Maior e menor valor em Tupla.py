from random import randint
lista = (randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))
print('='*50)
print(f'A listagem dos números é: {lista}')
print(f'O menor valor da tupla é {sorted(lista)[0]}')
print(f'O maior valor da tupla é {sorted(lista)[-1]}')
print('='*50)


# OU

'''print('='*50)
print(f'A listagem dos números é: {lista}')
print(f'O menor valor da tupla é {max(lista)}')
print(f'O maior valor da tupla é {min(lista)}')
print('='*50)'''

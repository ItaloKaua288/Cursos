totalG = 0
mais1000 = 0
nomeB = ''
precobarato = 0

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Qual o preço do produto? '))
    totalG += preco
    continuar = 'S'
    if preco > 1000:
        mais1000 += 1
    if precobarato == 0:
        precobarato = preco
        nomeB = nome
    else:
        if precobarato > preco:
            precobarato = preco
            nomeB = nome
    continuar = input('Deseja continuar S/N?').upper().strip()
    while continuar not in 'SN':
        print('Digite uma opção válida:')
        continuar = input('Deseja continuar S/N?').upper().strip()
    if continuar != 'S':
        break

print('='*40)
print(f'R$ {totalG:.2f} foi o tatal gasto')
print(f'{mais1000} custam mais de R$ 1000,00')
print(f'{nomeB} é o produto mais barato custando R$ {precobarato}')
print('='*40)

maior = 0
menor = 0
soma = 0
cont = 0
continuar = 'S'

while continuar != 'N':
    num = int(input('Digite um número: '))
    continuar = input('Deseja continuar S/N? ').upper().strip()
    cont += 1
    soma += num

    if num > maior:
        maior = num
    if menor == 0:
        menor = num
    elif menor > num:
        menor = num

    while continuar not in 'SN':
        print('Digite uma resposta válida!')
        continuar = input('Deseja continuar S/N? ').upper().strip()

print('A média dos valores digitados é {:.2f}'.format(soma / cont))
print('Foram digitados {} números'.format(cont))
print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))

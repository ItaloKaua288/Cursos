def leiaint(num):
    a = input(f'{num}:').strip()
    while True:
        if a.isnumeric():
            return a
        else:
            print('\033[31mERRO DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            a = input(f'{num}:').strip()


n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o valor {n}')

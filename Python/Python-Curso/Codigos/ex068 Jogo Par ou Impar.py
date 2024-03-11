from random import randint

comput = randint(1, 11)
escolha = input('Par ou impar? ').upper().strip()

while True:
    num = int(input('Digite um número de 1 a 10: ').strip())
    while num not in (1, 2 , 3 , 4 , 5 , 6 ,7 ,8 ,9 , 10):
        print('Digite uma opção válida')
        num = int(input('Digite um número de 1 a 10: ').strip())

    if (comput + num) % 2 == 0:
        if escolha == 'IMPAR':
            print('Você perdeu!')
        else:
            print('Você venceu!')
    elif (comput + num) % 2 != 0:
        if escolha == 'IMPAR':
            print('Você venceu!')
        else:
            print('Você perdeu!')
    troca = input('Desejar trocar S/N? ').upper()
    while troca not in 'SN':
        print('Digite uma opção válida')
        troca = input('Desejar trocar S/N? ').upper()
    if troca == 'S':
        escolha = input('Par ou impar? ').upper().strip()

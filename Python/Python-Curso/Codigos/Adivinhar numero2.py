from random import randint
from time import sleep

num=randint(1, 10)
chute = -1

print('PROCESSANDO...')
sleep(3)
print('Computador escolheu um número de 1 a 10')

while num != chute:
    print('Tente um número')
    chute = int(input('Qual o número? '))
    if chute != num:
        print('Você errou!')
        if chute < num:
            print('chute mais alto!')
        elif chute > num:
            print('chute mais baixo!')
    else:
        print('Você acertou! Parabéns!')

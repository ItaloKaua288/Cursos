from random import randint
from time import sleep

num=randint(0, 5)
chute=int(input('Chute um número: '))

print('PROCESSANDO...')
sleep(3)

if chute==num:
    print('Você acertou!')
else:
    print('Você errou')
     
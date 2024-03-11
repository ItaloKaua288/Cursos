from random import randint
from time import sleep

print('='*20)
print('Jogo Começou')
print('-'*20)

computador=str(randint(1, 3))
jogador=input('Pedra, papel ou tesoura? ').lower().strip()
vitorias=['1papel', '2tesoura', '3pedra']
derrotas=['1tesoura', '2pedra', '3papel']
empates=['1pedra', '3tesoura', '2papel']
#pedra=1 papel=2 tesoura=3

print('PROCESSANDO...')
sleep(3)

a=computador+jogador

if a in vitorias:
    print('Você venceu!')
elif a in derrotas:
    print('Você perdeu!')
elif a in empates:
    print('Você empatou')

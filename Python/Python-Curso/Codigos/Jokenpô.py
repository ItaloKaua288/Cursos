from random import randint
from time import sleep

computador=randint(1, 3)
jogador=(input('Pedra, papel ou tesoura? '))
computador1=str()
if computador==1:
    pedra=computador1='pedra'
elif computador==2:
    computador1='papel'
elif computador==3:
    computador1='tesoura'
#pedra=1 papel=2 tesoura=3

print('PROCESSANDO...')
sleep(3)
print('Computador escolheu {}'.format(computador1))

if computador1==jogador:
    print('Empate!')
elif computador!=jogador:
    if computador==1 and jogador=='papel':
        print('Você venceu!')
    elif computador==1 and jogador=='tesoura':
        print('Você perdeu!')
    elif computador==2 and jogador=='pedra':
        print('Você perdeu!')
    elif computador==2 and jogador=='tesoura':
        print('Você venceu!')
    elif computador==3 and jogador=='pedra':
        print('Você venceu!')
    elif computador==3 and jogador=='papel':
        print('Você perdeu!')

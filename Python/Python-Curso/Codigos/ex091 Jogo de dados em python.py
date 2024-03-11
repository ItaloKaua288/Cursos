from random import randint
from time import sleep
dados = {}
print('Valores sorteados:')
for x in range(1, 5):
    dados[f'jogador{x}'] = int(randint(1, 6))
    print(f'   O jogador{x} tirou {dados[f"jogador{x}"]}')
    sleep(0.5)
print('Ranking dos jogadores:')
for x in sorted(dados, key=dados.get, reverse=True):
    print(f'1 lugar: {x} com {dados[x]}')
    sleep(0.5)
# ou
'''from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador1': randint(0, 6), 'Jogador2': randint(0, 6), 'Jogador3': randint(0, 6), 'Jogador4': randint(0, 6)}
ranking = []

print('==Valores sorteados==')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
print('==RANKING DOS JOGADORES==')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i+1} lugar é o {v[0]} com {v[1]}')
    sleep(0.5)'''
from random import randint
palpites = []
dados = []
jogos = int(input('Quantos jogos deseja ver? '))
while jogos != 0:
    for x in range(0, 6):
        dados.append(randint(1, 60))
    palpites.append(dados[:])
    dados.clear()
    jogos -= 1
print('='*35)
print(f'{"OS PALPITES SÂO:": ^35}')
print('='*35)
for c in range(0, len(palpites)):
    if c < len(palpites):
        print(f'Jogo {c + 1}: {sorted(palpites[c])}')
print('='*35)

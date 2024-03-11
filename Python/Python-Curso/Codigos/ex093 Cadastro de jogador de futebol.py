jogador = {}
gols = []
total = 0
jogador['Nome'] = input('Nome: ')
jogador['Partidas'] = int(input('Número de partidas: '))
partidas = jogador['Partidas']

while partidas != 0:
    for x in range(0, partidas):
        if x == 1:
            gols.append(int(input(f'Quantos gols na partida {x+1}?')))
            partidas -= 1
            total += gols[x]
        else:
            gols.append(int(input(f'Quantos gols na partida {x+1}?')))
            partidas -= 1
            total += gols[x]
jogador['Gols'] = gols[:]
jogador['Total'] = total          # ou jogador['Total'] = sum(gols)

print('='*60)
print(jogador)
print('='*60)
print(f'Nome: {jogador["Nome"]}')
print(f'Gols: {jogador["Gols"]}')
print(f'Total: {jogador["Total"]}')
print('='*60)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} jogos')
for x in range(0, len(gols)):
    print(f'   Na partida {x+1} ele fez {gols[x]} gols')
print(f'Foi um total de {jogador["Total"]} gols')
print('='*60)

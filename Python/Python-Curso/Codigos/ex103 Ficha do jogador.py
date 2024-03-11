def ficha(nome, gols=0):
    print('-'*30)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


n = input('Nome do jogador: ').strip()
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    n = '<desconhecido>'
ficha(n, g)

jogador = {}
gols = []
total = 0

while True:
    dados = {}
    dados['Nome'] = input('Nome: ')
    dados['Partidas'] = int(input('Quantas partidas? '))
    for x in range(0, dados['Partidas']):
        gols.append(int(input(f'Quantos gols na partida {x + 1}: ')))
        total += int(gols[x])
    dados['Gols'] = gols[:]
    gols.clear()
    dados['Total'] = total
    jogador[f'jogador{len(jogador)+1}'] = dados.copy()
    continuar = (input('Deseja continuar S/N? ').strip().upper())
    while continuar not in 'SN':
        print('DIGITE UMA OPÇÂO VÁLIDA')
        continuar = (input('Deseja continuar S/N? ').strip().upper())
    if continuar == 'N':
        break

print('='*60)
print(jogador)
print('='*60)
print(f'{"Cod. Nome":-<10}{"Gols":->15}{"Total":->17}')
for x in range(1, len(jogador) + 1):
    print(f'{x}    {jogador[f"jogador{x}"]["Nome"]:-<16}', end='')
    print(f'{jogador[f"jogador{x}"]["Gols"]}', end='')
    print(f'{jogador[f"jogador{x}"]["Total"]:-<10}')
while True:
    resp = str(input('DESEJA VER OS DADOS DE QUAL J? ').upper().strip())
    if resp not in 'SN':
        print('ERRO')
    if resp == 'N':
        break
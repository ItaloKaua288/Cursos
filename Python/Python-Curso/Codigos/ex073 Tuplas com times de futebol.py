colocados = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atletico-PR', 'Atletico-MG',
             'Fortaleza', 'São Paulo', 'America-MG', 'Bota Fogo', 'Santos', 'goiais', 'Bragantino', 'Coritiba',
             'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')
print('\033[32m=-=\033[m'*20)
print(f'Os 5 primeiros colocados são:\033[34m {colocados[:5]}\033[m')
print(f'Os ultimos 4 colocados da tabela são:\033[34m {colocados[-4:]}\033[m')
print(f'Os times em ordem alfabetica:\033[34m {sorted(colocados)}\033[m')
print(f'O São Paulo está na posição:\033[34m {colocados.index("São Paulo")}\033[m')
print('\033[32m=-=\033[m'*20)

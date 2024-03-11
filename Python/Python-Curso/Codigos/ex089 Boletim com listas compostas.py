boletim = []
dados = []
continuar = 'S'
while continuar == 'S':
    dados.append(input('Digite o nome do aluno: '))
    dados.append(int(input('Digite a primeira nota do aluno: ')))
    dados.append(int(input('Digite a segunda nota do aluno: ')))
    boletim.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar S/N? ').strip().upper()
    while continuar not in 'SN':
        print('DIGITE UMA OPÇÂO VÁLIDA')
        continuar = input('Deseja continuar S/N? ').strip().upper()
    if continuar == 'N':
        break
print('='*33)
print(f'{"BOLETIM DOS ALUNOS:": ^33}')
print('='*33)
print(f"{'No. Nome': <25}{'Média': >8}")
print('='*33)
for x in range(0, len(boletim)):
    if len(boletim) == 1:
        print(f'{1} Nome: {boletim[0][0]: <15}{(boletim[0][1] + boletim[0][2]) / 2: >10}')
        break
    else:
        print(f'{x+1} Nome: {boletim[x][0]: <15}{(boletim[x][1] + boletim[x][2]) / 2: >10.1f}')
print('='*33)
while True:
    nota = int(input('Deseja ver as notas de quem? (999 interrompe): '))
    if nota == 999:
        break
    print(f'Notas de {boletim[nota-1][0]} são {boletim[nota-1][1]} e {boletim[nota-1][2]}')

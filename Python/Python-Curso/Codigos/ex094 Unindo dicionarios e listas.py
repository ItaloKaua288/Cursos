dados = []
Pessoa = {}
mulheres = []
cont = 1
media = 0
acima = []
while True:
    Pessoa['Nome'] = input('Digite o nome: ').capitalize().strip()
    Pessoa['Idade'] = int(input('Digite a idade: ').strip())
    Pessoa['Sexo'] = input('Digite o sexo M/F').upper().strip()
    while Pessoa['Sexo'] not in 'MF':
        Pessoa['Sexo'] = input('Digite o sexo M/F').upper().strip()
    if Pessoa['Sexo'] == 'F':
        mulheres.append(Pessoa['Nome'])
    dados.append(Pessoa.copy())
    Pessoa.clear()
    cont += 1
    continuar = (input('Deseja continuar S/N?').strip().upper())
    while continuar not in 'SN':
        print('DIGITE UMA OPÇÂO VÁLIDA')
        continuar = (input('Deseja continuar S/N?').strip().upper())
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(dados)} ')
for i in range(0, len(dados)):
    media += dados[i]['Idade']
print(f'A média das idades é {media / len(dados):.1f} anos')
print(f'As mulheres são: {mulheres}')
print('\n==Lista das pessoas ascima da média:')
for x in range(0, len(dados)):
    if int(dados[x]['Idade']) > media / len(dados):
        '''acima.append(dados[x]['Idade'])'''
        print(f'Nome= {dados[x]["Nome"]}, Idade= {dados[x]["Idade"]}, Sexo= {dados[x]["Sexo"]}')

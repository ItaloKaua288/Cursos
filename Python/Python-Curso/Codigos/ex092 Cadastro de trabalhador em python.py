from datetime import date

dados = dict()

dados['Nome'] = input('Nome: ')
dados['Idade'] = date.today().year - int(input('Ano de nascimento:'))
dados['CTPS'] = int(input('Número da carteira de trabalho (0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposento'] = dados['Idade'] + (35 - (date.today().year - dados['Ano de Contratação']))

print('='*30)
for k, v in dados.items():
    print(f'O {k} é: {v}')

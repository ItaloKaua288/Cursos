alunos = {}

alunos['Nome'] = input('Qual o nome: ')
alunos['Média'] = float(input(f'Qual a média de {alunos["Nome"]}: '))
if alunos['Média'] >= 6:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'
print(f'O nome é igual a {alunos["Nome"]}')
print(f'A média é igual a {alunos["Média"]}')
print(f'Situação do aluno é igual a {alunos["Situação"]}')

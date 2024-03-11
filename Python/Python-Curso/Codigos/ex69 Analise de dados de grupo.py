total = 0
homens = 0
maioridade = 0
mulheres20 = 0
continuar = 'S'
while continuar == 'S':
    total += 1
    print('======CADASTRE UMA PESSOA======')
    idade = int(input('Qual a idade dessa pessoa? ').strip())
    sexo = input('Qual o sexo desa pessaoa M/F? ').strip().upper()
    print('===============================')
    while sexo not in 'MF':
        print('Digite um sexo válido!')
        sexo = input('Qual o sexo desa pessaoa M/F? ').strip().upper()
        print('===============================')
    if sexo == 'F' and idade >= 18:
        mulheres20 += 1
    elif sexo == 'M':
        homens += 1
    if idade >= 18:
        maioridade += 1
    continuar = input('Deseja continuar S/N? ').strip().upper()

    if continuar == 'S':
        print('Digite os dados da nova pessoa:')
        print('===============================')
print('='*40)
print(f'{total} pessoas foram cadastradas no total')
print(f'{maioridade} pessoas alcançaram a maioridade')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres20} mulheres tem mais de 20 anos')
print('='*40)

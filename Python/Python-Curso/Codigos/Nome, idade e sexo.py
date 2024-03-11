pessoa1 = []
pessoa2 = []
pessoa3 = []
pessoa4 = []

for x in range(1, 5):
    dados = input('Qual o primeiro nome, idade e sexo: ').strip().lower()
    if x == 1:
        pessoa1 = dados
    elif x == 2:
        pessoa2 = dados
    elif x == 3:
        pessoa3 = dados
    elif x == 4:
        pessoa4 = dados

nome1, idade1, sexo1 = pessoa1.split()
nome2, idade2, sexo2 = pessoa2.split()
nome3, idade3, sexo3 = pessoa3.split()
nome4, idade4, sexo4 = pessoa4.split()
idadeM = (float(idade1) + float(idade2) + float(idade3) + float(idade4))/4
contf = 0
velhoh = ''
mulheres20 = 0

if int(idade1) < 20 and sexo1 == 'f': 
    mulheres20 += 1
elif int(idade2) < 20 and sexo2 == 'f':
    mulheres20 += 1
elif int(idade3) < 20 and sexo3 == 'f':
    mulheres20 += 1
else:
    if int(idade4) < 20 and sexo4 == 'f':
        mulheres20 += 1

if sexo1 == 'f': 
    contf += 1
elif sexo2 == 'f':
    contf += 1
elif sexo3 == 'f':
    contf += 1
else:
    if sexo4 == 'f':
        contf += 1

if idade1>idade2 and sexo1 == 'm':
    velhoh = nome1
elif idade2>idade3 and sexo2 == 'm':
    velhoh = nome2
elif idade3>idade4 and sexo3 == 'm':
    velhoh = nome3
else:
    if sexo4 == 'm':
        velhoh = nome4

print('''\033[31m==PESSOA 1====================================\033[m
|NOME: \033[34m{}\033[m
|IDADE: \033[34m{}\033[m
|SEXO [M/F]: \033[34m{}\033[m'''.format(nome1, idade1, sexo1.upper()))
print('''\033[31m==PESSOA 2====================================\033[m
|NOME: \033[34m{}\033[m
|IDADE: \033[34m{}\033[m
|SEXO [M/F]: \033[34m{}\033[m'''.format(nome2, idade2, sexo2.upper()))
print('''\033[31m==PESSOA 3====================================\033[m
|NOME: \033[34m{}\033[m
|IDADE: \033[34m{}\033[m
|SEXO [M/F]: \033[34m{}\033[m'''.format(nome3, idade3, sexo3.upper()))
print('''\033[31m==PESSOA 4====================================\033[m
|NOME: \033[34m{}\033[m
|IDADE: \033[34m{}\033[m
|SEXO [M/F]: \033[34m{}\033[m'''.format(nome4, idade4, sexo4.upper()))
print('\033[31m==============================================\033[m')

print('A média das idades do grupo é \033[34m{}\033[m'.format(idadeM))
print('Tem \033[34m{}\033[m mulheres no grupo'.format(contf))
print('O homem mais velho é \033[34m{}\033[m'.format(velhoh))
print('No grupo tem \033[34m{}\033[m mulheres com menos de 20 anos'.format(mulheres20))
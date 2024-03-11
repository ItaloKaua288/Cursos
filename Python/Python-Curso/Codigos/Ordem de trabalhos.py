from random import shuffle

a1=(input('Aluno 1:'))
a2=(input('Aluno 2:'))
a3=(input('Aluno 3:'))
a4=(input('Aluno 4:'))

ordem=([a1, a2, a3, a4])
shuffle(ordem)

print('A ordem das apresentações é: {}'.format(ordem))



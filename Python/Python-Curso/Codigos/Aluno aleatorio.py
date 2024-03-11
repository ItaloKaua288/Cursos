from random import randint

a1=(input('aluno 1:'))
a2=(input('aluno 2:'))
a3=(input('aluno 3:'))
a4=(input('aluno 4:'))

r= randint(1, 4)

if r==1:
    print('Aluno {} foi sorteado'.format(a1))
elif r==2:
    print('Aluno {} foi sorteado'.format(a2))
elif r==3:
    print('Aluno {} foi sorteado'.format(a3))
else:
    print('aluno {} foi sorteado'.format(a4))


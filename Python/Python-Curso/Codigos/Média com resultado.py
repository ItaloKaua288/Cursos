nota1=float(input('Nota 1: '))
nota2=float(input('Nota 2: '))
media= (nota1+nota2)/2

if media<5:
    print('Reprovado com média {}'.format(media))
elif 5<=media<=6.9:
    print('Está de recuperação {}'.format(media))
elif media>=7:
    print('Aprovado com média {}'.format(media))

from datetime import date

ano=int(input('Digite seu ano de nascimento: '))
idade= date.today().year-ano

if idade<18:
    print('Ainda vai se alistar')
    print('Ainda falta {} anos'.format(18-idade))
elif idade == 18:
    print('É hora de se alistar!')
else:
    print('Passou do prazo de se alistar')
    print('Passou {} anos'.format(idade-18))

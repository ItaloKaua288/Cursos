from datetime import date

ano=int(input('Qual ano de nascimento? '))
idade=date.today().year-ano

if idade<=9:
    print('Categoria MIRIM')
elif 9<idade<=14:
    print('Categoria INFANTIL')
elif 14<idade<=19:
    print('Categoria JUNIOR')
elif 19<idade<=20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')

salario=int(input('Qual o salario? '))

if salario>1250:
    print('Seu salario recebe reajuste de 10%, {:2f}'.format(salario+salario*(10/100)))
else:
    print('Seu salario recebe reajuste de 15%, {:2f}'.format(salario+salario*(15/100)))


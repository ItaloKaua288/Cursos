valorcasa=float(input('Valor da casa: '))
salario=int(input('Seu salario: '))
anospg=float(input('Em quantos ano vai pagar? '))

prestacao=valorcasa/anospg

if prestacao>((30/100)*salario):
    print('Compra não aprovada!')
else:
    print('Compra aprovada!')

distancia=float(input('Quantos quilometros de viagem? '))

if distancia<=200:
    print('Valor da passagem é de {}'.format(distancia*0.5))
else:
    print('Valor da passagem é de {}'.format(distancia*0.45))

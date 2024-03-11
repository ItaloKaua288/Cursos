velocidade=float(input('Qual a velocidade?'))
multa=(velocidade-80)*7

if velocidade>80:
    print('Você foi multado')
    print('Sua multa foi de {}'.format(multa))
else:
    print('Você está dentro do limite de velocidade')

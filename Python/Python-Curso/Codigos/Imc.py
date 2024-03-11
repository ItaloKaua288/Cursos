peso=float(input('Peso: '))
altura=float(input('Altura: '))
imc=peso/altura**2

if imc<18.5:
    print('Seu imc é {:.1f} e está abaixo do peso'.format(imc))
elif 25<=imc<=30:
    print('Seu imc é {:.1f} e está em sobrepeso'.format(imc))
elif 30<=imc<=40:
    print('Seu imc é {:.1f} e está em obesidade'.format(imc))
elif imc>40:
    print('Seu imc é {:.1f} e está em obesidade morbida'.format(imc))

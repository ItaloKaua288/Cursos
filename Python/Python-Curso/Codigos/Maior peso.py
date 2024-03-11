maior = 0
menor = 0

for x in range(1, 6):
    peso = float(input('Qual o peso dessa pessoa? '))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O maior peso é {} e o menor é {}'.format(maior, menor))
# Só para quando for digitado o número 999

cont = 0
soma = 0
a = 0

while a != 999:
    a = int(input('Digite um número (digite 999 para parar): '))
    if a != 999:
        cont += 1
        soma += a
print('Foram digitados {} números e a soma deles é {}'.format(cont, soma))

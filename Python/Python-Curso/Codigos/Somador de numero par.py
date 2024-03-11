soma=0
cont=0

for x in range(1, 7):
    num=int(input('Digite um numero: '))
    if num%2==0:
        soma=soma+num
        cont=cont+1
print('Dos números solicitados {} são par e a soma é {}'.format(cont, soma))


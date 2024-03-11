soma = 0
cont = 0
maior = 0
menor = 0
while True:
    num = int(input('Digite um número (digite 999 para parar): '))
    cont += 1
    soma += num
    if num == 999:
        break
    if num > maior:
        maior = num
    if menor == 0:
        menor = num
    elif menor > num:
        menor = num
print(f'Foi digitado {cont} e a soma entre eles é {soma - 999}')
print(f'o menor número é {menor} e o maior é {maior}')

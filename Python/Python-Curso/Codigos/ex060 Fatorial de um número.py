num = int(input('Qual o número? '))
fat = num
resul = 0

print('O fatorial de {} é:'.format(num))

while fat > 0 and fat < num + 1:
    if fat == num:
        print(num, end='x')
        fat -= 1
        resul = num
    if fat < num and fat > 1:
        print(fat, end='x')
        resul = resul * fat
        fat -= 1
    else:
        print(fat, end='=')
        break
print(resul)
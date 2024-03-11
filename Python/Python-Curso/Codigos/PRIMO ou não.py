num=int(input('Digite um numero: '))
total=0
for x in range(1, num+1):
    if num % x == 0:
        print('\033[34m', end=' ')
        total+=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(x), end=' ' '\033[m')
if total>2:
    print('\n Não é primo')
else:
    print('\n É primo')
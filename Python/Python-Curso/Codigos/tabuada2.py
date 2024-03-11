num=int(input('Digite um numero: ').strip())
for i in range(1,11):
    print('{} x {:2} = {}'.format(num, i, i*num))
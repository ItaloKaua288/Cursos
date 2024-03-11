num = int(input('Digite um número: '))
elem = int(input('Quantos números da sequência? '))
elem1 = elem
n1 = 0
soma = 0

print('{}A sequencia de Fibonacci do número {} é{}:'.format('\033[34m', num, '\033[m'))

while elem != 0:
    soma += n1
    if elem != 0:
        if elem == elem1 or elem1 == elem - 1:
            n1 = num
            elem -= 1
            print(n1, end=' ')
        else:
            if elem != 0 and elem >= 0:
                elem -= 1
                print(soma, end=' ')
    else:
        break

print('\n{}-FIM-{}'.format('\033[34m', '\033[m'))

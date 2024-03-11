num1 = float(input('Qual é o primeiro número? '))
num2 = float(input('Qual é o segundo número? '))
opção = 0

while opção not in (1, 5):
    print('Qual opção você deseja?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opção = int(input('Qual deseja escolher? '))
    if opção == 1:
        print('A soma de {:.2f} e {:.2f} é {:.2f}'.format(num1, num2, num1+num2))
        break
    elif opção == 2:
        print('A multiplicação de {:.2f} por {:.2f} é {:.2f}'.format(num1, num2, num1*num2))
        break
    elif opção == 3:
        maior = 0
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número entre {} e {} é {}'.format(num1, num2, maior))
        break
    elif opção == 4:
        num1 = float(input('Qual é o primeiro número? '))
        num2 = float(input('Qual é o segundo número? '))
    else:
        break
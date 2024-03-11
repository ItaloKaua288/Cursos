num1=int(input('Qual número sera convertido? '))
print('''Conversor:
[1] Decimal para binario
[2] Decimal para octal
[3] Decimal para hexadecimal''')
opção=int(input('Opção: '))

if opção==1:
    print('O número {} convertido para BINARIO é {}'.format(num1, bin(num1)))
elif opção==2:
    print('O número {} convertido para OCTAL é {}'.format(num1, oct(num1)))
elif opção==3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num1, hex(num1)))
else:
    print('Escolha uma das opções corretas')

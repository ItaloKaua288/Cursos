a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', ' sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um numero de 0 a 20: '))
    if num > 20 or num < 1:
        num = int(input('Tente novamente. Digite um numero de 0 a 20: '))
    if num < 20 or num > 1:
        print(f'== O NUMERO {num} POR EXTENSO É===')
        print(a[num])
        continar = input('Você quer continuar S/N?').strip().upper()
        while continar not in 'SN':
            continar = input('Você quer continuar S/N?').strip().upper()
    if continar == 'N':
        break

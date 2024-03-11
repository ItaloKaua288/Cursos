def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuario interrompeu o programa\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor digite um número Real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuario interrompeu o programa\033[m')
            return 0
        else:
            return n


n1 = leiafloat('Digite um Real: ')
n2 = leiaint('Digite um Inteiro: ')
print(f'O valor Inteiro digitado foi {n2} e o Real foi {n1}')


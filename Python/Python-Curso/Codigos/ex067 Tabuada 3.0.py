while True:
    num = int(input('Digite um número: '))
    if num < 0:
        print('Fim')
        break
    print(f'\033[35m-=-TABUADA DO NúMERO {num}-=-\033[m')
    for x in range(1, 11):
        print(f'{x} x {num} = {num * x}')

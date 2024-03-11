#parte 1

a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
n = 0
termo = 0
S = 'S'


while n != 10:
    n += 1
    if termo == 0:
        termo = a1
        print(termo)
    elif n != 10:
        termo += r
        print(termo)

#parte 2

rodadas = 0
n2 = 0

while S == 'S':
    S = input('Deseja continuar? S/N: ').upper()
    if S not in 'SN':
        while S not in "SN":
            print('\033[31mDigite S ou N:\033[m')
            S = input('Deseja continuar? S/N: ').upper()
    if S == 'S':
        rodadas = int(input('Quantos termos a mais deseja ver?').strip())
        if rodadas == 0:
            print('\033[33m-FIM-\033[m')
            break
        else:
            while rodadas != 0:
                if rodadas != 0:
                    rodadas -= 1
                    termo += r
                    print(termo)
    else:
        print('\33[33m-FIM-')

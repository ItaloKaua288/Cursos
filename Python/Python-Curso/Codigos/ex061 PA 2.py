a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
n = 0
termo = 0
while n != 10:
    n += 1
    if termo == 0:
        termo = a1
        print(termo)
    else:
        termo += r
        print(termo)

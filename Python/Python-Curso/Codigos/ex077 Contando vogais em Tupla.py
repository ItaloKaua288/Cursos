lista = ('Humburguer', 'Coxinha', 'Refrigerante', 'Batata-Frita', 'Pipoca', 'Chocolate')
vogais = ''

for x in range(1, len(lista)):
    if lista[x].count('a') or lista[x].count('A') != 0:
        vogais = ' a'
    if lista[x].count('e') or lista[x].count('E') != 0:
        vogais += ' e'
    if lista[x].count('i') or lista[x].count('I') != 0:
        vogais += ' i'
    if lista[x].count('o') or lista[x].count('O') != 0:
        vogais += ' o'
    if lista[x].count('u') or lista[x].count('U') != 0:
        vogais += ' u'
    print(f'Vogais da palavra {lista[x]} são:{vogais}')
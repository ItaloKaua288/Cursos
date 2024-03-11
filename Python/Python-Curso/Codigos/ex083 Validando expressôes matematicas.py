# Analiza se os parenteses estão fechados corretamente
listaex = []

expressao = input('Digite uma expressão: ')
for letra in range(0, len(expressao)):
    listaex.append(expressao[letra])

abertos = listaex.count('(')
fechados = listaex.count(')')

if abertos == fechados:
    print('Essa expressão é válida')
else:
    print('Essa expressão não é válida')

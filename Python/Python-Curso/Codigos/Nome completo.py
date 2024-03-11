nome=input('Qual seu nome?').strip()

print('Nome em maiculo:', nome.upper())
print('Nome em minusculo:', nome.lower())
print('Numero de letras:', len(''.join(nome.split())))
print('Numero de letras do primeiro nome:', len(nome.split()[0]))

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for x in range(len(junto) -1, -1, -1):
    inverso = inverso+junto[x]
#ou no lugar do 'for' e do 'inverso =' ''
#inverso = junto[::-1]

if junto==inverso:
    print('palindromo')
else:
    print('Não é palindromo')

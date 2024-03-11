frase=input('digite uma frase: ').strip()

print('Tem {} A nessa frase'.format(frase.upper().count('A')))
print('O A aparece primeiro na letra {} da frase'.format(frase.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.upper().rfind('A')+1))
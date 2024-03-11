cidade=input('digite o nome da cidade: ').strip().lower()
a=cidade.split()[0].find('santo')
lista1=cidade.split()[0]
if a==lista1:
    print('começa com SANTO')
else:
    print('Não começa com SANTO')
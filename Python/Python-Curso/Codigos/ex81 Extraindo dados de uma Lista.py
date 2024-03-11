lista = []
continuar = 'S'
while continuar == 'S':
    lista.append(int(input('Digite um número: ')))
    continuar = input('Deseja adicionar mais algum número S/N? ').upper().strip()
    while continuar not in 'SN':
        print('DIGITE UMA OPÇÂO VÁLIDA')
        continuar = input('Deseja adicionar mais algum número S/N? ').upper().strip()
print('='*60)
print(f'Foram digitados {len(lista)} número')
print(f'A lista dos valores em ordem decrescente é: {sorted(lista, reverse=True)}')
if 5 in lista:
    if lista.count(5) == 1:
        print(f'O valor 5 foi digitado na posição {lista.index(5)+1}')
    else:
        print(f'O valor 5 foi digitado na posição:', end=' ')
        for x in range(0, len(lista)):
            print(f'{lista.index(5)+1}', end='...')
else:
    print('O valor 5 não foi digitado')
print('=-=FIM=-=')
print('='*60)
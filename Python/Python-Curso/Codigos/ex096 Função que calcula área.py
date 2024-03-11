def área(l, c):
    resul = l * c
    print(f'A área do seu terreno de {l} x {c} é de {resul} metros²')


print('='*20)
print('Controle de terrenos')
print('='*20)
área(float(input('Largura do terreno em metros? ')), float(input('Comprimento do terreno em metros? ')))

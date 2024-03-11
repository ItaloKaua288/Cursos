import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(n)} é igual a {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} é igual a {moeda.dobro(n, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(n, 10, True)}')
print(f'Diminuindo em 13%, temos {moeda.diminuir(n, 13, True)}')

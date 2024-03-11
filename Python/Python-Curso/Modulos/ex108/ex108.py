import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(n)} é igual a {moeda.metade(n)}')
print(f'O dobro de {moeda.moeda(n)} é igual a {moeda.dobro(n)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(n, 10)}')
print(f'Diminuindo em 13%, temos {moeda.diminuir(n, 13)}')

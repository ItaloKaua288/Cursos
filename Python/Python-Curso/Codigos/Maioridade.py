from datetime import date

maioridade=0
menor=0
dataAtual=date.today().year

for x in range(1, 8):
    ano = int(input('Digite o ano: '))
    idade = dataAtual - ano
    if idade>18:
        maioridade = maioridade + 1
    else:
        menor = menor + 1
print('{} já atingiram a maioridade e {} ainda não atingiram a maioridade'.format(maioridade, menor))
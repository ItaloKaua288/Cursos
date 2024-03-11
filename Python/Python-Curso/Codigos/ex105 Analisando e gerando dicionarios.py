def notas(*n, sit=False):
    """
        Função para analisar as notas e situação de vários alunos.
    :param n: Notas dos alunos.
    :param sit: Valor opciona, mostra ou não a situação se for True ou False.
    :return: retorna o resultado para resp.
    """
    dados = {}
    total = 0
    maior = 0
    menor = 0
    soma = 0
    cont = len(n)
    situacao = ''
    while True:
        for x in range(0, len(n)):
            soma += n[x]
            if x == 0:
                maior = n[x]
                menor = n[x]
            else:
                if n[x] > maior:
                    maior = n[x]
                if n[x] < menor:
                    menor = n[x]
        break
    while True:
        total += 1
        cont -= 1
        if cont == 0:
            break
    media = soma / total
    dados['Total'] = total
    dados['Maior'] = maior
    dados['Menor'] = menor
    dados['Média'] = media
    if sit:
        if media >= 6:
            situacao = 'Boa'
        if media < 6:
            situacao = 'Ruim'
        dados['Situação'] = situacao
    return dados


# PROGRAMA PRINCIPAL
resp = notas(3, 10, 6.5, sit=True)
print(resp)

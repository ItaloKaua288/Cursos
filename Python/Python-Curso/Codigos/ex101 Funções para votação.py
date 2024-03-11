def voto(anonas):
    """
        Função para verificar a obrigatoriedade de voto.
    :param anonas: Ano de nascimento.
    :return: Retorna valores para resp.
    """
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - anonas
    print('='*35)
    if 65 > idade >= 18:
        return f'Com {idade} anos o voto OBRIGATORIO'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos o voto OPICIONAL'
    else:
        return f'Com {idade} anos o voto NEGADO'


# Programa principal
resp = voto(int(input('Em que ano você nasceu?')))
print(resp)
